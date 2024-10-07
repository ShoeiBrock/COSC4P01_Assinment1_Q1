import os
from hashlib import sha256

class Login:
    def __init__(self):
        self.usernames = []  # The username strings for each user account
        self.hashed_passwords = []  # The hashed passwords strings for each user account
        self.failure_nums = []  # The number of failures in a row for each user account
        self.failure_num = 0  # The number of failures in a row of the user
        self.info_path = 'data/login_info.txt'
        self.is_login = False

        self.read_information()

    def read_information(self):
        if os.path.isfile(self.info_path):
            # Read login information
            info = open(self.info_path, 'r')
            for line in info:
                tokens = line.split()
                self.usernames.append(tokens[0])
                self.hashed_passwords.append(tokens[1])
                self.failure_nums.append(int(tokens[2]))
            info.close()
        else:
            # Create a login_info.txt
            info = open(self.info_path, 'w')
            info.close()

    def signup_information(self, username, password):


        message = None
        # Write new username and hashed password in login_info.txt
        if username == '' or password == '':
            message = 'Neither username nor password is entered.'
        elif username in self.usernames:
            message = 'This username is already in use.'
        else:
            line = username + ' ' + str(sha256(password.encode()).digest()) + ' 0\n'

            if os.path.isfile(self.info_path):
                info = open(self.info_path, 'a')
            else:
                info = open(self.info_path, 'w')
            info.write(line)
            info.close()
            self.read_information()
            message = 'Your account are created successfully.'

        return message

    def validate_password(self, username, password):
        # Check if username is stored in login_info.txt
        if username not in self.usernames:
            return 'Wrong username and password!'

        # Find the index for username
        index = self.usernames.index(username)
        if self.failure_num >= 2:
            return 'You failed to login multiple times. You cannot attempt to login any more.'
        if self.failure_nums[index] >= 2:
            return 'This user is locked. You cannot login.'
        if str(sha256(password.encode()).digest()) == self.hashed_passwords[index]:
            # Reset the number of failure for this user
            self.failure_nums[index] = 0
            self.is_login = True
            # Update login_info.txt before the program terminates
            self.update_info()
            return 'Login successful! Redirecting to dashboard...'
        else:
            # Increment the failure times of both user account and the current user
            self.failure_nums[index] += 1
            self.failure_num += 1
            return 'Wrong username and password!'

    def update_info(self):
        with open(self.info_path, 'w') as info:
            for username, password, failure_num in zip(self.usernames, self.hashed_passwords, self.failure_nums):
                line = username + ' ' + str(sha256(password.encode()).digest()) + ' ' + str(failure_num) + '\n'
                info.write(line)
            info.close()
    def recreate_info(self):
        """
        This method recreates the login_info file. Not executable by user.
        This is used for unit test.
        :return:
        """
        with open(self.info_path, 'w') as f:
            f.close()
            self.usernames = []
            self.hashed_passwords = []
            self.failure_nums = []

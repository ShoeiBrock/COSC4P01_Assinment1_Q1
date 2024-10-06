import unittest
from urllib.parse import uses_query

from login import Login

class TestLogin(unittest.TestCase):
    def test_3attempts(self):
        login = Login()

        login.recreate_info()

        t_username = 'Mike'
        t_password = 'Password'
        w_username = 'Mike'
        w_password = 'AAAA'
        expected = 'You failed to login multiple times. You cannot attempt to login any more.'

        login.signup_information(t_username, t_password)
        login.validate_password(w_username, w_password)
        login.validate_password(w_username, w_password)
        result = login.validate_password(w_username, w_password)
        self.assertEqual(expected, result)

    def test_empty_username(self):
        login = Login()
        login.recreate_info()
        expected = 'Neither username nor password is entered.'

        username = ''
        password = 'PASSWORD'
        result = login.signup_information(username, password)

        self.assertEqual(expected, result)

    def test_empty_password(self):
        login = Login()
        login.recreate_info()
        expected = 'Neither username nor password is entered.'

        username = 'Mike'
        password = ''
        result = login.signup_information(username, password)

        self.assertEqual(expected, result)

    def test_valid_password(self):
        login = Login()
        login.recreate_info()
        username = 'Mike'
        password = '<PASSWORD>'
        expected = 'Login successful! Redirecting to dashboard...'

        login.signup_information(username, password)
        result = login.validate_password(username, password)
        self.assertEqual(expected, result)

    def test_invalid_password(self):
        login = Login()
        login.recreate_info()
        username = 'Mike'
        password = '<PASSWORD>'
        w_password = '<password>'
        expected = 'Wrong username and password!'

        login.signup_information(username, password)
        result = login.validate_password(username, w_password)

        self.assertEqual(expected, result)

    def test_existing_username(self):
        login = Login()
        login.recreate_info()
        username = 'Mike'
        password = '<PASSWORD>'
        expected = 'This username is already in use.'

        login.signup_information(username, password)
        result =login.signup_information(username, password)

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

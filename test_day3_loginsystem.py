import unittest
from day3_loginsystem import login_system

class TestLoginSystem(unittest.TestCase):
    def test_success(self):
        self.assertEqual(login_system("admin", "qwerty"), "Welcome admin!")

    def test_wrong_password(self):
        self.assertEqual(login_system("guest", "wrong"), "Wrong password")

    def test_no_user(self):
        self.assertEqual(login_system("hacker", "123"), "No such user")

if __name__ == "__main__":
    unittest.main()
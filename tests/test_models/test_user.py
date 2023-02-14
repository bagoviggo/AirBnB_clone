#!/usr/bin/env python3
# test_models/test_user.py

"""This module contains the tests for the User class"""

import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Set up the test"""
        self.user = User()

    def tearDown(self):
        """Tear down the test"""
        del self.user

    def test_is_instance(self):
        """Test if user is an instance of User"""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test if user has the required attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_str(self):
        """Test the string representation of the User class"""
        string = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(string, str(self.user))

    def test_email_attribute(self):
        """Test the email attribute of User class"""
        self.assertEqual(self.user.email, "")

    def test_password_attribute(self):
        """Test the password attribute of User class"""
        self.assertEqual(self.user.password, "")

    def test_first_name_attribute(self):
        """Test the first_name attribute of User class"""
        self.assertEqual(self.user.first_name, "")

    def test_last_name_attribute(self):
        """Test the last_name attribute of User class"""
        self.assertEqual(self.user.last_name, "")


if __name__ == "__main__":
    unittest.main()

# Imports
import unittest
import sys
import io
import os

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
module_under_test_path = os.path.join(project_path, "src", "08")
sys.path.append(module_under_test_path)

from contact import Contact


#Classes
class Contact_test(unittest.TestCase):

    def setUp(self):
        self.test_contact = Contact("Fritz", "Meier", "Fritz.Meier@hs-augsburg.de")

    def test_contact_name(self):
        self.assertEqual(self.test_contact.first_name, "Fritz")

    def test_contact_email(self):
        self.assertEqual(self.test_contact.email, "Fritz.Meier@hs-augsburg.de")
        test_email_list = [
            "Fritz.Meier.de",
            "Firtz.Meier@gmx.d"
            "Fritz.Meier@@gmx.de"
        ]

        for test_mail in test_email_list:
            captureOutput = io.StringIO() # Create StringIO instance
            sys.stdout = captureOutput   # redirect stdout
            self.test_contact.set_Email(test_mail)
            self.assertEqual(captureOutput.getvalue(), 
                "Your email addres is wrong: {0}\n".format(test_mail),
                "Tested email address: {0}".format(test_mail))
            self.assertIsNone(self.test_contact.email)
            sys.stdout = sys.__stdout__ #reset redirect


            #self.test_contact.email = None
            #self.assertIsNone(self.test_contact.email)

# main init
if __name__ == "__main__":
    unittest.main()

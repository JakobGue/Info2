import unittest
import io
import sys
sys.path.append('../src')

from Adressmanager.contact import Contact

test_first_name = "Andreas"
test_last_name  = "Hans"
test_mail = "Hallo@gmx.de"

class ContatTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.testContact = Contact("Andreas", "Hans", test_mail)

    def test_contact_name(self):
        self.assertEqual(self.testContact.first_name, test_first_name)
        self.assertIsInstance(self.testContact.first_name, str)
        self.assertEqual(self.testContact.last_name, test_last_name)
        self.assertIsInstance(self.testContact.last_name, str)
        #self.assertIsInstance(self.testContact.email, None)

    def test_email(self):
        self.testContact.set_Email(test_mail)
        self.assertEqual(self.testContact.email, test_mail)
        self.assertIsInstance(self.testContact.email, str)

        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        self.testContact.set_Email("Test.Person")     # Call unchanged function.               
        self.assertEqual(capturedOutput.getvalue(), "Your email addres is wrong: Test.Person\n")
        self.assertNotIsInstance(self.testContact.email, str)
        capturedOutput.truncate(0)

        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        self.testContact.set_Email("Test.Person@")     
        self.assertEqual(capturedOutput.getvalue(), "Your email addres is wrong: Test.Person@\n")
        self.assertNotIsInstance(self.testContact.email, str)      

        capturedOutput = io.StringIO()          # Create StringIO object
        sys.stdout = capturedOutput                   #  and redirect stdout.
        self.testContact.set_Email("Test.Person@gmx.d")     # Call unchanged function.‚
        self.assertEqual(capturedOutput.getvalue(), "Your email addres is wrong: Test.Person@gmx.d\n")
        self.assertNotIsInstance(self.testContact.email, str)
        
        sys.stdout = sys.__stdout__                   # Reset redirect.

    # @classmethod
    # def tearDownClass(cls):
    #     self.testContact.shutdown()

if __name__ == "__main__": # avoid python3 -m unittest contact_test.py - simply python3 contact_test.py is enough
    unittest.main()
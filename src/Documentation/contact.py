# Imports 
import json
import ssl
import threading
import urllib.request 
import urllib.parse


# classes and functions

email_domain_list = ["de", "com", "net"]

class Contact:
    """Contians the contact data of one person.

    The class contact is meant to be a summary of all personal data
    of one contact. 

    Attributes:
        first_name (str): First name of a contact
        last_name  (str): Last name of the contact
        birthday   (datetime.dateime): The date of the contacts birth.
        address    (str): Where the contact is living? 
        phone      (str): Under which number is the person reachable?
    """

    def __init__ ( self, first_name, last_name, email = None):
        """Constructor of the Contact instance.

        A contact needs at least the first name and the last name of 
        a person. The email is optional. All other contact elements
        can be setted later. 

        Args:
            first_name (str): First name of a contact. It is expected that 
                            the first letter is in caps. 
            last_name  (str): Last name of the contact
            email      (str): Email of the contact, 
                            the email is setted by the member
                            function set_Email
        Returns:
            None

        """
        self.first_name = first_name
        self.last_name  = last_name 
        self.birthday   = None
        self.address    = None
        self.phone           = None
        self.info_first_name = ""

        self.thread = threading.Thread(target=self.get_Info_to_first_name)
        self.thread.start()

        self.set_Email(email)

    def is_downloading_in_progress(self):
        self.thread.join()
        return self.thread.isAlive()

    def Contians(self, value):
        retval = False
        if value in self.first_name:
            retval = True
        elif value in self.last_name:
            retval = True
        return retval

    def __str__(self):
        """Magic function to generate the string representation. 

        Generation of the string representation of the contact. 

        Args:
            none 
        Returns:
            str: standard string representation of the contact. 

        """        
        return "First name: {0:10} | last name: {1:15} | email: {2}".format(
            self.first_name, 
            self.last_name,
            self.email)

    def get_Info_to_first_name(self):
        retValue = f"{self.first_name}: \n"

        query_parameters = {
            "action"  : "query",
            "format"  : "json",
            "list"    : "search",
            "srsearch": self.first_name
        }

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE    

        querystring = urllib.parse.urlencode(query_parameters)
        base_url = "https://en.wikipedia.org/w/api.php"
        url_request = base_url + "?" + querystring

        try: 
            with urllib.request.urlopen(url_request, context=ctx) as response:
                data = response.read()         
                decode_data = data.decode("UTF-8")      
                dict_data = json.loads(decode_data) # json.dumps () --> umgekehrte Richtung
                retValue += dict_data["query"]["search"][0]["snippet"]          
        except:
            retValue += "Nothing found."

        self.info_first_name = retValue

    def set_Email(self, email):
        """Checks and set the email of the contact. 

        The function checks the correctness of the given email address
        regarding the @-sign and the domain. 

        Args:
            email (str): The email of the contact. 
        Returns:
            None 

        """            
        returnValue = None

        if type(email) == str:
            if email.count("@") == 1:
                email_parts = email.split(".")
                if email_parts[-1] in email_domain_list:
                    returnValue = email

        if returnValue == None:
            print ("Your email addres is wrong: {0}".format(email))

        self.email = returnValue

# test code
if __name__ == "__main__":
    contact1 = Contact("Andreas", "Meier", "Andreas.Meier@gmx.de")
    print (contact1)

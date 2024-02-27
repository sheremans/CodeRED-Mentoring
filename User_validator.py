

#I create an object with the class (class has two attributes (username and email) and 2 methods (OOP)- is_valid_username and is_valid_email'
# The __init__ method is a special method (constructor) that is called when an object is created. It initializes the attributes of the object.
#to create an object of the class, you instantiate it by calling the class name as if it were a function (UserValidator() in this case).

    

    class UserValidator:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def is_valid_username(self):
        return self.username.isalpha() and len(self.username) <= 15

    def is_valid_email(self):
        return (
            self.email.startswith(self.username.lower()) and
            self.email.endswith('@ubs.com') and
            '_' in self.email and
            ' ' not in self.email
        )


user_validator_instance = UserValidator(username='', email='')


while not user_validator_instance.is_valid_username() or not user_validator_instance.is_valid_email():
   
    username_input = input("Enter a username: ").strip()  
    email_input = input("Enter an email address: ").strip()

  
    user_validator_instance = UserValidator(username=username_input, email=email_input)

   
    if not user_validator_instance.is_valid_username():
        print("Whoops! Your username does not meet the conditions.")
        print("Username conditions:")
        print("- Should have at least 1 alphabet character.")
        print("- Should not exceed 15 characters.")
    elif not user_validator_instance.is_valid_email():
        print("Whoops! Your email does not meet the conditions.")
        print("Email conditions:")
        print("- Should start with the username in lower case.")
        print("- Should end with '@ubs.com'.")
        print("- Should include an underscore ('_').")
        print("- Should not contain any whitespaces.")


print("Registration successful. You got it!")

#command line execution - task to try in terminal.Issue cannot save the file in VScodes
user_input = input("Enter something: ")

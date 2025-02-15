from datetime import datetime

class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password

    def clean_email(self):
        return self._email.lower().strip()

    def get_email(self):
        print(f"Email is accessed at {datetime.now()}")
        return self._email

    def set_email(self, new_email):
        if '@' in new_email:
            self._email = new_email.lower().strip()

    @property
    def email(self):
        print(f"Email is accessed at {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second} seconds")
        return self._email

    @email.setter
    def email(self, new_email):
        if '@' in new_email:
            print(f"New email is set as {new_email}")
            self._email = new_email.lower().strip()
        else:
            raise ValueError("Invalid email address")

    def say_hi_to_user(self,user):
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")


user1 = User('saisanthosh9154','   Saisanthosh9154@gmail.com',1234)

user2 = User('jane_doe','jane_doe@gmail.com',5678)

# user1.say_hi_to_user(user2)

# print(user1._email,' -- ',user2._email)

# print(user1._email)

# print(user1.clean_email())

# print(user2.get_email())
# user2.set_email('joe_doe@microsoft.com')
# print(user2.get_email())

print(user1.email)

user1.email = 'jos_biden@usa.com'

print(user1.email)

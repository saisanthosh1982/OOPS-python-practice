# Abstraction

# reduces the complexity by hiding unnecessary details.

class EmailService:
    def _connect(self):
        print('Connecting to the email server')

    def _authenticate(self):
        print('Autheticating...')

    def send_email(self):
        self._connect()
        self._authenticate()
        print('Sending email...')
        self._disconnect()

    def receive_email(self):
        self._connect()
        self._authenticate()
        print('Receiving email...')
        self._disconnect()

    def _disconnect(self):
        print('Disconnecting from the email server')


email = EmailService()
email.send_email()
email.receive_email()

# Note: In the above example, we have abstracted the 'connect', 'authenticate', and 'disconnect' methods. We have made them private using the underscore prefix. 
# This means they are not accessible outside the class. This makes the code more secure and prevents unauthorized access to these methods. 
# However, they can still be called from within the class if necessary.


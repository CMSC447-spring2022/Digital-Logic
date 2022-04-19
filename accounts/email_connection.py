import smtplib, ssl
import json
from os.path import exists
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


def initconn(debug):
    if debug:
        logging.info("logging in to email with localhost")
        port = 1025
        stmp_server = 'localhost'
        username = 'test@test.com'
    elif exists('../../secret'):
        logging.info("logging in to email with gmail")
        with open('../../secret', 'rb') as configfile:
            config = json.load(configfile)
        port = 465  # For SSL
        username = config['email']['username']
        password = config['email']['password']
        stmp_server = 'smtp.gmail.com'
    else:
        logging.warning("no secret file found, defaulting to localhost for email login")
        port = 1025
        stmp_server = 'localhost'
        username = 'test@test.com'

    # Create a secure SSL context
    context = ssl.create_default_context()
    print('about to connect')
    server = smtplib.SMTP_SSL(stmp_server, port, context=context)
    if stmp_server != 'localhost':
        server.login(username, password)
    print('connected')
    return server, username


class Email:
    def __init__(self, debug=True):
        self.conn, self.username = initconn(debug)

    def send_mail(self, to_email, message_subject, message_body):
        message = f"""\
        Subject: {message_subject}
        
        {message_body}"""
        self.conn.sendmail(to_email, self.username, message)


if __name__ == '__main__':
    e = Email()
    print(e)

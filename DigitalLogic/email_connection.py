# https://realpython.com/python-send-email/

import smtplib, ssl
import json, os
from os.path import exists
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


def initconn(debug):
    secret_path = os.path.dirname(__file__) + '/../../secret'
    if debug:
        logging.info("debug mode, not logging in")
        return '', 'test@test.com'
    elif exists(secret_path):
        logging.info("logging in to email with gmail")
        with open(secret_path, 'rb') as configfile:
            config = json.load(configfile)
        port = 465  # For SSL
        username = config['email']['username']
        password = config['email']['password']
        stmp_server = 'smtp.gmail.com'
    else:
        logging.warning("no secret file found, defaulting to debug mode for email login")
        return '', 'test@test.com'

    # Create a secure SSL context
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(stmp_server, port, context=context)
    server.login(username, password)
    return server, username


class Email:
    def __init__(self, debug=False):
        self.conn, self.username = initconn(debug)
        self.debug = True if self.conn == '' else False

    def send_mail(self, to_email, message_subject, message_body):
        if self.debug:
            return 0
        message = f"""Subject: {message_subject}\n\n{message_body}"""
        try:
            self.conn.sendmail(self.username, to_email, message)
            return 1
        except smtplib.SMTPException:
            logging.warning('sending email failed')
            return -1

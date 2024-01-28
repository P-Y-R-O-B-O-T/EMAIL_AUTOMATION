import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#$$$$$$$$$$#

class Email() :
    def __init__(self,
                 server_addr: str) -> None :
        self.SSL_CONTEXT = ssl.create_default_context()
        self.SERVER = smtplib.SMTP(server_addr)
        self.SERVER.ehlo()
        self.SERVER.starttls()
        self.SERVER.ehlo()

    def set_template(self,
                     template: str) -> None :
        self.TEMPLATE = template

    def set_user_pass(self,
              email: str,
              passwd: str) -> None :
        self.EMAIL = email
        self.PASS = passwd

    def login(self) -> None :
        self.SERVER.login(self.EMAIL,
                          self.PASS)

    def send_mail(self,
                  recipient: str,
                  subject: str,
                  format_data: dict = None,
                  attachments: list = []) -> None :
        message = MIMEMultipart()
        message["Subject"] = subject
        message["From"] = self.EMAIL
        message["To"] = recipient

        body = MIMEText(self.TEMPLATE.format(**format_data),
                        "HTML".lower())

        message.attach(body)

        self.attach_files(message,
                          attachments)

        text = message.as_string()

        self.SERVER.sendmail(self.EMAIL,
                             recipient,
                             text)

    def attach_files(self,
                     message: str,
                     attachments: str) -> None :
        for _ in attachments :
            file_handle = open(_, "rb")
            mime_base_part = MIMEBase("application",
                                      "octet-stream")
            mime_base_part.set_payload(file_handle.read())
            encoders.encode_base64(mime_base_part)
            mime_base_part.add_header("Content-Disposition",
                                      "attachment; filename= {0}".format(_))
            message.attach(mime_base_part)

#$$$$$$$$$$#

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(report_path):

    sender = "venkymanjunavi@gmail.com"
    password = "lkarctjbwatqzqbb"
    receiver = "manjusprout@gmail.com"

    msg = MIMEMultipart()
    msg['Subject'] = "Automated Report"
    msg['From'] = sender
    msg['To'] = receiver

    attachment = open(report_path, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)

    part.add_header(
        'Content-Disposition',
        f'attachment; filename=report.pdf'
    )

    msg.attach(part)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender, password)
    server.send_message(msg)
    server.quit()
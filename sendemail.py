import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# SMTP Server Settings
smtp_server = 'smtp-relay.sendinblue.com'
smtp_port = 587

# Your Email Login Credentials
email = 'youremailid@gmail.com'
password = 'your password'

# Recipient Email Address
to_email = 'sender mail id@gmail.com'

# Email Content
subject = 'Sample Email Subject'
body = 'This is a sample email sent using Python.'

# File to be attached
file_path = 'file name.csv'

# Create the email message
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Attach the file
attachment = open(file_path, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename={file_path}')
msg.attach(part)

# Connect to the SMTP server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email, password)
    
    # Send the email
    server.sendmail(email, to_email, msg.as_string())
    print('Email with attachment sent successfully!')
except Exception as e:
    print(f'An error occurred: {str(e)}')
finally:
    # Quit the server
    server.quit()

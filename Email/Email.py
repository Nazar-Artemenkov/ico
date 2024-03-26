import smtplib, ssl
from email.message import EmailMessage
import imghdr
smtp_server = "smtp.gmail.com"
port = 587
sender_email ="Telefonredmi782@gmail.com"
password = input("Kirjuta oma salsõna ja vajuta enter:")
context = ssl.create_default_context()
msg = EmailMessage()
msg.set_content("...")
msg['Subject']="Kirja teema"
msg['From']="Nazar Artemenkov"
msg['to']="marina.oleinik@tthk.ee"
with open("hit.png",'rb') as fpilt:
    pilt=fpilt.read()
msg.add_attachment(pilt,maintype='image',subtype=imghdr.what(None, pilt))
try:
    server = smtplib.SMTP(smtp_server,port)
    server.starttls(context=context)
    server.login(sender_email, password)
    server.send_message(msg)
    print("Kiri on saatnud")
except Exception as e:
    print(e)
finally:
    server.quit()
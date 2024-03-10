import csv,smtplib,ssl,urllib.request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

efrom="thenetxnewsletter@gmail.com"
passw=""
msubj="NewsLetter"
tolist="t.csv"
newsimg="i.img"

msgroot=MIMEMultipart('related')
msgroot['Subject']=msubj
msgroot['From']=efrom
msgroot['To']=efrom
msgroot.preamble='This is a multi-part message in MIME format.'

msgalt=MIMEMultipart('alternative')
msgroot.attach(msgalt)

msghtml=MIMEText('<img src="cid:image1">', 'html')
msgalt.attach(msghtml)

fp=open(newsimg, 'rb')
msgimg1=MIMEImage(fp.read(),_subtype="png")
fp.close()

msgimg1.add_header('Content-ID', '<image1>')
msgroot.attach(msgimg1)

context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(efrom, passw)
    with open(tolist, 'r') as file:
        reader=csv.reader(file)
        next(reader)
        for name,email in reader:
            msgroot['To']=email
            server.sendmail(efrom, email, msgroot)
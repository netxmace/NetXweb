htmlnx = """\
<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">


<head>
    <title>Email Title</title>

    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="x-apple-disable-message-reformatting" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./style/styles.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
	
</head>

<body style="background-color:silver;">
<table style="width:100%;border-spacing:0px;" >
 
<tr> 
	<td style="width:10%;">&nbsp;</td> 
	<td style="color: white;background-color:black"><b>&nbsp;Hello {name}, </b> </td>  
	<td style="width:10%">&nbsp;</td> 
</tr>


<tr> 
	<td style="width:10%">&nbsp;</td> 
	<td style="width:80%;background-color:black" > <a href ="https://netxmace.github.io/"><img style="display:block;" width="100%" height="100%" src="cid:image1" alt="newsletter" id="a"></a> </td> 
	<td style="width:10%">&nbsp;</td> 
</tr>

<tr> 
   <td style="width:10%;">&nbsp;</td> 
   <td style="color: white;font-size:10px;text-align: center;background-color:black"> <i> Mail is send from NetX club MACE</i> </td> 
   <td style="width:10%">&nbsp;</td> 
</tr>

<tr> 
   <td style="width:10%;">&nbsp;</td> 
   <td style="color: white;font-size:10px;text-align: center;background-color:black"> <i>*Click the image to visit our webpage</i> </td> 
   <td style="width:10%">&nbsp;</td> 
</tr>
 
</table>

<body>

</html>
			
"""

import csv,smtplib,ssl,urllib.request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

efrom="thenetxnewsletter@gmail.com"
passw="aoihclfynjgbhpfq"
msubj="NewsLetter"
tolist=r"D:\NetX\NetXweb\NL Auto Mailing\testcsv.csv"
newsimg=r"D:\NetX\NetXweb\NL Auto Mailing\Newsletter.png"

msgroot=MIMEMultipart('related')
msgroot['Subject']=msubj
msgroot['From']=efrom
msgroot['To']=efrom
msgroot.preamble='This is a multi-part message in MIME format.'

msgalt=MIMEMultipart('alternative')
msgroot.attach(msgalt)

msghtml=MIMEText(htmlnx, 'html')
msgalt.attach(msghtml)

fp=open(newsimg, 'rb')
msgimg1=MIMEImage(fp.read(),_subtype="png")
fp.close()

msgimg1.add_header('Content-ID', '<image1>')
msgroot.attach(msgimg1)

context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(efrom, passw)
    with open(tolist) as file:
        reader=csv.reader(file)
        next(reader)
        for name,email in reader:
            mailmsg=msgroot.as_string().format(name=name)
            server.sendmail(efrom, email, mailmsg)
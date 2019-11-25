def sendEmailNotification(toaddr, category, location, imageName, imageLocation):
    import smtplib 
    from email.mime.multipart import MIMEMultipart 
    from email.mime.text import MIMEText 
    from email.mime.base import MIMEBase 
    from email import encoders 
    fromaddr = "nsrk9393@gmail.com"
    #toaddr = "siva.nulakani@gmail.com"
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = "SmartBin-e-Alert Notification"
    body = "Hello,\n\n" + category + " identified at location " + location + " and need your attention to make our workspace clean.\n\n Thanks\n SmartBin-e-Alert Team"
    msg.attach(MIMEText(body, 'plain')) 
    filename = imageName
    attachment = open(imageLocation, "rb") 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, "Syam9492@Akp") 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()
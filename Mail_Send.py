import smtplib

class Report_On_Mail:

    def __init__(self,email,password):
        self.email = email
        self.password = password

    def send_mail(self,message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email,self.password)
        server.sendmail(self.email,self.email,message)
        server.quit()

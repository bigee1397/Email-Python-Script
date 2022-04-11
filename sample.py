
import smtplib


sender_email = "Sender's mail id"
rec_email = "Receiver's mail id"
password1 = "Enter sender's password"
message = "Enter message here"


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password1)
server.sendmail(sender_email, rec_email, message)
server.quit()
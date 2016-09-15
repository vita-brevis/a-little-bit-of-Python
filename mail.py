import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("frommail", "password")
msg = "MESSAGE: My name is Sherlock Holmes.  It is my business to know what other people don't know.!"
server.sendmail("frommail", "tomail", msg)
server.quit()

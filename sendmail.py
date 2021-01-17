import smtplib

def send_message(login, password, subject, message_text, send_to):
	smtp_server = "smtp.gmail.com"
	port = 587

	server = smtplib.SMTP(smtp_server, port)
	server.starttls()

	server.login(login, password)

	msg = f"Subject: {subject}\n\n{message_text}"

	server.sendmail(login, send_to, msg)

	server.quit()

login = input("You'r g-mail: ")
passwd = input("Type password: ")
to = input("Receiver: ")
subj = input("Subject: ") 
msg_text = input("msg: ")

send_message(login, passwd, subj, msg_text, to)
print("\nSuccessfully sent.")
import smtplib
import email.message
import os
from dotenv import load_dotenv

load_dotenv()
login = os.getenv("EMAIL")
senha = os.getenv("SENHA")
debug = os.getenv("DEBUG")

def enviar_email():
    msg = email.message.Message()
    msg["Subject"] = "Teste de e-mail automatizado - Servidor Python"
    msg["From"] = login
    msg["To"] = login

    email_body = """<p>Olá,<p>
     <p>Este é um teste de automação via servidor<p>
     <p>Obrigado!!"""

    email_body = email_body.encode("utf-8")

    msg.add_header("Content-Type","text/html")
    msg.set_payload(email_body)

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(login,senha)
    servidor.send_message(msg)
    servidor.quit()
    print('Email enviado com sucesso')
    return

if __name__ == "__main__":
    try:
        enviar_email()
    except Exception as e:
        print(f'Error: {e}')

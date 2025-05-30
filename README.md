# 💌 Envio de E-mail Automatizado com GitHub Actions

Este projeto envia e-mails automaticamente a cada 4 horas utilizando Python e o agendador gratuito do GitHub Actions.

## 📦 Sobre o projeto

O script `teste_email.py` envia um e-mail HTML personalizado usando o servidor SMTP do Gmail. O agendamento é feito por meio de workflows do GitHub Actions, que rodam o script periodicamente sem necessidade de servidor.

---

## 🚀 Funcionalidades

- Envio de e-mail automático a cada 4 horas
- Uso seguro de variáveis sensíveis (como senha do e-mail)
- Integração com GitHub Actions (agendamento gratuito)
- Compatível com contas Gmail (via App Password)

---

## ⚙️ Pré-requisitos

- Conta GitHub
- Conta Gmail com [senha de app](https://myaccount.google.com/apppasswords)
- Python 3.8+

---

## 🔐 Como configurar os segredos

1. No seu repositório no GitHub, vá até:
   **Settings > Secrets and variables > Actions > New repository secret**

2. Adicione as seguintes variáveis:

| Nome do Secret | Descrição                        |
|----------------|----------------------------------|
| `EMAIL`        | Seu e-mail de envio              |
| `SENHA`        | Senha de app do Gmail            |
| `DEBUG`        | Valor `True` ou `False`          |

---

## 🕒 Agendamento

O script é executado automaticamente **a cada 4 horas**, usando o seguinte cron:

```yaml
schedule:
  - cron: "0 */4 * * *"

# :envelope: Python Automate Gmail Sender :envelope:

## Instalation 
<strong>On Linux</strong> (on Windows analogously, but some commands might be different)
1. Clone my repository
``` bash
git  clone https://github.com/wysogladszymon/Python-Automate-Email-Sender.git
```
2. Go to repository folder using
``` bash
cd Python-Automate-Email-Sender
```
3. Enable two-step verification on your google account (this from where you want to send your email)
4. Go to this [link](https://myaccount.google.com/u/4/apppasswords) to set an app email password.
5. Fill gaps and paste received 16-digits password.
6. Create .env file:
``` bash
echo EMAIL_SENDER = "" > .env
echo EMAIL_PASSWORD = "" >> .env
echo EMAIL_RECEIVER = "" >> .env
```
7. Fill informations in ``` .env ``` file and you are ready to go.
8. In file ``` message.txt ``` put email content, where first line should be an email header.
``` bash
touch message.txt
```
9. Run this program using:
``` bash
source myenv/bin/activate
python3 emailSender.py
```

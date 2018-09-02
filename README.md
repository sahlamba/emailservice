# emailservice

Python CLI tool to send mails!

### Setup Project

Make sure you have [python3](https://www.python.org/download/releases/3.0/) and [pipenv](https://github.com/pypa/pipenv) installed in your system -

```shell
$ python3 --version
Python 3.5.0

$ pipenv --version
pipenv, version 2018.7.1
```

Clone the repo and `cd` into it

```shell
$ git clone https://github.com/thedrumsknight/emailservice.git && cd emailservice
```

Setup virtualenv with Python 3.5 and install dependencies

```shell
$ pipenv --python 3.5 && pipenv install
```

### Setup `.env`

Create a `.env` file in the root dir with the following keys -

```bash
# .env
SMTP_HOST='smtp.gmail.com'
SMTP_PORT=587

SENDER_EMAIL='<sender_email_address>'
SENDER_EMAIL_PASSWORD='<password>'

RECEIVER_EMAIL='<receiver_email_address>'

EMAIL_SUBJECT='A message from the Pi'
```

### Script Usage

Run the script in virtualenv -

```shell
$ pipenv run python3 ./send-mail.py
```

### Customize the Program

- Edit account details and email subject in `.env` file.
- Edit the message templates in the [templates](templates) dir.
- Edit type of message sent in `main()` in [send-mail.py](send-mail.py).

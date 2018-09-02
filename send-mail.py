#!/usr/bin/python3
import click

from mailer import mailer
from dotenv import load_dotenv

def plain(recipient_email, sub, mesg):
    msg = mailer.build_plain_message('templates/default.txt', recipient_email, sub, mesg)
    mailer.send_mail(msg)

def html(recipient_email):
    msg = mailer.build_html_message('templates/reboot.html', recipient_email)
    mailer.send_mail(msg)

@click.command()
@click.option('-s', '--subject', help="Subject of the email.")
@click.option('-m', '--message', help="Message to be sent in the email.")
@click.argument('recipient_email')
def send(subject, message, recipient_email):
    # Load .env
    load_dotenv()
    # Send plain text mail
    plain(recipient_email, subject, message)
    # Send HTML content mail
    # html()

if __name__ == '__main__':
    send()

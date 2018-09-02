#!/usr/bin/python3
import click

from mailer import mailer
from dotenv import load_dotenv

def plain(recipient_email):
    msg = mailer.build_plain_message('templates/default.txt', recipient_email)
    mailer.send_mail(msg)

def html(recipient_email):
    msg = mailer.build_html_message('templates/reboot.html', recipient_email)
    mailer.send_mail(msg)

@click.command()
@click.option('--s', help='Subject of the email.')
@click.option('--m', help='Message to be sent.')
@click.argument('recipient_email')
def send(s, m, recipient_email):
    # Load .env
    load_dotenv()
    # Send plain text mail
    plain(recipient_email)
    # Send HTML content mail
    # html()

if __name__ == '__main__':
    send()
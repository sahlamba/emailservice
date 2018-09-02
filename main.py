from mailer import mailer
from dotenv import load_dotenv

def plain():
    msg = mailer.build_plain_message('templates/reboot.txt')
    mailer.send_mail(msg)

def html():
    msg = mailer.build_html_message('templates/reboot.html')
    mailer.send_mail(msg)

def main():
    # Load .env
    load_dotenv()
    # Send plain text mail
    plain()
    # Send HTML content mail
    html()

if __name__ == '__main__':
    main()
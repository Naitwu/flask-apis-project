import os
import requests
from dotenv import load_dotenv
import jinja2

load_dotenv()

template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)

def render_template(template_name, **context):
    template = template_env.get_template(template_name)
    return template.render(**context)

def send_simple_message(to, subject, text, html):
    return requests.post(
        url=f"https://api.mailgun.net/v3/{os.getenv('MAILGUN_DOMAIN')}/messages",
        auth=("api", os.getenv('MAILGUN_API_KEY')),
        data={
            "from": f"Will <mailgun@{os.getenv('MAILGUN_DOMAIN')}>",
            "to": [to],
            "subject": subject,
            "text": text,
            "html": html
        }
    )

def send_user_registration_email(username, email):
    return send_simple_message(
        to=email,
        subject="Welcome to our service!",
        text=f"Hello {username}, thank you for registering!",
        html=render_template("email/action.html", username=username)
    )
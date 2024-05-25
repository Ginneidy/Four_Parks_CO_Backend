from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def send_admin_password(email, temporary_password):
    """
    This function sends the password to the admin user
    """
    subject = "Four Parks - Contraseña de administrador"

    message = f"Su contraseña temporal es: {temporary_password}"
    html_message = render_to_string(
        "emails/admin_mail.html", {"temporary_password": temporary_password}
    )
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        html_message=html_message,
    )


def send_activation_mail(email, activation_code):
    subject = "Activa tu usuario de four parks"
    message = (
        f"Gracias por registrarte! Este es tu código de activación: {activation_code}"
    )
    html_message = render_to_string(
        "emails/mail.html", {"activation_code": activation_code}
    )
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        html_message=html_message,
    )

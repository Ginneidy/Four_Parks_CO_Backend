from datetime import datetime

from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings

from email.mime.image import MIMEImage

from helpers.PDF.booking_pdf import generate_pdf_booking
from helpers.qrcode_helpers import generate_qr_code


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


def send_mail_confirmation_reservation(user, parking, booking):
    booking_code = "FP-" + str(booking["id"])
    # Generar código QR
    qr_buffer = generate_qr_code(booking_code)
    qr_buffer.seek(0)  # Reset buffer position after generating QR code

    # Convert booking["check_in"] and booking["check_out"] to datetime objects
    check_in = datetime.strptime(booking.check_in, "%Y-%m-%dT%H:%M:%SZ")
    check_out = datetime.strptime(booking.check_out, "%Y-%m-%dT%H:%M:%SZ")

    # Generar PDF con el código QR
    reserva_detalles = {
        "reservation_id": booking_code,
        "parking_name": parking.park_name,
        "address": parking.street_address,
        "reservation_date": check_in.strftime("%Y-%m-%d"),
        "time_slot": check_in.strftime("%H:%M") + " - " + check_out.strftime("%H:%M"),
        "total_price": booking["total_amount"],
    }
    pdf_buffer = generate_pdf_booking(reserva_detalles, qr_buffer)

    # Crear contenido del correo
    subject = "Confirmación de Reserva de Four Parks"
    html_message = render_to_string(
        "emails/parking_reservation_confirmation.html",
        {
            "user_name": user.user_name + " " + user.last_name,
            "reservation_id": booking_code,
            "parking_name": parking.park_name,
            "address": parking.street_address,
            "reservation_date": check_in.strftime("%Y-%m-%d"),
            "time_slot": check_in.strftime("%H:%M")
            + " - "
            + check_out.strftime("%H:%M"),
            "total_price": booking["total_amount"],
            "view_reservation_url": "/",
        },
    )
    message = strip_tags(html_message)

    # Crear email con alternativas
    email = EmailMultiAlternatives(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [user.email_address],
    )
    email.attach_alternative(html_message, "text/html")

    # Adjuntar el código QR como imagen en el correo
    qr_buffer.seek(0)  # Reset buffer position before attaching
    qr_image = MIMEImage(qr_buffer.read())
    qr_image.add_header("Content-ID", "<qr_code>")
    email.attach(qr_image)

    # Adjuntar el PDF
    email.attach("reserva_detalles.pdf", pdf_buffer.read(), "fpreservation/pdf")

    email.send()


def send_payment_confirmation_mail(user, credit_card, booking):
    subject = "Confirmación de Pago - Four Parks"

    # Detalles del pago
    card_last_digits = credit_card.card_number[-4:]
    payment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Cálculo del total y desglose
    total = booking.total_amount

    duration = booking.check_out - booking.check_in
    daily_fee = (
        booking.parking.fee.filter(vehicle_type=booking.vehicle.vehicle_type)
        .get(fee_type__description="dia")
        .amount
    )
    hourly_fee = (
        booking.parking.fee.filter(vehicle_type=booking.vehicle.vehicle_type)
        .get(fee_type__description="hora")
        .amount
    )
    minute_fee = (
        booking.parking.fee.filter(vehicle_type=booking.vehicle.vehicle_type)
        .get(fee_type__description="minuto")
        .amount
    )
    reservation_fee = (
        booking.parking.fee.filter(vehicle_type=booking.vehicle.vehicle_type)
        .get(fee_type__description="reserva")
        .amount
    )

    total_days = duration.days
    total_hours = duration.seconds // 3600
    total_minutes = (duration.seconds % 3600) // 60

    # Crear mensaje HTML
    html_message = render_to_string(
        "emails/payment_confirmation.html",
        {
            "user_name": user.user_name + " " + user.last_name,
            "card_last_digits": card_last_digits,
            "payment_date": payment_date,
            "total": total,
            "booking_id": "FP-" + str(booking.id),
            "reservation_fee": reservation_fee,
            "daily_fee": daily_fee,
            "hourly_fee": hourly_fee,
            "minute_fee": minute_fee,
            "total_days": total_days,
            "total_hours": total_hours,
            "total_minutes": total_minutes,
        },
    )
    message = strip_tags(html_message)

    # Crear email con alternativas
    email = EmailMultiAlternatives(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [user.email_address],
    )
    email.attach_alternative(html_message, "text/html")

    email.send()

from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, blue, grey

from io import BytesIO
import requests

# Obtener el logo de la empresa
logo_url = "https://i.ibb.co/vjfSVXL/SVG-to-PNG-logo.png"  # Reemplaza con la URL correcta del logo
response = requests.get(logo_url)
if response.status_code == 200:
    logo_buffer = BytesIO(response.content)
else:
    raise Exception("No se pudo descargar el logo de la empresa.")


def generate_pdf_booking(reserva_detalles, qr_buffer):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Agregar logo de la empresa
    145 * 203

    logo_image = ImageReader(logo_buffer)
    c.drawImage(
        logo_image, width / 2 - 54.375, height - 1.5 * inch, 108.75, 152.25, mask="auto"
    )

    # Título del documento
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(black)
    c.drawCentredString(width / 2, height - 2 * inch, "Four Parks")

    # Título de la sección
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(black)
    c.drawString(40, height - 2.8 * inch, "Detalles de la Reserva")

    # Línea divisoria
    c.setLineWidth(1)
    c.setStrokeColor(black)
    c.line(40, height - 2.9 * inch, width - 40, height - 2.9 * inch)

    # Información del huésped
    reserva_y = height - 3.4 * inch
    c.setFont("Helvetica", 12)
    line_height = 20

    c.drawString(40, reserva_y, f"ID de Reserva: {reserva_detalles['reservation_id']}")
    reserva_y -= line_height
    c.drawString(40, reserva_y, f"Parqueadero: {reserva_detalles['parking_name']}")
    reserva_y -= line_height
    c.drawString(40, reserva_y, f"Dirección: {reserva_detalles['address']}")
    reserva_y -= line_height
    c.drawString(
        40, reserva_y, f"Fecha de Reserva: {reserva_detalles['reservation_date']}"
    )
    reserva_y -= line_height
    c.drawString(40, reserva_y, f"Horario: {reserva_detalles['time_slot']}")
    reserva_y -= line_height
    c.drawString(40, reserva_y, f"Precio Total: ${reserva_detalles['total_price']}")

    # Instrucción para el código QR
    c.setFont("Helvetica-Bold", 12)
    reserva_y -= 40
    c.drawString(40, reserva_y, "Presenta este código QR para confirmar tu reserva:")

    # Convertir qr_buffer a un objeto de imagen compatible
    qr_image = ImageReader(qr_buffer)

    # Incluir el código QR en el PDF
    c.drawImage(qr_image, 40, reserva_y - 150, 2 * inch, 2 * inch)

    # Pie de página con información de contacto
    c.setFont("Helvetica", 10)
    c.setFillColor(grey)
    c.drawString(40, 50, "Contacto: info@fourparks.com | Tel: (555) 555-5555")
    c.drawString(40, 35, "Dirección: 123 Parque St., Ciudad, País")
    c.drawString(40, 20, "Website: www.fourparks.com")

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer


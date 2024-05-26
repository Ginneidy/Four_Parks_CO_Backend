import os
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.conf import settings


def generate_parking_usage_pdf(data):
    template_path = "reports/parking_usage_report.html"
    context = {"report": data}

    # Render the HTML template with context data
    html = render_to_string(template_path, context)

    # Create a PDF file
    result = open(os.path.join(settings.MEDIA_ROOT, "parking_usage_report.pdf"), "wb")

    # Convert HTML to PDF
    pisa_status = pisa.CreatePDF(html, dest=result)

    # Close the file
    result.close()

    if pisa_status.err:
        return None
    return os.path.join(settings.MEDIA_ROOT, "parking_usage_report.pdf")

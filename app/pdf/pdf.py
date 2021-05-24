# This module is responsible for generating the report in PDF format
from reportlab.pdfgen import canvas


def header(filename=None, font=None, size=None, title=None, domain=None, ip=None):
    """This function is responsible for drawing a header in the pdf and integrating a body with the results"""
    if not filename or not font or not size or not title or not domain or not ip:
        # If one of the parameters is empty, an error message is displayed
        print("Try again please")
    else:
        pdf = canvas.Canvas(filename + '.pdf')
        pdf.setFont(font, size)
        pdf.setTitle(filename)
        pdf.drawCentredString(300, 790, "Website IP Tracker")
        pdf.setFont("Helvetica", 16)
        pdf.drawCentredString(300, 765, "tracks the IP address of any website")

        body(pdf, "Helvetica", 14, domain, ip)


def body(pdf, font, size, domain, ip):
    """This function is responsible for integrating a body with the results in the PDF report"""
    domain_obj = pdf.beginText(40, 680)
    domain_obj.setFont(font, size)
    domain_obj.textLine(f"Domain: {domain}")
    pdf.drawText(domain_obj)

    ip_obj = pdf.beginText(40, 650)
    ip_obj.setFont(font, size)
    ip_obj.textLine(f"IP: {ip}")
    pdf.drawText(ip_obj)
    pdf.setFont(font, 12)
    pdf.drawCentredString(300, 60, "Developed by Mazzya : https://github.com/mazzya")
    pdf.drawCentredString(300, 40, "Project repository : https://github.com/mazzya/website-ip-tracker")
    pdf.drawCentredString(300, 10, "Version : 1.1.0")
    pdf.save()
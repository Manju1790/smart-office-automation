from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Table
import os

REPORT_FOLDER = "reports"

def create_report(file_name, total, average):

    report_path = os.path.join(REPORT_FOLDER, f"{file_name}_report.pdf")

    doc = SimpleDocTemplate(report_path)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Smart Office Automation Report", styles["Title"]))
    elements.append(Spacer(1, 20))

    data = [
        ["Total Amount", total],
        ["Average Amount", average]
    ]

    table = Table(data)
    elements.append(table)

    doc.build(elements)

    return report_path
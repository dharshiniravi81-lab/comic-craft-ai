import os
from datetime import datetime
from fpdf import FPDF


def save_pdf(layout):
    os.makedirs(
        "static/exports",
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"comic_{timestamp}.pdf"

    filepath = os.path.join(
        "static",
        "exports",
        filename
    )

    pdf = FPDF()

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    for panel in layout:

        pdf.add_page()

        pdf.set_font(
            "Arial",
            "B",
            20
        )

        pdf.cell(
            0,
            12,
            f"Panel {panel['panel']}: {panel['title']}",
            ln=True
        )

        image_path = panel["image"]

        if os.path.exists(image_path):
            pdf.image(
                image_path,
                x=15,
                y=35,
                w=180
            )

        pdf.set_y(150)

        pdf.set_font(
            "Arial",
            "I",
            11
        )

        pdf.multi_cell(
            0,
            8,
            panel["scene_description"]
        )

        pdf.ln(5)

        pdf.set_font(
            "Arial",
            "",
            11
        )

        pdf.multi_cell(
            0,
            8,
            panel["story"]
        )

    pdf.output(filepath)

    return filepath
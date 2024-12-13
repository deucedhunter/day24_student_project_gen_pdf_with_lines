from email.header import Header

import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')
for index, row in df.iterrows():
    topic = row["Topic"]
    pages = int(row["Pages"])

    # Header
    pdf.add_page()
    pdf.set_font(family="Arial", style="B", size=24)
    pdf.cell(w=0, h=12, txt=topic,
             align="L", ln=1)
    # Footer
    pdf.ln(265)
    pdf.set_font(family="Arial", style="I", size=12)
    pdf.cell(w=0, h=8, txt=topic,
             align="R", ln=1)

    for height in range(20, 277, 10):
        pdf.line(10,height,200,height)
    for page in range(pages-1):
        pdf.add_page()
        for y in range(20, 277, 10):
            pdf.line(10,y,200,y)
        # Footer
        pdf.ln(277)
        pdf.set_font(family="Arial", style="I", size=12)
        pdf.cell(w=0, h=8, txt=topic,
                 align="R", ln=1)
pdf.output("output.pdf")
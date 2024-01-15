from fpdf import FPDF
import pandas

pdf=FPDF(orientation="P",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
pd=pandas.read_csv("topics.csv")

for index,rows in pd.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times",size=22,style="I")
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=rows["Topic"],align="L",ln=1)
    pdf.line(10,20,200,20)

    for y in range(20,298,10):
        pdf.line(10,y,200,y)
    pdf.line(10,21,200,21)

    pdf.ln(265)
    pdf.set_font(family="Times",size=10,style="U")
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=rows["Topic"],align="L",ln=1)


    for i in range(rows["Pages"]-1):
        pdf.add_page()
        for y in range(20, 288, 10):
            pdf.line(10, y, 200, y)
        pdf.line(10, 21, 200, 21)

        pdf.ln(270)
        pdf.set_font(family="Times", size=10, style="U")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=rows["Topic"], align="L", ln=1)


pdf.output("output.pdf")
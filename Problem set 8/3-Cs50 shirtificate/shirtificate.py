from fpdf import FPDF

class Pdf():
    def __init__(self,name):
        self._pdf=FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 45)
        self.pdf.cell(0, 60, "CS50 Shirtificate", align="C")
        self.pdf.image("shirtificate.png", x=self._pdf.epw)
        self.pdf.set_font_size(30)
        self.pdf.set_text_color(255,255,255)
        self. pdf.text(x=46 , y=140, txt=f"{name} took CS50")
    def save(self,name):
        self._pdf.output(name)
        
name=input("Name: ")
pdf=Pdf(name)
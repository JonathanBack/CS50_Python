from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.set_y(30)
        self.set_font("helvetica", "B", 35)
        # Printing title:
        self.cell( text = "CS50 Shirtificate", border=0, align="C", center = True)
        self.ln(90)


# Instantiation of inherited class
def main():
    pdf = PDF(orientation="P", unit="mm", format="A4")
    img = Image.open('shirtificate.png')
    shirt = generate_pdf(pdf, img)

def center_image(pdf, img):

    img_width, img_height = img.size
    # A4 = 210mm wide by 297mm tall.
    page_width = int(pdf.w)
    page_height = int(pdf.h)
    # dpi = img.info['dpi']
    dpi = 100
    width_in_mm = round((img_width / dpi) * 25.4)
    height_in_mm = round((img_height / dpi) * 25.4)
    center_x = (page_width - width_in_mm) / 2
    center_y = (page_height - height_in_mm) / 2
    return center_x, center_y, width_in_mm, height_in_mm

def generate_pdf(pdf, img):

    center_x, center_y, width_in_mm, height_in_mm = center_image(pdf, img)
    pdf.add_page()
    name = input("Name: ")
    pdf.image("shirtificate.png", x = center_x, y = center_y, w = width_in_mm, h = height_in_mm)
    pdf.set_margin(margin = 0)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", size=22)
    pdf.cell(text=f"{name} took CS50", border=0, center = True)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()

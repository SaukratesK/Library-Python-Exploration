from fpdf import FPDF




def main():
    pdf = FPDF(format='A4', unit='mm')
    pdf.add_page()
    pdf.set_font('Times','',10.0)
    pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")

    left = pdf.l_margin
    right = pdf.r_margin
    top = pdf.t_margin
    bottom = pdf.b_margin
    print(left)
    print(right)
    print(top)
    print(bottom)

    # Effective page width and height
    epw = pdf.w - left - right
    eph = pdf.h - top - bottom
     
    # Draw margins for our viewing pleasure
    pdf.rect(left, top, w=epw, h=eph)

    pdf.ln(0.15)

    pdf.set_draw_color(0, 255, 0) #vert
    pdf.line(20, 20, 20, 200)
    pdf.set_draw_color(0, 0, 255) #blue
    pdf.line(30, 30, 30, 200)


    
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0) #rouge
    pdf.line(20, 20, 150, 20)


    pdf.set_fill_color(255, 255, 0)
    pdf.set_line_width(0.2)
    pdf.set_draw_color(0, 0, 255) #blue
    pdf.ellipse(50, 50, 50, 50, 'D')
    pdf.rect(15, 15, 50, 50, 'F')






    pdf.output("simple_demo.pdf")









if __name__ == '__main__':
    main()

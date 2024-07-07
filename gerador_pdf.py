from fpdf import FPDF
import os

#Arquivo de teste da biblioteca
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, "Hello World!")
pdf.output('dados/teste.pdf')
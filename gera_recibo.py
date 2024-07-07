from fpdf import FPDF
from num2words import num2words
from datetime import date
#Variáveis
cliente = input("Digite o nome do cliente\n")
consulta = input("Digite o tipo de consulta\n")
valor = input("Digite o valor da consulta\n")
valor_msg = f"{valor} reais"
valor_extenso = num2words(float(valor), lang='pt-br')
valor_reais = f"{valor_extenso} reais"
data = date.today()
dd = data.day
mm = data.month
yy = data.year

#Layout do Recibo

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', "", 20)

page_width = pdf.w
page_height = pdf.h
pdf.image("dados/rec.jpg", x=0, y=0, w=page_width, h=page_height)

#Textos e dimensões
pdf.text(162, 46, valor_msg)
pdf.text(80, 86, cliente)
pdf.text(80, 111, valor_reais)
pdf.text(80, 139, consulta)
pdf.set_text_color(255, 255, 255)
#datas
pdf.text(30,195, str(dd))
pdf.text(50, 195, str(mm))
pdf.text(70, 195,str(yy))
nome_arquivo = f"{cliente.strip()}_{dd}_{mm}_{yy})"

pdf.output("recibo.pdf")
print("Recibo gerado com sucesso")
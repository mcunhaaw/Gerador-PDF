Este projeto tem como objetivo criar um gerador de recibos automatizado para a psicóloga fictícia Karina Vilela, utilizando Python. 

![Descrição da Imagem](https://onebitcode.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff04298a7-bf43-4bf0-baf7-b90a9d340e03%2Frec.jpg?table=block&id=f6553a41-e0c9-47d0-b1c5-f44d463441c0&spaceId=6e5271d8-2f68-42f5-aa75-5978bbff47fa&width=600&userId=&cache=v2)

As bibliotecas usadas são:

- **FPDF**: para a criação e manipulação de arquivos PDF.
- **num2words**: para converter valores numéricos em palavras.
- **date**: para manipulação de datas.

## Requisitos

Para executar o código, é necessário ter as seguintes bibliotecas instaladas:

- `fpdf`
- `num2words`

Você pode instalar essas bibliotecas utilizando o `pip`:

```bash
pip install fpdf num2words
```

## Uso

Este script Python permite gerar recibos personalizados em formato PDF para a psicóloga fictícia Karina Vilela. O processo envolve a coleta de informações do cliente, conversão do valor da consulta para extenso e formatação da data atual.

### Passo 1: Coleta de Dados do Cliente

Execute o script. Será solicitado que você forneça algumas informações:

```python
cliente = input("Digite o nome do cliente\n")
consulta = input("Digite o tipo de consulta\n")
valor = input("Digite o valor da consulta\n")
```
### Conversão e Formatação dos Dados

Convertendo o valor da consulta para palavras e formatando a data atual:

```python
valor_msg = f"{valor} reais"
valor_extenso = num2words(float(valor), lang='pt-br')
valor_reais = f"{valor_extenso} reais"
data = date.today()
dd = data.day
mm = data.month
yy = data.year
```
### Criação do Layout do Recibo

Configurando o layout do recibo, incluindo uma imagem de fundo:

```python
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', "", 20)

page_width = pdf.w
page_height = pdf.h
pdf.image("dados/rec.jpg", x=0, y=0, w=page_width, h=page_height)
```
### Criação do Layout do Recibo

Configurando o layout do recibo, incluindo uma imagem de fundo:

```python
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', "", 20)

page_width = pdf.w
page_height = pdf.h
pdf.image("dados/rec.jpg", x=0, y=0, w=page_width, h=page_height)
```
### Inserção dos Textos e Datas no PDF

Adicionando os textos e datas no PDF, posicionando-os adequadamente:

```python
pdf.text(162, 46, valor_msg)
pdf.text(80, 86, cliente)
pdf.text(80, 111, valor_reais)
pdf.text(80, 139, consulta)
pdf.set_text_color(255, 255, 255)

pdf.text(30, 195, str(dd))
pdf.text(50, 195, str(mm))
pdf.text(70, 195, str(yy))
```
### Geração e Salvamento do Arquivo PDF

Salvando o arquivo PDF com um nome baseado no nome do cliente e na data atual:

```python
nome_arquivo = f"{cliente.strip()}_{dd}_{mm}_{yy}.pdf"
pdf.output(nome_arquivo)
print("Recibo gerado com sucesso")
```
## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

import PyPDF2
import os
import re
def extract_factura_info(pdf_file_path):
    #abrir el archivo pdf
    with open(pdf_file_path,'rb')as file:
        #crear pdf obejtos de lectura
        pdf_reader= PyPDF2.PdfReader(file)
        #extraer texto de cada pagina
        text=''
        
        for page_num in range(len(pdf_reader.pages)):
            page=pdf_reader.pages[page_num]
            text+=page.extract_text()
        #expresiones regulares
        ex_numero_factura= r'F\d{3}-\d{6}'
        #extraer información de expresiones regulares
        info_numero_factura_match=re.search(ex_numero_factura,text)
        #extraer información
        numero_factura=info_numero_factura_match.group() if info_numero_factura_match else None
        print("el número de factura es: "+numero_factura)


extract_factura_info("facturas/factura01.pdf")

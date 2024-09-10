from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors 
  
#pip install reportlab
class GeneradorPDF:
    def generar_fila_item(self, item):
        return f'{item.numero_unidades} de {item.nombre} a {item.precio_unitario} la unidad: {item.importe}€ '

    def generar(self, factura):
        print(f"Generando PDF para la factura {factura.nombre_cliente}. Importe total: {factura.get_importe_con_reduce()}")

        fileName = f'{factura.nombre_cliente}.pdf'
        documentTitle = 'sample'
        title = 'Sekurytas Dyrect'
        subTitle = 'Factura'
        client = factura.nombre_cliente
        #textLines = [ 
        #    str(factura.get_importe_con_reduce()), 
        #]
        # textLines = [item.nombre for item in factura.items] 
        # textLines = [f'{item.numero_unidades} de {item.nombre}' for item in factura.items]
        # textLines = [item.get_fila_factura() for item in factura.items]
        #textLines = [self.generar_fila_item(item) for item in factura.items]
        textLines = [str(item) for item in factura.items] 

        # creating a pdf object 
        pdf = canvas.Canvas(fileName) 
        
        # setting the title of the document 
        pdf.setTitle(documentTitle) 
        
        
        
        # creating the title by setting it's font  
        # and putting it on the canvas 
        #pdf.setFont('abc', 36) 
        pdf.drawCentredString(300, 770, title) 

        pdf.drawCentredString(290, 740, client) 
        
        # creating the subtitle by setting it's font,  
        # colour and putting it on the canvas 
        pdf.setFillColorRGB(0, 0, 255) 
        pdf.setFont("Courier-Bold", 24) 
        pdf.drawCentredString(290, 720, subTitle) 
        
        # drawing a line 
        pdf.line(30, 710, 550, 710) 
        
        # creating a multiline text using  
        # textline and for loop 
        text = pdf.beginText(40, 680) 
        text.setFont("Courier", 18) 
        text.setFillColor(colors.red) 
        for line in textLines: 
            text.textLine(line) 
        pdf.drawText(text) 
        
        # saving the pdf 
        pdf.save() 
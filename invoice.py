from reportlab.pdfgen import canvas

c = canvas.Canvas("invoice.pdf", pagesize=(200, 250), bottomup=0)

c.translate(10,40)
c.scale(1,-1)
c.drawImage("logo.jpg", 0, 0, width=50, height=30)
c.scale(1,-1)
c.translate(-10,-40)
c.setFont("Helvetica-Bold", 10)
c.drawCentredString(125, 20, "Elabs Tech")

c.line(70, 22, 180, 22)
c.setFont("Helvetica-Bold", 5)
c.drawCentredString(125, 30, "Ntinda-Kulambiro")
c.drawCentredString(125, 35, "Kampala, Uganda")

c.setFont("Helvetica-Bold", 6)
c.drawCentredString(125, 42, "GSTIN : 0753237823")

c.line(5, 45, 195, 45)
c.setFont("Courier-Bold", 8)
c.drawCentredString(100, 55, "INVOICE")
c.roundRect(15, 63, 170, 40, 10, stroke=1, fill=0)

c.setFont("Times-Bold", 5)
c.drawRightString(70,70,"INVOICE No.: ")
c.drawString(70, 80, "Date: ")
c.drawString(70, 90, "CUSTOMER NAME: ")
c.drawString(70, 100, "PHONE No.")

c.roundRect(15, 108, 170, 130, 10, stroke=1, fill=0)
c.line(15, 120, 185, 120)
c.drawCentredString(25, 118, "SR No.")
c.drawCentredString(75, 118, "GOODS DECRIPTION")
c.drawCentredString(125, 118, "RATE")
c.drawCentredString(148, 118, "QTY")
c.drawCentredString(173, 118, "TOTAL")

c.line(15, 120, 185, 210)
c.line(35, 108, 35, 220)
c.line(115, 108, 115, 220)
c.line(135, 108, 135, 220)
c.line(160, 108, 160, 220)

c.line(15, 220, 185, 220)
c.line(100, 220, 100, 238)
c.drawString(20, 225, "We declare that the above mentioned")
c.drawString(20, 230, "information is true")
c.drawString(20, 235, "(This is a system generated invoice)")
c.drawRightString(180, 235, "Authorised Signatory")

c.showPage()
c.save

# Libraries: reportlab

# Concepts: Creating and formatting PDF documents, adding text and images to PDFs.



from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf():
    # Create a canvas object
    c = canvas.Canvas("script.pdf", pagesize=letter)
    
    # Draw a string at (100, 750) on the canvas
    c.drawString(100, 750, "Hariom Singh")
    
    # Save the canvas, which finalizes the PDF file
    c.save()

# Call the function to create the PDF
create_pdf()

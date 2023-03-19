# Importing Required Module
from os import read
import img2pdf
# Creating Image File Object
ImgFile = open("C:\\Users\\user\\Desktop\\fss logo.png",r)
# Creating PDF File Object
PdfFile = open("test1.pdf","wb")
# Converting Image File to PDF
PdfFile.write(img2pdf.convert(ImgFile))
#Closing Image File Object
ImgFile.close()
#Closing PDF File Object
PdfFile.close()
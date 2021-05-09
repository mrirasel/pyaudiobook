import pyttsx3
import PyPDF2
book = open('oop.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
rasel = pyttsx3.init()
for num in range(7,pages):
    page = pdfReader.getPage(num)
    text =page.extractText()
    rasel.say(text)
    rasel.runAndWait()

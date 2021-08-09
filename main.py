import easygui
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileWriter, PdfFileReader
import PyPDF2
import re
from tkinter import messagebox
from tkinter import Text
import os
import calendar;
import time
from config import configs
import base64
from datetime import datetime

def checkPath(dir):
    if os.path.isdir(dir):
        print()
    else:
        os.mkdir(dir)
def subPath(dir):
    if '\\' in dir:
        return '\\'
    elif '/' in dir:
        return '/'
try:
    filename = ""
    Tk().withdraw()
    filename = askopenfilename()
    if(filename[-3:] == "pdf"):
        inputpdf = PdfFileReader(open(filename, "rb"))
        ts = calendar.timegm(time.gmtime())
        passwd = configs.PASSWD
        passwd = passwd.replace("x", "M")
        passwd = passwd.replace("AA", "ZD")
        passwd = passwd.replace("y", "N") 
        passwd = passwd[:-1]
        passwd = base64.b64decode(passwd)
        text = "Enter the password to enter GeeksforGeeks"
        title = "Window Title GfG"
        output = easygui.passwordbox(text, title)
        if(passwd.decode('UTF-8') == base64.b64encode(output.encode("utf-8"))):
            workpath = configs.PATH + str(ts)
            checkPath(workpath)
            for i in range(inputpdf.numPages):
                output = PdfFileWriter()
                output.addPage(inputpdf.getPage(i))
                with open(workpath + subPath(workpath) + "%s.pdf" % i, "wb") as outputStream:
                    output.write(outputStream)      
            f = open(workpath + subPath(workpath) + "0.txt","w+")
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            f.write(dt_string)
            f.close() 
            messagebox.showinfo("doMestre_Folha", "Arquivo foi separado, iniciando processamento...")
            pdf_file = open('/home/cleiton/Documents/pdf-a.pdf', 'rb')
            read_pdf = PyPDF2.PdfFileReader(pdf_file)
            number_of_pages = read_pdf.getNumPages()
            page = read_pdf.getPage(0)
            page_content = page.extractText()
            parsed = ''.join(page_content)
            print("Sem eliminar as quebras")
            print(parsed)
            parsed = re.sub('n', '', parsed)
            print("Após eliminar as quebras")
            print(parsed)
        else:
           messagebox.showinfo("doMestre_Folha", "Erro. Senha incorreta") 
    else:
        messagebox.showinfo("doMestre_Folha", "Erro. Selecione um arquivo PDF")
except:
    messagebox.showinfo("doMestre_Folha", "Erro ao selecionar arquivo.")
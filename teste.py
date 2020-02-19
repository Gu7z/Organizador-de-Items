import os.path
from os import path
import os
import datetime
from shutil import copyfile

d = datetime.datetime.today()

filesPath = "C:\\Users\\Public\\Documentos"

print('>>>>>>>>><<<<<<<<<')
print('-----SCRIPNIK-----')
print('>>>>>>>>><<<<<<<<<')

oldornew = input('Documento 1)Antigo ou 2)Novo? \n Resp: ')
userResponse = input('Qual o tipo de arquivo? \n 1)Ata \n 2)Circular Interna \n 3)Carta Comercial \n Res: ')
documentNumber = input('Qual o titulo/numero do documento? \n Res: ')

def rename():
    contador = 1
    paaath = "C:\\Users\\Gustavo\\Desktop\\opora\\"
    for file in os.listdir(paaath):
        filetype = file.split('.')
        if not filetype[1] == 'exe':
            os.rename(file, '{}.{}'.format(contador, filetype[1]))
            contador += 1

def atas():
    contador = 0
    if not path.isdir(atafiles):
        os.system('mkdir {}'.format(atafiles))
    else:
        for file in os.listdir(atafiles):
            contador += 1
	
    for file in os.listdir('.'):
        filetype = file.split('.')
        if not filetype[1] == 'exe':
            new_name = 'Ata {} - Arquivo {}.{}'.format(documentNumber, contador, filetype[1])
            os.rename(file, '{}'.format(new_name))
            contador += 1
            
    for file in os.listdir('.'):
        filetype = file.split('.')
        if not filetype[1] == 'exe':
            os.system('move "{}" {}'.format(file, atafiles))
            
def circ():
    contador = 0
    if not path.isdir(circular):
        os.system('mkdir {}'.format(circular))
    else:
        for file in os.listdir(circular):
            contador += 1
	
    for file in os.listdir('.'):
        filetype = file.split('.')
        if not filetype[1] == 'exe':
            new_name = 'Circular-Interna {} - Arquivo {}.{}'.format(documentNumber, contador, filetype[1])
            os.rename(file, '{}'.format(new_name))
            contador += 1
            
    for file in os.listdir('.'):
        filetype = file.split('.')
        if not filetype[1] == 'exe':
            os.system('move "{}" {}'.format(file, circular))
            
	
def carta():
    contador = 0
    if not path.isdir(cartafile):
        os.system('mkdir {}'.format(cartafile))
    else:
        for file in os.listdir(cartafile):
            contador += 1
	
    for file in os.listdir('.'):
        filetype = file.split('.')
        if not filetype[1] == 'exe':
            new_name = 'Carta-Comercial {} - Arquivo {}.{}'.format(documentNumber, contador, filetype[1])
            os.rename(file, '{}'.format(new_name))
            contador += 1
            
    for file in os.listdir('.'):
        filetype = file.split('.')
        if not filetype[1] == 'exe':
            os.system('move "{}" {}'.format(file, cartafile))
            
	
def makeFiles():
        
    if int(userResponse) == 1:
        if(path.isdir('\\Atas'.format(filesPath))):
            atas()
        else:       
            os.system('mkdir {}\\Atas'.format(filesPath))
            atas()
            
    elif int(userResponse) == 2:
        
        if(path.isdir('{}\\Circular-Interna'.format(filesPath))):
            circ()
        else:       
            os.system('mkdir {}\\Circular-Interna'.format(filesPath))
            circ()
            
    elif int(userResponse) == 3:
        
        if(path.isdir('{}\\Carta-Comercial'.format(filesPath))):
            carta()
        else:       
            os.system('mkdir {}\\Circular-Interna'.format(filesPath))
            carta()
            
    else:
        print('No response')

if path.isdir(filesPath) :
    if int(oldornew) == 1:
        month = input('Digite o mes. Ex: Jan = 01, Fev = 02\n Resp: ')
        year = input('Digite o Ano. Ex: 2020, 2019, 1991\n Resp: ')
        date = "{}-{}".format(month, year)
        atafiles  = "C:\\Users\\Public\\Documentos\\Atas\\{}".format(date)
        circular  = "C:\\Users\\Public\\Documentos\\Circular-Interna\\{}".format(date)
        cartafile = "C:\\Users\\Public\\Documentos\\Carta-Comercial\\{}".format(date)
        makeFiles()
    elif int(oldornew) == 2:
        date = d.strftime('%m-%Y')
        atafiles  = "C:\\Users\\Public\\Documentos\\Atas\\{}".format(date)
        circular  = "C:\\Users\\Public\\Documentos\\Circular-Interna\\{}".format(date)
        cartafile = "C:\\Users\\Public\\Documentos\\Carta-Comercial\\{}".format(date)
        makeFiles()
else:
    os.system('mkdir {}'.format(filesPath))
    makeFiles()

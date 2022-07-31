from ftplib import FTP
import logging

HOST = 'localhost'
PORT = 2121

name = input()

try:
     handler = FTP()
     handler.connect(ip, port)
     handler.login(login, password)
        
except Exception:
     logging.critical('Não foi possivel conectar ao servidor FTP')
    
ftp.retrlines('LIST', callback=log.append)
    files = (line.rsplit(None, 1)[1] for line in log)
    print 'Arquivos: \n'
    for f in list(files):
        print f

Dfile = open('PastaExemplo/Downloads/' + name, 'wb')
try:
        handler.retrbinary('RETR ' + filename, Dfile.write)
except Exception, e:
      
    print 'Erro ao abaixar o arquivo '
    raise e
     
print 'Download feito com sucesso! :)'
    
Dfile.close()

try:
     handler.cwd(Dir)
except Exception:
     print 'Não foi possivel acessar o diretorio ou o diretorio não existe'
    
try:
     handler.delete(name)
except Exception:
     print ' não foi possivel deletar o arquivo ou ele é inexistente'
print 'O arquivo foi deletado'

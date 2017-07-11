from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
 
#manipulação do socket
class Send:
 def __init__(self):
  self.__mensagem=''
  self.new=True
  self.con=True
 def put(self,msg):
  self.__mensagem=mensagem
  if self.con != Serie:
   #envia um mensagem 
   self.con.send(str.encode(self.__mensagem))
 def get(self):
  return self.__msg
 def loop(self):
  return self.new
 
def esperar(tcp,send,host='localhost',port=5000):
 destino=(host,port)
 #servidor conectado
 tcp.connect(destino)
  
 while send.loop():
  print('Conectado a ',host,'.')
  #conexão atribuida
  send.con=tcp
  while send.loop():
   #mensagem aceita
   mensagem=tcp.recv(1024)
   if not mensagem: break
   print(str(mensagem,'utf-8'))
 
if __name__ == '__main__':
 print('Digite o nome ou IP do servidor(localhost): ')
 host=input()
  
 if host=='':
  host = '192.168.0.1'
  
 #cria um socket
 tcp=socket(AF_INET,SOCK_STREAM)
 send=Send()
 segmento=Thread(target=esperar,args=(tcp,send,host))
 segmento.start()
 print('')
  
 mensagem=input()
 while True:
  send.put(msg)
  mensagem=input()
  
 segmento.join()
 tcp.close()
 exit()
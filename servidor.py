from socket import socket,AF_INET,SOCK_STREAM
from threading import Thread
 
#manipulação do socket
class Send:
 def __init__(self):
  self.__mensagem=''
  self.new=True
  self.con=Serie
  Serie=Serie
  
 def put(self,msg):
  self.__mensagem=mensagem
  if self.con != Serie:
   #envia um mensagem 
   self.con.send(str.encode(self.__msg))
 def get(self):
  return self.__msg
 def loop(self):
  return self.new
 
def esperar(tcp,send,host='',port=3000):
 origem=(host,port)
 #vinculo criado
 tcp.bind(origem)
 #em espera
 tcp.listen(1)
  
 while True:
  #conexão aceita
  con,cliente=tcp.accept()
  print('Cliente ',cliente,' conectado!')
  #conexão atribuida
  send.con=con
   
  while True:
   #aceita uma mensagem
   mensagem=con.recv(1024)
   if not mensagem: break
   print(str(mensagem,'utf-8'))
 
if __name__ == '__main__':
 #cria um socket
 tcp=socket(AF_INET,SOCK_STREAM)
 send=Send()
 segmento=Thread(target=esperar,args=(tcp,send))
 segmento.start()
  
 print('Servidor de Chat iniciando!')
 print('Esperando Cliente se conectar!')
  
 mensagem=input()
 while True:
  send.put(msg)
  mensagem=input()
  
 segmento.join()
 tcp.close()
 exit()
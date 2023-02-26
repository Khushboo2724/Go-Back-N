import types,sys,time
import socket
from socket import AF_INET, SOCK_STREAM
host,port=sys.argv[1],int(sys.argv[2])
s=socket.socket(AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
ack=0
t=0.25
recv_final=[]
while True:
	try:
		data=s.recv(1024)
	except:
		print("not recieved till now")
		continue
	if not data:
		break
	elif data.decode()=="-1":
		print("all the frames are succesfully recieved")
		break
	else:
		data=data.decode()
		print(data)
		print("here1")
		if data[0:9]==str(ack):
			print("went here2 in if")
			recv_final.append(data)
			ack=ack+1
			print(ack)
			ack1=ack.to_bytes(8,'big')
			s.send(ack1)
		else:
			time.sleep(t)
			#while True:
				#try:
			s.send(ack.to_bytes(2,'big'))
				#except:
					#print("in else trying to send")
					#continue
				#else:
					#print("done")
					#break

import types,sys,time
import socket
from socket import AF_INET, SOCK_STREAM

m=int(input("enter the value of size of sequence number field in bits i.e m"))
Sm=(2**m)-1
print(Sm)
Sn=0
Sf=0
t=0.25 #choosed this time coz the quickest search on google less than 0.2 sec,so adjusted with it
data=b"0this data is been sent to my own device using a Go-Back_N protocol with max throughput of more than 60%"
buffer_store=[]
host,port=sys.argv[1],int(sys.argv[2])
s=socket.socket(AF_INET,socket.SOCK_STREAM)
s.bind((host,port))

while True:
    s.listen()
    conn,addr=s.accept()

    with conn:
        print(f"Connected by {addr}")

    #send when data is ready
    #if got the packet to wnd\

        if(Sn-Sf>=Sm):
                #sleep
                time.sleep(t)

        else:
            
            ack_no=0
            #get data from the message u want to send fragmented from given sample
            #d=sys.getsizeof(data)/7
            data_new=data
            while len(data)!=0 :
            #make fragment of it and store it in the list so that easy to pop whenever an ack received or even easy to send dynamic
                buffer_store.append(data_new[0:7])
                ack_no=ack_no+1
                ack1=ack_no.to_bytes(8,'big')
                print("in appending mode")
                data=data.replace(data[0:7],b'')
                data_new=data.replace(data[0:7],ack1)
                print(ack_no)
                print(data_new)
                

            buffer_store.append(b'-1')
            print("appending end ack no")
                

        #send it
        next=0
        while next!=len(buffer_store):
            while Sm!=0:
                print(buffer_store[next])
                conn.send(buffer_store[next])
                print(next)
                next=next+1
                print(next)
                Sm=Sm-1
                print(Sm)
                #inc the Sn++
                Sn=Sn+1
                print(Sn)
                time.sleep(t)#timer not running set timer on
                print("slept")
                data1=conn.recv(1024)
                
                while data1!=0: #recieved something
                    print("recieved something")
                    #data1=conn.recv(1024)
                    print("recieved")
                    data1=data1.decode()
                    #data1=(data1)
                    print("hdihw")
                    print(type(data1))
                    print(len(data1))
                    print(data1)

                    if data1==str(next):
                        Sf=Sf+1
                        print("gefkh")
                        print(Sf)
                        buffer_store.pop(0)
                        
                    elif data1>str(next):
                        print("jlojp")
                        next=data1
                        print(next)
                        Sf=data1
                        print(Sf)
                        

            Sm=(2**m)-1
            next=0
            Sn=0
                
            #run a while loop till timer doesnt go off to recieve the ack
        
            #once ack received decode it and check the ack numb cumulative
            #if ack is corrupted sleep

            #else correct remove the fragment from list inc Sn++

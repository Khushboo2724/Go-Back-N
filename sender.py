import socket,types,sys,time
m=int(input("enter the value of size of sequence number field in bits i.e m"))
Sm=(2**m)-1
print(Sm)
Sn=0
Sf=0
t=0.25 #choosed this time coz the quickest search on google less than 0.2 sec,so adjusted with it
data=b"this data is been sent to my own device using a Go-Back_N protocol with max throughput of more than 60%"
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
        s=0,e=7
        #get data from the message u want to send fragmented from given sample
        #d=sys.getsizeof(data)/7
        while sys.getsizeof(data)!=0 :
        #make fragment of it and store it in the list so that easy to pop whenever an ack received or even easy to send dynamic
        buffer_store.append(data[s:e])
        data=data.replace(data[s:e],b"")
        

    #send it
    next=0
    while next!=len(buffer_store):
        while Sm!=0:

            conn.send(buffer_store[next])
            next=++
            Sm--
            #inc the Sn++
            Sn++
            time.sleep(t):#timer not running set timer on
            
            if conn.recv()!=0: #recieved something
                data=conn.recv()
                data=data.decode()
                if data==next:
                    Sn++
                    buffer_store.pop(0)
                    break
                else data<next:
                    break
                


            else:
                break
            
        #run a while loop till timer doesnt go off to recieve the ack
    
        #once ack received decode it and check the ack numb cumulative
        #if ack is corrupted sleep
        #else correct remove the fragment from list inc Sn++
# Python Client 
#connect to server at port 12345
import socket 
from time import gmtime, strftime , sleep
import pickle # to convert list to string
import random



port = int(raw_input("please enter port number  :"))
input_list = ['','','','','']#save empty list size 5
input_list[0] = raw_input("please enter id station  :")
input_list[1] = raw_input("please enter name  :")
#port = 12345
host = ''
BUFFER_SIZE = 2048

try:
	client = socket.socket() 
	client.connect((host, port))
except socket.error as e:
	print e
	
while True:	
	data = client.recv(BUFFER_SIZE) # WAIT UNTIL GET "KEEP ALIVE " FROM SERVER
	if data:
		input_list[2] = strftime("%Y-%m-%d %H:%M:%S", gmtime())#get current time
		input_list[3] = (random.choice(open("data.txt").readline()).strip('\n'))#choose random row data from data.txt(1 or 0)
		input_list[4] = (random.choice(open("data.txt").readline()).strip('\n'))
		print input_list
		client.send(str(pickle.dumps(input_list)))     #convert list to string
	input_list[2] = ''  #clear time & alarm & wather for next interval
	input_list[3] = ''
	input_list[4] = ''
	
	
client.close()
    
 
 

import socket 
import threading
import sqlite3
from time import * #set 10 second sleep
import sys #exit
import pickle #for send data with socket
import random #make random text file for clients

class ClientThread(threading.Thread):
	
    def __init__(self,ip,port,conn): #init thread
        threading.Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.conn = conn
        print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
    def run(self): #start thread function
		self.conn.send("Welcome to the server\n\n")
		
		while True : 
			
			self.conn.send("keep alive message!!!!!!")
			threadLock.acquire()# Lock To Synchronize The Threads
			data = pickle.loads(conn.recv(2048)) #convert message string to list
			sleep(1)
			if data != "":
				
				print "ok" ##for ckecking...
				self.DataBaseHendler(data)			   
			else:#data received is empty string
				print("data is empty string. diconnecting....") 
				sys.exit(0) #terminates thread
			threadLock.release()	# Unlock To Release The Next Thread	  
			sleep(20)	
		
	        		
			
			 
    def DataBaseHendler(self,data):

		try:
			try:
				con=sqlite3.connect('station.db') #establish connection to database
				cur = con.cursor()
			except Error as e:
				print (e)
				sys.exit(0) #if no connection to data base

		except IOError as e:
			print("I/O error ({0}): {1}".format(e.errno, e.strerror))
		print("\n\n")

		#sql job:
		cur.execute("INSERT OR REPLACE INTO status VALUES(?, ?, ?, ?, ?) ", (data[0], data[1], data[2], data[3], data[4]))
		con.commit()
		
		#printing status table data to valid correct input
		print("status data table : ")
		cur.execute("SELECT * FROM status")
		rows = cur.fetchall()
		con.commit()
		for row in rows:
			print str(row)

		con.close()
			

	

		
		        
            
            
if __name__ == '__main__':

#create text file with random data for the clients.	   
    
	with open("data.txt","wb") as f:
		for i in range (0,10):
			line_data = str(random.randint(0,1))
			f.write(line_data) 

#clear data from status rows table to start new table info.
	con=sqlite3.connect('station.db')
	cur=con.cursor()
	cur.execute("DELETE FROM status")
	con.commit()
	con.close()

# Multithreaded Python server :
	threadLock = threading.Lock()
	PORT = 12345   
	Server = socket.socket() 
	Server.bind(('',PORT))
	Server.listen(5) 
	threads = [] 
	
 
	
	while True: 
		
		print "Multithreaded Python server : Waiting for connections from  clients..." 
		(conn, (ip,port)) = Server.accept() 
		newthread = ClientThread(ip,port,conn)
		newthread.start() #start from run(self) function
		threads.append(newthread) 
		'''
			while True:
				for t in threads:
					if not t.isAlive():
						threads.remove(t)
						
				sleep(60)
		'''
	
		
	

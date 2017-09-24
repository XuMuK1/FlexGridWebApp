##########

import time
from flask import Flask, jsonify
from multiprocessing import Process, Value


app = Flask(__name__)







#################

from flask import Flask, render_template,json, request, jsonify
import random	
from flask.ext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
 

# MySQL configurations
print("MYSQL is turned off")


'''
app.config['MYSQL_DATABASE_USER'] = 'xumuk'
app.config['MYSQL_DATABASE_PASSWORD'] = 'C6h0e2m2istry'
app.config['MYSQL_DATABASE_DB'] = 'FlexGridDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn= mysql.connect()
cursor = conn.cursor()
'''

##INIT BLUETOOTH
print("Bluetooth module is turned off")

#import bluetooth
''' print("Searching for devices...")
print ("")
nearby_devices = bluetooth.discover_devices()
num = 0
print("Select your device by entering its coresponding number...")
for i in nearby_devices:
	num+=1
	print( num , ": " , bluetooth.lookup_name( i ))

selection = int(input("> ")) - 1
print("You have selected", bluetooth.lookup_name(nearby_devices[selection]))
bd_addr = nearby_devices[selection]

port = 1

'''

####


import atexit

@app.route("/",methods=['GET','POST'])
def main():
	if(request.method == 'POST'):
		reqjs = request.get_json()
		print("POST received: "+str(reqjs))
		
		if(reqjs['command'] == "UpdateArduino"):				
			return UpdateDataFromArduino()
			#return "Respond on request to updateArduino"

	else:
		print("I am updating the info from DB!! (/main.GET)")
    		#sql = "SELECT * from houses;"
    		#cursor.execute(sql)
    		#queryResult = cursor.fetchall()
		queryResult=[[1,"Future, Innovation str., 1",200],
			[2,"Future, Innovation str., 2",100],
			[3,"Future, Innovation str., 3",170]]#until I connect the DB
		return render_template('index.html', data=queryResult)

##BLUETOOTH MODULE

def UpdateDataFromArduino():
	'''BLUETOOTH IS TURNED OFF
	k=0
	toAnalyze=b""
	print("connecting...")
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((bd_addr, port))
	print("connected")

	while(k<=200):
		k=k+1
		data = sock.recv(1)
		toAnalyze=toAnalyze+data
		
	
	toAnalyze=str(toAnalyze.decode("utf-8"))
	toAnalyze=toAnalyze.split("##")[1]
	toAnalyze=toAnalyze.split(',')
	print(toAnalyze)
	print("parsed2!!")
	
	sock.close()'''

	toAnalyze=[str(random.randint(1,9))]*12#temporary
	print("Uploading observations to DB and sending response to web-page")

	return ",".join(toAnalyze)

#####


if __name__ == "__main__":
    app.run()
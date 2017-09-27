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
print("MYSQL is turned on")



app.config['MYSQL_DATABASE_USER'] = 'xumuk'
app.config['MYSQL_DATABASE_PASSWORD'] = 'C6h0e2m2istry'
app.config['MYSQL_DATABASE_DB'] = 'FlexGridDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn= mysql.connect()
cursor = conn.cursor()


##INIT BLUETOOTH
print("Bluetooth module is turned off")
'''
import bluetooth
print("Searching for devices...")
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
print("connecting...")
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

print("connected")

'''



####
houses =[]  #on/off

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
			if(reqjs['command'] == "SwitchHouse"):
				print(reqjs['id'])
				return SwitchHouse(reqjs['id'])
			else:
				if(reqjs['command'] == "UpdateHouses"):
					return json.dumps(houses)					
					
	else:
		print("I am updating the info from DB!! (/main.GET)")
		sql = "SELECT houseId, address from houses;"
		cursor.execute(sql)
		queryResult = cursor.fetchall()
		sql = "SELECT OnOff from houses;"
		cursor.execute(sql)
		#queryResult=[[1,"Future, Innovation str., 1"],
		#	[2,"Future, Innovation str., 2"],
		#	[3,"Future, Innovation str., 3"]]#until I connect the DB
		global houses
		
		houses=[k for k in cursor.fetchall()]
		# all is on
		print("HOUSES!!!"+str(houses))
		return render_template('index.html', data=queryResult)

def SwitchHouse(houseId):
	global houses
	print("HOUSES"+str(houses))
	houses[houseId]=not houses[houseId]
	print("Switching house"+str(houseId))
	if(houses[houseId]):
		print("...ON!")
		sql="UPDATE houses SET OnOff = TRUE WHERE houseId="+str(houseId+1)
		cursor.execute(sql)
		conn.commit()
		return "On"
	else:
		print("...OFF!")
		sql="UPDATE houses SET OnOff = FALSE WHERE houseId="+str(houseId+1)
		cursor.execute(sql)
		conn.commit()
		return "Off"

def MakeBlackout():
	global houses
	for i in range(0,len(houses)):  
		houses[i]=False
	sql="UPDATE houses set OnOff = False;"

	
##BLUETOOTH MODULE

respond = [{"timestamps":[z for z in range(0,10)],
		    "innerConsumption":[random.uniform(0,1) for i in range(0,10)],
		    "energyImport":[random.uniform(0,1) for i in range(0,10)],
		    "budget":[random.uniform(0,1) for i in range(0,10)],
		    "energyExport":[random.uniform(0,1) for i in range(0,10)]} for k in range(0,3)]

def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]
	
def UpdateDataFromArduino():
	#BLUETOOTH IS TURNED OFF
	
	k=0   
	'''
	toAnalyze=b""
	

	while(k<=20):
		try:
			k=k+1
			data = sock.recv(10)
			toAnalyze=toAnalyze+data
		except:
			global sock
			for i in range(0,3):
				print("Reconnect attempt "+str(i))
				sock.close()
				try:
					sock.connect((bd_addr, port))
				except:
					if(i==2):
						print("SORRY, it is not possible")
			

		
	print(toAnalyze)
	toAnalyze=str(toAnalyze.decode("utf-8"))
	toAnalyze=toAnalyze.split("##")[1]
	toAnalyze=toAnalyze.split(',')
	#print(toAnalyze)
	#print("parsed2!!")
	toAnalyze=[int(toAnalyze[k])/1023*5 for k in range(0,len(toAnalyze))]
	'''
	
	#fixed price(yet)
	price=2   

	inConsNorm=0.01*500*0.8 #normalization constants
	importNorm=1/68*2000
	exportNorm=0.1*25
	print("Calculating")
	for i in range(0,3):
		respond[i]["innerConsumption"]=shift(respond[i]["innerConsumption"],1)		
		respond[i]["energyImport"]=shift(respond[i]["energyImport"],1) #both for import/export
		respond[i]["budget"]=shift(respond[i]["budget"],1)
		respond[i]["energyExport"]=shift(respond[i]["energyExport"],1)
	
		#Bluetooth is turned OFF
		'''respond[i]["innerConsumption"][len(respond[i]["innerConsumption"])-1]=(toAnalyze[4*i+2]-toAnalyze[4*i+1])*(toAnalyze[4*i+2])*inConsNorm
		respond[i]["energyImport"][len(respond[i]["energyImport"])-1]=(toAnalyze[4*i]-toAnalyze[4*i+2])**2 * importNorm
		respond[i]["energyExport"][len(respond[i]["energyExport"])-1]=(5-toAnalyze[4*i+3])**2 * exportNorm
		respond[i]["budget"][len(respond[i]["budget"])-1]=respond[i]["energyImport"][len(respond[i]["energyImport"])-1]*price    '''
		
	
	#toAnalyze=[str(random.randint(1,9))]*12#temporary
	print("Uploading observations to DB and sending response to web-page")

	return json.dumps(respond)

#####


if __name__ == "__main__":
    app.run()
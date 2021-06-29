# atm_sensor_get.py
import requests
import datetime
import html
now = datetime.datetime.now()
date_stamp = now.strftime("%Y-%b-%d %H:%M")
r = requests.get("https://app.alphax.cloud/api/WHI?tag=WHI-ATC01")
temp = r.json()[0]["val_calibrated"]
pres = r.json()[1]["val_calibrated"]
voltage = r.json()[2]["val_calibrated"]
print("Date_stamp,       Temp,Pres,   Bat")
data = date_stamp + "," + str(temp) + "," + str(pres) + "," + str(voltage) + "\n"
print(data)
f = open('/home/pi/botanica-park-lake/data.txt','a')
f.write(data)
f.close()
message = """
<h1>Atmospheric Conditions</h1>
<p>The current temperature is %s</p>
<p>The current atmospheric pressure is %s</p>
<p>The current battery voltage is %s</p>
""" % (html.escape(str(temp)), html.escape(str(pres)), html.escape(str(voltage)))
print(message)

f = open('/home/pi/botanica-park-lake/atm.html', 'w')
f.write(message)
f.close()






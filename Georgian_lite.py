import time,sys,os
from datetime import datetime,date

today=datetime.date(datetime.now())
finish=date(2028,11,17) # your project deadline
while 1:
    os.system('cls')
    starting_time = time.time()
    h=int(datetime.now().strftime("%H")) # hours
    m=int(datetime.now().strftime("%M")) # minutes
    s=int(datetime.now().strftime("%S"))+time.time()%1 # seconds upto nano seconds

    tm= h*60+m+s/60 # today minutes
    ts= h*3600+m*60+s # today seconds	
    fd=abs(finish-today).days # finish date

    print(f'''now {h:02d}:{m:02d}:{s:06.3f} /23:59:59.999  
tm {tm:09.4f} /1439.9999  
ts {ts:8.2f} /86399.99  

{fd+1-ts/86400:013.7f} /10414.9999999 days↓  
{fd*24+24-ts/3600:013.6f} /249999.999999 hours↓  
''')
	
    time.sleep(0.032)
    sys.stdout.write('\x1b[1A'*20)

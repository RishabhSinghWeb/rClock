import time,sys
from datetime import datetime,date

min,max,avgt,avg,difavg = 1,0,0,0,0
today=datetime.date(datetime.now())
finish=date(2028,11,17)
while 1:
	start = time.time()
	h=int(datetime.now().strftime("%H"))
	m=int(datetime.now().strftime("%M"))
	s=int(datetime.now().strftime("%S"))+time.time()%1
	tm= h*60+m+s/60
	ts= h*3600+m*60+s	
	rh=h+22 if h<2 else h-2
	rnow = rh*4.1666666667+m*0.06944444+s*0.001157
	fd=abs(finish-today).days
	
	end = time.time()
	ping =1000*(end -start)
	avgcopy = avg
	avg= (avgcopy*avgt+ping)/(avgt+1)
	difping =avg-avgcopy
	difcopy = difping
	difavg = (difcopy*avgt+difping)/(avgt+1)
	avgt+=1	
	if ping < min: min = ping
	if ping > max: max = ping	
	
	print(f'''{time.time():12.2f}

now {h:02d}:{m:02d}:{s:06.3f} /23:59:59.999  
tm {tm:09.4f} /1439.9999  
ts {ts:8.2f} /86399.99  

rnow {rh:02d}:{m:02d}:{s:06.3f} /23:59:59.999  
rnow {rnow:02.5f} /99.99999  
rmin {rh*60+m+s/60:09.4f} /1439.9999  

{fd+1-ts/86400:013.7f} /10414.9999999 days↓  
{fd*24+24-ts/3600:013.6f} /249999.999999 hours↓  

{min:.2f} < {ping:.2f} < {max:.2f} μs ping effi   
       {avg:.2f} avg μs  ''')
	
	time.sleep(0.032)
	sys.stdout.write('\x1b[1A'*20)
#	os.system( 'cls' )
#	for x in range(15):
#		sys.stdout.write('\x1b[1A'*2)		
#		sys.stdout.write(' '*36+'\n')
#		print(chr(127)*100)

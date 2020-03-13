import time,sys,os
from datetime import datetime,date

min_ping,max_ping,avg_count,avg_ping,dif_avg = 1,0,0,0,0
today = datetime.date(datetime.now())
finish = date(2028,11,17) # your project deadline
while 1:
\tos.system('cls') # clear screen
	starting_time = time.time()
	h =int(datetime.now().strftime("%H")) # hours
	m = int(datetime.now().strftime("%M")) # minutes
	s = int(datetime.now().strftime("%S"))+time.time()%1 # seconds upto nano seconds
	tm = h*60+m+s/60 # today minutes
	ts = h*3600+m*60+s # today seconds	
	rh = h+22 if h<2 else h-2 # r hours
	rnow = rh*4.1666666667+m*0.06944444+s*0.001157 # 100/24/60/60
	fd = abs(finish - today).days # finish date
	
	ending_time = time.time()
	ping = 1000*(ending_time - starting_time)
	avg_ping_copy = avg_ping
	avg = (avg_ping*avg_count+ping)/(avg_count+1)
	dif_ping = avg_ping - avg_copy
	dif_ping_copy = dif_ping
	dif_avg = (dif_avg*avg_count+dif_ping)/(avg_count+1)
	avg_count+=1	
	if ping < min_ping: min_ping = ping
	if ping > max_ping: max_ping = ping	
	
	print(f'''{time.time():12.2f}

now {h:02d}:{m:02d}:{s:06.3f} /23:59:59.999  
tm {tm:09.4f} /1439.9999  
ts {ts:8.2f} /86399.99  

rnow {rh:02d}:{m:02d}:{s:06.3f} /23:59:59.999  
rnow {rnow:07.5f} /99.99999  
rmin {rh*60+m+s/60:09.4f} /1439.9999  

{fd+1-ts/86400:013.7f} /10414.9999999 days↓  
{fd*24+24-ts/3600:013.6f} /249999.999999 hours↓  

{min_ping:.2f} < {ping:.2f} < {max_ping:.2f} ms ping effi   
       {avg_ping:.2f} avg ping ms  ''')
	
	time.sleep(0.032)
	
	# clear output
	sys.stdout.write('\x1b[1A'*20) # move cursor to the top
#	for x in range(15): # rewrite spaces
#		sys.stdout.write('\x1b[1A'*2)		
#		sys.stdout.write(' '*36+'\n')
#		print(chr(127)*100)

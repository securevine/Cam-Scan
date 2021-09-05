#Cam-scan for all ports
#!/usr/bin/python
import os
import sys
import socket
import platform
import time, datetime, os
from multiprocessing.dummy import Pool as ThreadPool

def scan(fileName):
	# masscan
	a = os.popen("masscan -p554,5554,8554,10554,18554 -iL %s --wait 0 "% fileName ).read()
	
	# Url extraction from massscan result
	print "\n"
	print "IP's to be scanned "
	print "-------------------"	
	for result in a.splitlines(): 
		ip1 = (result.split('on')[1]).strip()
		print ip1
		ip2 = (result.split('port'))[1].strip()
		ip3 = (ip2.split('/'))[0].strip()
		f1 = open("url", "a")
		print >> f1, (ip1+':'+ip3)
		f1.close()
		
def camerascan(url):		
	# Cameradar		
	ip = (url.split(':'))[0].strip()
	port = (url.split(':'))[1].strip()
	print "\n"
	print "Cameradar operation starting on",ip 
	print "------------------------------------------------"
	c = os.popen("docker run -t ullaakut/cameradar -T 50000 -t %s -p %s " %(str(ip), port)).read()
	print c
	time.sleep(2)

	# Url extraction from cameradar resulting file and taking screenshots	
	for line in c.splitlines():
		if "rtsp://" in line:
			line = line[43:-4] 
			f3 = open("rtsp_url", "a")
			print >> f3, line
			print "\n"
			print "Screenshot is being taken of", line
			print "--------------------------------------------------------------------------------"
			split1 = (line.split('@'))[1]
			split2 = (split1.split(':'))[0]
			os.system("ffmpeg -rtsp_transport tcp -y -i %s -ss 00:00:01.50 -vframes 1 Screenshots/%s.jpg " %(line,split2))		
			time.sleep(2)
			f3.close()
			
if __name__ == "__main__":
	os.system("mkdir Screenshots 2>/dev/null")
	#today = datetime.date.today()  
	#todaystr = today.isoformat()   
	#os.mkdir(todaystr)
	fileName = sys.argv[1]	
	with open (fileName, "r") as f:
		scan(fileName)
		f2 = open("url" , "r")
		b = f2.readlines()	
		f2.close()
		pool = ThreadPool(int(sys.argv[2]))
		results = pool.map(camerascan, b)		
		pool.close() 
		pool.join()
		

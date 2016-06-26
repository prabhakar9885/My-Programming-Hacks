"""
Scans the given path for all the media files and returns the length of the files in terms of time.

Usage:  python GetLength.py <Path to media files>

"""



import subprocess, re, sys, os, time

def getFilesRecursively( src ):
	files = []
	for root, dirnames, filenames in os.walk(src):
		files.extend( [ root +"/"+f for f in filenames ] )
	return files;

def updateProgess(count, maxval, desc="" ):
	sys.stdout.write( "\r" ); 
	sys.stdout.write( " "*columns );
	sys.stdout.write( "\r " + str(count)+ "/" + str(maxval) );
	sys.stdout.write( " : " + desc );
	sys.stdout.flush()
    


files = getFilesRecursively(sys.argv[1])


durationRegex = re.compile('\nDuration +: +([0-9]+h ?)?([0-9]+mn ?)?([0-9]+s ?)?')
totalHrs = 0
totalMns = 0
totalSec = 0
rows, columns = [ int(i) for i in os.popen('stty size', 'r').read().split() ]

total = len(files)
count = 0

for file in files:
	proc = subprocess.Popen( ['mediainfo' , file], stdout=subprocess.PIPE )
	fileInfo = proc.stdout.read()
	duration = durationRegex.search(fileInfo)
	if duration is None:
		continue;
	hrs, mns, sec = duration.groups()
	# print file+":"+str(duration.groups())
	hrs = int(hrs.strip()[:-1]) if hrs is not None else 0
	mns = int(mns.strip()[:-2]) if mns is not None else 0
	sec = int(sec.strip()[:-1]) if sec is not None else 0

	totalSec += sec
	if totalSec >59:
		totalMns += (totalSec/60)
		totalSec %= 60

	totalMns += mns
	if totalMns >59:
		totalHrs += totalMns/60
		totalMns %= 60

	totalHrs += hrs

	count+=1
	updateProgess( count, total, file )

sys.stdout.write( "\n " ); 

if totalHrs!=0:
	sys.stdout.write( str(totalHrs)+"h " )
if totalMns!=0:
	sys.stdout.write( str(totalMns)+"m " )
if totalSec!=0:
	sys.stdout.write( str(totalSec)+"s " )

print("")
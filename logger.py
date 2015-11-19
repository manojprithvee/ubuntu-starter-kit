import subprocess
print "Starting the logger for Ubuntu-Starter-kit.."
p = subprocess.Popen("tail -F ubuntu-stater-kit.log", stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True,executable="/bin/bash")
while(True):
  retcode = p.poll() #returns None while subprocess is running
  print p.stdout.readline()
  if(retcode is not None):
    break
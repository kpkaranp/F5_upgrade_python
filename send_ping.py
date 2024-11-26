import os

def check(hostname):
  flag = True
  while(flag):
    response = os.system("ping -c 10 " + hostname +" > /dev/null 2>&1")
    if response == 0:
      state = 'up'
      print "F5 is UP"
      flag = False
    else:
      print "F5 is rebooting"
      state = 'down'
  return state


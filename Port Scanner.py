import socket,random
from errno import ECONNREFUSED
ports_to_scan = []
to_scan = ""
target_ip = ""
rni = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
def main_menu():
    global to_scan,target_ip
    print """
  ___         _     ___
 | _ \___ _ _| |_  / __| __ __ _ _ _  _ _  ___ _ _
 |  _/ _ \ '_|  _| \__ \/ _/ _` | ' \| ' \/ -_) '_|
 |_| \___/_|  \__| |___/\__\__,_|_||_|_||_\___|_|
By EkosFox - version 0.1b
"""
    choice_1 = raw_input("""
    (1) Scan A Target
    (2) **Soon**
    (3) Exit
        """)
    if choice_1 == "1":
        print "Scan A Target"
        target_ip = raw_input("Enter the target's ip: ")
        to_scan = raw_input("How many ports you want to scan? : ")
        try:
            for q in range(0,int(to_scan)):
                ports_to_scan.append(input("Enter the port: "))
        except:
            print "EXCEPTION: Error was found. Check the port entered."
            main_menu()

        scan_target(target_ip)
    elif choice_1 == "2":
        print "Wait and see..."
        main_menu()
    elif choice_1 == "3":
        print "Goodbye!"
        exit()

def scan_target(ip):
    file = open("PortScanDump" + rni + ".txt","wb+")
    global to_scan,ports_to_scan
    for q in range(0,int(to_scan)):
        true = 0
        actual_port = ports_to_scan[q]
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((ip,actual_port))
            print "The port " + str(actual_port) + " is open!"
            true = 1
            file.write("%s \n" % target_ip )
            file.write("%s \n" % actual_port)
        
        except socket.error as err:
            if err.errno == ECONNREFUSED:
                print "The port " + str(actual_port) + " is closed!"
        except socket.timeout as err:
            print err
            print "That port is not reponsive"
    if true == 1:
        file = open("PortScanDump.txt","wb+")
        file.write("%s \n" % target_ip )
        for i in ports_to_scan:
            file.write("%s \n" % i)
        file.close()
    print "Returning to menu..."
    ports_to_scan = list()
    to_scan = ""
    file.close()
    main_menu()
            
                
main_menu()

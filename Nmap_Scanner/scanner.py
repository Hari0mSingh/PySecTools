import nmap
import sys
import time

nm_scan = nmap.PortScanner()
nm_scanner = nm_scan.scan(sys.argv[1], '80')

print("[*] Running...")
host_is_up = "[*] The host %s is %s.\n" % (sys.argv[1], nm_scanner['scan'][sys.argv[1]]['status']['state'])

port_scanned = "[*] The port %s was scanned.\n" % nm_scanner['nmap']['scaninfo']['tcp']['services']

port_state = "[*] Port 80 is %s.\n" % nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']

scan_method = "[*] The scan method is: %s.\n" % nm_scanner['nmap']['scaninfo']['tcp']['method']

scan_reason = "[*] The scan result reason is: %s.\n" % nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']

nmap_command = "[*] The command: %s.\n" % nm_scanner['nmap']['command_line']

with open('%s-scan_report.txt' % sys.argv[1], 'w') as f:
    f.write("Scannig the target : %s"%(sys.argv[1])+"\n")
    f.write(host_is_up + port_scanned + port_state + scan_method + scan_reason + nmap_command)
    f.write('\nReport generated ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print('\nFinished....')
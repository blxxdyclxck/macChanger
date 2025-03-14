import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest = "interface", help="Interface para cambiar dirección MAC")
parser.add_option("-m", "--mac", dest = "newMac", help="Nueva dirección MAC")

(options, arguments) = parser.parse_args()

interface = options.interface
newMac = options.newMac
print("[+] Cambiando direccion MAC para " + interface +  " a " + newMac)


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
subprocess.call(["ifconfig", interface, "up"])


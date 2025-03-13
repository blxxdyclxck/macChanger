import subprocess

interface = input("interface > ")
newMac = input("mac > ")

print("[+] Cambiando direccion MAC para " + interface +  " a " + newMac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + newMac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)



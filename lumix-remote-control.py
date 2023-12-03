import requests
import time
camera_ip_address = "192.168.54.1"
udn = "<specify_udn>"
hostname = "<specify_hostname>"
choice = 0

def peering():
    r = requests.get('http://' + camera_ip_address + ':80/cam.cgi?mode=accctrl&type=req_acc&value=' + udn + '&value2=' + hostname)
    if "ok" in r.text:
        r = requests.get('http://' + camera_ip_address + ':80/cam.cgi?mode=setsetting&type=device_name&value=' + hostname)
        if "ok" in r.text:
            print("Connecion successfull")
    else:
        print("Connection error :\n" + r.text)
        exit()

def capture():
    r = requests.get('http://' + camera_ip_address + ':80/cam.cgi?mode=camcmd&value=capture')
    if "ok" in r.text:
        print("Capture successfull")
    else:
        print("Capture failed")

def intervalometer():
    time_period = input("Sur combien de temps voulez-vous réaliser les prises de vue? (en secondes)\n")
    time_period = int(time_period)
    interval = input("Sur quelle intervalle de temps voulez-vous réaliser les prises de vue? (en secondes)\n")
    interval = int(interval)
    iteration = time_period // interval
    i = 1
    print("Il y aura donc " + str(iteration) + " prises de vue\n")
    while i <= iteration:
        print("Prise de vue n°" + str(i) + " :")
        #capture()
        if i != iteration:
            time.sleep(interval)
        i = i + 1
    print("\nPrises de vue terminées! Retour au menu principal\n")
    
while choice != 4:
    print("Bienvenue! Que souhaitez-vous faire ?\n")
    print("1. S'appairer avec l'appareil photo")
    print("2. Réaliser une prise de vue")
    print("3. Paramétrer une session de prise de vue avec un intervallomètre")
    print("4. Quitter le programme\n")
    choice = input("Choix ? (1, 2, 3 ou 4):\n")
    choice = int(choice)
    if choice == 1:
        peering()
    if choice == 2:
        capture()
    if choice == 3:
        intervalometer()
    if choice == 4:
        exit()
    

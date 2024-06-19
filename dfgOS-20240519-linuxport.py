from rich.console import Console
import os
import time
import random
class dfgos:
    def test():
        print('Finding PCI Devices')
        time.sleep(2)
        print('0:0:0 Intel 440BX/ZX AGPset Host Bridge\n0:1:0 Intel 440BX/ZX AGPset PCI-to-PCI Host Bridge')
        time.sleep(5)
        print('0:7:0 Intel PIIX4/4E/4M ISA Bridge\n0:15:0 Virtual NVIDIA 9500MGS\n0:16:0 Mylex BT958 SCSI Host Adapter')
        time.sleep(4)
        print('0:17:0 Virtual 5.0 Virtual USB 2.0 Host Controller\n     2:1:0 Intel PIIX4/4E/4M USB Interface\n     2:2:0 AMD PCnet LANCE PCI Ethernet Controller\n     2:3:0 Ensoniq AudioPC\n     2:4:0 Virtual Standard Enchaned PCI to USB Host Controller')
        time.sleep(6)
        print('0:21:0 Virtual PCI Express Root Port\n0:22:0 Virtual PCI Express Root Port\n0:23:0 Virtual PCI Express Root Port\n0:24:0 Virtual PCI Express Root Port')
        time.sleep(3)
        print('Found partition at idx 0')
        print('Finded')
dfgos.test()
print('dfgOS Pre-Alpha Build 20240519 Installer')
name = input('Account Set\nName: ')
password = input(f'Password for {name}: ')
c = Console()
def main_start():
    os.system('clear')
    print('Files\nTestTXT       <txt>')
    while True:
        cons = input(f'devOS [{name}]>> ')
        if cons == 'fs':
            print('File System is not finished. Function not yet work.')
        elif cons == 'sysinfo':
            print('Creator GitHub: DcorpProj\ndfgOS 20240519 for Linux subsystem SDK\nFile system: FAT32\nCPU VirtualCPU 1 8-core @ 1.980GHz\nAll RAM: 125MB by VirtualRAM 1\nAvailable RAM: 102MB\nUsed RAM: 23MB')
        elif cons == 'exit':
            print('Thanks you for testing OS')
            input('Press enter')
            break
        elif cons == 'rand':
            rnd = random.randint(1, 9999999999999999999999999999)
            print(rnd)
        elif cons == 'calc':
            print(eval(input('calc: ')))
        elif cons == 'read TestTXT.txt':
            print('--TestTXT.txt--\nTesting TXT files')
        elif cons == 'help':
            print('\ndfgOS Pre-Alpha 20240519\nread - Read files, like a cat in Linux\nsysinfo - System information\nexit - Exit\nrand - Generate random number\ncalc - Calculator\nfs - UNFINISHED, Not works')
        else:
            c.print('[red bold]Unknown command, Enter help and enter')
os.system('clear')
c.print('[red bold]     _  __       ____   _____ ')
c.print('[blue bold]    | |/ _|     / __ \ / ____|          version: Pre-Alpha 20240519 (linux-port)')
c.print('[yellow bold]  __| | |_ __ _| |  | | (___          GitHub: DcorpProj')
c.print('[purple bold] / _` |  _/ _` | |  | |\___ \ ')
c.print('[bold red]| (_| | || (_| | |__| |____) |')
c.print('[bold green] \__,_|_| \__, |\____/|_____/ ')
c.print('[bold yellow]           __/ |              ')
c.print('[bold violet]          |___/               ')
print(f'\n\n\n_Login_\n\nName: {name}')
while True:
    passwd = input('Enter password: ')
    if passwd == password:
        
        main_start()
        break
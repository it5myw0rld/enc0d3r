import numpy as np  
import random, time
from os import system, name
alphabet = " abcdefghijklmnopqrstuvwxyz1234567890~`!@#$%^&*()-=_+[]{}\\|'\"/.,><" 
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system("clear")
def encode():
    clear()
    alphabet_values = [i for i in range(0, len(alphabet))]
    message = input("[+] Enter Message: ")
    message = message.lower()
    msg_int = []
    for i in range(len(message)):
        for j in range(len(alphabet_values)):
            if (message[i] == alphabet[j]):
                msg_int.append(alphabet_values[j])
    splitted = [msg_int[i:i + 3] for i in range(0, len(msg_int), 3)]
    for i in range(len(splitted)):
        while len(splitted[i]) != 3:
            splitted[i].append(0)
    while True:
        mat = [[random.randint(1, 20) for j in range(3)] for i in range(3)]
        det  = np.linalg.det(mat)
        if det != 0:
            inv = np.linalg.inv(mat)
            inv = np.around(inv)
            r = np.dot(mat, inv)
            i = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            if np.all(r == i):
                break
    result = np.dot(splitted, mat)
    result = result.tolist()
    def li_str(ab):
        b = []
        for i in range(len(ab)):
            for j in range(len(ab[0])):
                b.append(str(ab[i][j]))
        c = ', '.join(b)
        return c
    result = li_str(result)
    mat = li_str(mat)
    print("\x1b[1;32m[+] Please wait...we're working for you :-)")
    time.sleep(1)
    clear()
    print("Encoded Message: ", result)
    print("Encoding key: ", mat)
    print("\n\x1b[1;31mThis key is Random key. Don't Forget it!\n")
    time.sleep(2)
    ch = input("\n[!] Do You continue[Y/n]: ")
    if ch.lower() == 'n':
        exit()
    print('\n\n\n')
# ---------------------decode-----------------------
def decode():
    clear()
    print("\033[1;33m[+] Enter Key and Message seperated by comma ','")
    key = input("[+] Enter key: ")
    def str_list(a):
        li = list(a.split(','))
        li = [li[i:i +3] for i in range(0, len(li), 3)]
        c = []
        for i in range(len(li)):
            for j in range(len(li[0])):
                c.append(int(li[i][j]))
        c = [c[i:i +3] for i in range(0, len(c), 3)]
        return c
    key = str_list(key)
    for i in range(len(key)):
        for j in range(len(key[0])):
            if (key[i][j]) >= 21:
                print("\033[1;31m Wrong Key :-(")
                print("\033[1;31m Program will be Exited..")
                time.sleep(3)
                exit()
    msg = input("[+] Enter encoded message: ")
    msg = str_list(msg)
    key = np.linalg.inv(key)
    decoded = np.dot(msg, key)
    decoded = np.around(decoded).tolist()
    result = ""
    for i in range(len(decoded)):
        for k in range(len(decoded[0])):
            result += alphabet[round(decoded[i][k])]
    print("You'r Decoded message is ", result)
    ch = input("\n[!] Do You Continue[Y/n]: ").lower()
    if ch == 'n':
        exit()
    print("\n\n\n")
if __name__ == '__main__':
	while(True):
		print("------------------------Menu--------------------\n1. Encode\n2. Decode\n3. Exit\n")
		choice = int(input('Enter choice: '))
		if choice == 1:
			encode()
		elif choice == 2:
			decode()
		else:
			print("[!] Bye!. Shutdowning...")
			break

def encrypt():
    a = int(input("enter the integer you wish to shift the letters by:"))
    b = input("enter the text to be encrypted")
    l = []
    s = ""
    for i in b.lower():
        l.append(i)
    for i in range(len(l)):
        s+= (chr(ord(l[i])+a))

    print(s)

def decryp():
    a = int(input("enter the integer by which the message was shifted:"))
    b = input("enter the text to be encrypted")
    l = []
    s = ""
    for i in b.lower():
        l.append(i)
    for i in range(len(l)):
        s += (chr(ord(l[i]) - a))

    print(s)


print("menu")
print("1 - encryption")
print("2 - decryption")
ask = int(input("enter the menu number for the process to follow"))
if ask==1:
    encrypt()
elif ask==2:
    decryp()

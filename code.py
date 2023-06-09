def encrypt():
    a = int(input("enter the integer you wish to shift the letters by:"))
    b = input("enter the text to be encrypted")
    l = []
    d = dict()
    for i in b.lower():
        l.append(i)
    d[0]="a"
    d[1]="b"
    d[2]="c"
    d[3]="d"
    d[4]="e"
    d[5]="f"
    d[6]="g"
    d[7]="h"
    d[8]="i"
    d[9]="j"
    d[10]="k"
    d[11]="l"
    d[12]="m"
    d[13]="n"
    d[14]="o"
    d[15]="p"
    d[16]="q"
    d[17]="r"
    d[18]="s"
    d[19]="t"
    d[20]="u"
    d[21]="v"
    d[22]="w"
    d[23]="x"
    d[24]="y"
    d[25] = "z"
    g=""
    for k in range(len(l)):
        for j in d:
            if l[k]==d[j]:
                g=g+(d[j+a])
    print(g)

def decryp():
    a = int(input("enter the integer by which the message was shifted:"))
    b = input("enter the text to be encrypted")
    l = []
    d = dict()
    for i in b.lower():
        l.append(i)
    d[0] = "a"
    d[1] = "b"
    d[2] = "c"
    d[3] = "d"
    d[4] = "e"
    d[5] = "f"
    d[6] = "g"
    d[7] = "h"
    d[8] = "i"
    d[9] = "j"
    d[10] = "k"
    d[11] = "l"
    d[12] = "m"
    d[13] = "n"
    d[14] = "o"
    d[15] = "p"
    d[16] = "q"
    d[17] = "r"
    d[18] = "s"
    d[19] = "t"
    d[20] = "u"
    d[21] = "v"
    d[22] = "w"
    d[23] = "x"
    d[24] = "y"
    d[25] = "z"
    g = ""
    for k in range(len(l)):
        for j in d:
            if l[k] == d[j]:
                g = g + (d[j - a])

    print(g)


print("menu")
print("1 - encryption")
print("2 - decryption")
ask = int(input("enter the menu number for the process to follow"))
if ask==1:
    encrypt()
elif ask==2:
    decryp()

















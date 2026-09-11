s = str(input())
sl = {
    'A' : 'A',
    'H' : 'H',
    'I' : 'I',
    'M' : 'M',
    'O' : 'O',
    'T' : 'T',
    'U' : 'U',
    'V' : 'V',
    'W' : 'W',
    'X' : 'X',
    'Y' : 'Y',
    '1' : '1',
    '8' : '8',
#    'Z' : '5',
#    'S' : '2',
#    'E' : '3',
#    'J' : 'L',
#    '2' : 'Z',
#    '3' : 'E',
#    '5' : 'Z',
#    'L' : 'J'
    }

SL = {
    'Z' : '5',
    'S' : '2',
    'E' : '3',
    'J' : 'L',
    '2' : 'Z',
    '3' : 'E',
    '5' : 'Z',
    'L' : 'J'
}

S = []
a, b = 0, 0

for symbol in s:
    S.append(symbol)
k = int(len(S)/2)
for i in range(k):
    if  sl.get(S[i].upper()) != None and sl.get(S[-i].upper()) != None:
        if sl[S[i].upper()] == sl[S[-i].upper()]:
            a = a + 1
    elif SL.get(S[i].upper()) != None and SL.get(S[-i].upper()) != None:
        if SL[S[i].upper()] == S[-i].upper():
            b = b + 1
    else: print(f"{s} is not a palindrome.")

if len(S) % 2 == 1:
    if a == k:
        if sl.get(S[k+1].upper()) != None:
            print(f"{s} is a mirrored palindrome.")
        else:
            print(f"{s} is a regular palindrome.")
    elif b == k: 
        print(f"{s} is a mirrored string.")


elif len(S) % 2 == 0:
    if a == k:
        print(f"{s} is a mirrored palindrome.")
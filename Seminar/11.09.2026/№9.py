s = str(input())

S = []

for symbol in s:
    S.append(symbol)
S.append(" ")

pr = {
    "." : 1, 
    "!" : 1, 
    "?" : 1,
   # " " : 2
    }

cout = 0

for i in range(len(S)):
    if pr.get(S[i]) != None and pr[s[i]] == 1:
        if (pr.get(S[i+1]) != None and pr[S[i+1]] != pr[S[i]]):
            cout += 1
        elif (pr.get(S[i+1]) == None and (pr.get(S[i]) != None)):
            cout += 1
print(cout)
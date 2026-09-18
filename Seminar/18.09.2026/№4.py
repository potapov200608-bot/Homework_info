a, sim = input().split(" ")
a = int(a)

if  a%2 != 0:
    for i in range(1, int(a/2)+1):
        print(sim*i)
    print(sim*(int(a/2)+1))
    for i in range(int(a/2) , 0, -1):
        print(sim*i)
else: 
    for i in range(1, int(a/2)):
        print(sim*i)
    for i in range(int(a/2)-1, 0, -1):
        print(sim*i)
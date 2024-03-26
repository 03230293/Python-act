# N=9
# def toh(self, N, fromm, to, aux):
#     if N==1:
#         print("Move disk1 from nod", +str(fromm)+ "to rod" + str(to))
#         return 1
#     move=0
#     moves+=self.toh(N-1, fromm, aux, to)
#     moves+=1
#     print("Move disk ", + str(N), +"fromm rod"+ str(fromm)+ "to rod" + str(to))
#     moves+=self.toh(N-1, aux, to, fromm,)
#     return moves
# print(toh(N))

def hanoi(n,f,to,via):
    if n==1:
        print("move disk from", f, "to", to)
    else:
        hanoi(n-1,f,via,to)
        print("Move disk", n, "from", f, "to", to)
        hanoi(n-1, via, to, f)

n=3
f="A"
to="B"
via="C"
hanoi(n,f,via,to)
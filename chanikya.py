L=["X", 20, "Y", 10, "Z", 30]
CNT=0
ST =" "
INC=0
for C in range(1,6,2):
 CNT=CNT +C
 ST=ST +L[C-1]+"@"
 INC= INC +L[C]
 print (CNT, INC, ST)
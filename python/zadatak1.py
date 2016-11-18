"""
1. Napiši funkciju koja prima listu cijelih brojeva
 i iz nje izdvaja parne brojeve te ih sprema u novu 
 listu i vraća tu listu s parnim brojevima
  (npr. [1, 2, 3, 4, 5, 6, 7, 8, 9] >> [2, 4, 6, 8])."""


a=[]
parni=[]
neparni=[]

x=int(raw_input("Upisi broj koji želiš dodati na listu (za izlazak unesi 0: "))

while(x!=0):
  a.append(x)
  
  if x%2 == 0:
    parni.append(x)
  else:
    pass
  
  x=int(raw_input("Upisi jos jedan broj: ")) 
  
print a
print "Svi parni brojevi koje si napisala su: " 
print parni

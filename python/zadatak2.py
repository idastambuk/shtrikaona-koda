"""Napiši skriptu koja od korisnika traži unos tri broja i 
    javlja koji je od tih brojeva najveći."""
    
a=[]

while len (a) < 3:
  x= int(raw_input("Upisi broj: "))
  a.append(x)
  
print "najveći broj je", max(a)

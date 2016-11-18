""" Napiši funkciju koja prima jednu riječ (niz znakova)
i vraća listu čiji su elementi pojedinačna slova iz te riječi 
(npr. 'auto' >> ['a','u','t','o']).
"""
slova=[]
a=raw_input("Upisi rijec")

for item in a:
  slova.append(item)
  
print slova
  
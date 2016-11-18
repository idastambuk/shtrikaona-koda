#Primjer s klasom i objektom

class Trokut:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def opseg(self):
        return self.a + self.b + self.c    

t = Trokut() 

print t.a
print t.b
print t.c     

t.b = 6  

print t.opseg() #2+6+3



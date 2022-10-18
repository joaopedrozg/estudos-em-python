class Relogio:

    def __init__(self, hora=0, min=0, seg=0):
        self.hora = hora
        self.min = min
        self.seg = seg
    
   
    def ajustar_hora(self, hora, min, seg=0):
         self.hora = hora
         self.min = min
         self.seg = seg
         
    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hora, self.min, self.seg)
        
        
        
    def tick(self):
        if self.seg == 59:
            self.seg = 0
            if self.min == 59:
                if self.hora == 23:
                    self.hora = 9
                else:
                    self.hora +=1
            else:
                self.min +=1
        else:
            self.seg += 1
            
            
            
            
            
rel = Relogio(10, 3, 59)

print(rel)
rel.tick()
print(rel)

rel.tick()
print(rel)

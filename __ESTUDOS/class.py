class Data:
    
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        print(self)
        
    @classmethod
    def de_string(cls, data_string):
        dia, mes, ano = map(int, data_string.split('-'))
        data = cls(dia, mes, ano)
        return data
        
        
    @staticmethod
    def is_date_valid(data_string):
        dia, mes, ano = map(int, data_string.split('-'))
        return dia <= 31 and mes <= 12 and ano <= 2020
        
    
        
        
data = Data(10,10,10)
data1 = Data.de_string("10-10-2016")
vdd = Data.is_date_valid('30-10-2016')
print(vdd)

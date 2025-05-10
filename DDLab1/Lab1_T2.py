datamb = float(1.44)
databy = float(1.44*(1024**2))
pagen = 100
strn = 50
symn = 25
symby = 4

dbby = pagen*strn*symn*symby
n = int(databy//dbby)

print("Количество книг, помещающихся на дискету:", n)

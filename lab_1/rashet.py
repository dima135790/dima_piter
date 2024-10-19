disk = 1.44*1024*1024
pages = 100
lines = 50
symbols = 25
ves = 4
numbers=int(disk // (pages * lines * symbols * ves))
print("Количество книг, помещающихся на дискету:",numbers)

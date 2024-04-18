leer = 0
sumatoria = 0
for i in range(0,3,1):
 leer += float(input(f"ingrese el leer {i+1}:"))
if leer > 0:
   sumatoria = sumatoria + leer
print(f"ingrese la sumatoria :",sumatoria)


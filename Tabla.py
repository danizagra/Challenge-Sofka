import pandas as pd
from tabulate import tabulate

# Imprime tabla a partir de los datos de 
# una lista de listas:
a = 100
b = 'bogota'
rios1 = [[b, a],
         ['Guadiaro', 79],
         ['Guadalhorce', 154],
         ['Guadalmedina', 51.5]]

       
print(tabulate(rios1))

df=pd.DataFrame(rios1)
print (df)
ordenada = df.sort_values(1, ascending=False)
print (ordenada)
print ('--------')

print (tabulate(ordenada.iloc[[0,1]],showindex=False))

import csv

def read_csv(path):
    with open(path,'r') as csvfile:
      reader = csv.reader(csvfile,delimiter=',') 
      # leemos la primera fila
      # que corresponde a los nombre 
      # de las columnas
      header = next(reader)
      data = []
      # iterar el archivo 
      for row in reader:
         # crea tuplas clave,valor 
         iterable = zip(header,row)
         # dictionary comprehention
         country_dict = {key: value for key ,value in iterable}
         data.append(country_dict)
      return data


if __name__ ==  '__main__':
   data = read_csv('data.csv')
   print(data[0])
   print(type(data[0]))

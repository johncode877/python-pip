import charts
import utils
import csv_utils
import charts

# https://learnpython.com/blog/filter-dictionary-in-python/
# https://nextjournal.com/jgomo3/recorrer-diccionarios-en-python?change-id=CmyCqWfaXPsyd47wgq7hzz

def run():
   
   data = csv_utils.read_csv('data.csv')
   
   # para una mejor visualizacion 
   # podemos filtrar por continente 
   data = list (filter(lambda item: item['Continent']=='South America',data))
   
   # solucion propuesta en clase 
   countries = list(map(lambda x:x['CCA3'],data))
   percentages = list(map(lambda x:float(x['World Population Percentage']),data))
   charts.generate_pie_chart(countries,percentages)
   
   country_name = input('Type Country => ') 
   
   result = utils.get_data_by_country(data,country_name)
   print(result) 
   
   if len(result) > 0:
     country_dict = result[0]
     result = utils.get_population(country_dict)
     
     charts.generate_bar_chart(country_name,result.keys(),result.values()) 


if __name__ == '__main__':
  run()
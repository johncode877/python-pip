# modulo con funciones 
# definidas 


def get_population(dict_country):
    result = {key.replace(' Population',''):int(value) for (key,value) in dict_country.items() if 'Population' in key and 'Percentage' not in key}
    return result

'''
def get_population():
    keys = ['pe','col','bol']
    values = [300,400,250]
    return keys,values
'''

def get_data_by_country(data,country):
    result = list(filter(lambda item:item['Country/Territory'] == country,data))
    return result

def filtering_population(dict):    
    key, value = dict
    if 'Population' in key:
        return True  # filter pair out of the dictionary
    else:
        return False  # keep pair in the filtered dictionary


def get_data_population(data_population):
 result = {country:population for (country,population) in data_population.items() if population > 50 }
 print(result)


A = 'Hello'






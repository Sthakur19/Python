travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
    travel_log_dic = {
    }
    travel_log_dic["country"] = country
    travel_log_dic["visits"] = visits
    travel_log_dic["cities"] = cities
    travel_log.append(travel_log_dic)




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

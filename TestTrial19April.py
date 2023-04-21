temperatures = [
{
'monday': 12,
'wednesday': 13,
'friday': 14
},
{
'monday': 15,
'friday': 12
},
{
'tuesday': 10,
'thursday': 11,
'saturday': 12
},
]

def get_hottest_day(temperatures):
    maxTemp = []
    for i in range(0,len(temperatures)):
        res = 0
        for val in temperatures[i].values():
             res += val
        # using len() to get total keys for mean computation
        res = res / len(temperatures)
        maxTemp.append(res)
        # printing result
    print(max(maxTemp))

get_hottest_day(temperatures)
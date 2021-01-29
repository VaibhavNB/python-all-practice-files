import json
data='{"var1":"harry","var2":56}'
parsed=json.loads(data)           #json load
print(parsed['var1'])

data2={
    "chnla_name":"codewithharry",
    "cars": ['bmw','audi8','maruti'],
    "fridg":('roti',540),
    "isbad":False
}
jscomp=json.dumps(data2)            #json dumps   this converts the python dict into js compatible dict
print(jscomp)

#task what is sort_keys_parameter in dumps



groc = {
    'milk': 60,
    'biscut':10,
    'egg':40,
    'butter':100
}

print(f"Original dictionary: {groc}")

print(groc['milk']) #accessing the value of key 'milk'

print(groc.get('egg')) #accessing the value of key 'egg' it does not get error if key is not present in dictionary

print(groc.keys())

print(groc.values())

print(groc.items())

groc.update({'cake': 250})
print(f"updated dict is : {groc}")


dict=groc.copy()

print(f"copied dict is : {dict}")
print(id(groc),id(dict))
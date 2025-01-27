thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])#Ford

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)#{'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

#<class 'dict'>

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)#{'name': 'John', 'age': 36, 'country': 'Norway'}

#x = thisdict.get("model")
#x = thisdict["model"]

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)#dict_keys(['brand', 'model', 'year'])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)#dict_values(['Ford', 'Mustang', 1964])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
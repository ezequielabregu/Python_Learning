customer = {
    "name": "john smith",
    "age": 30,
    "is_verified": True
}
# print(customer["age"]) # llamo a la key del diccionario customer
customer["name"] = "Jack Smith" # actualizo el key "name"
customer["birthdate"] = "Jan  1 1980" # --> agrego el key al dictionarie
print(customer.get("birthdate")) # --> es mejor que la anterior xq no produce error si la key no existe
print(customer)
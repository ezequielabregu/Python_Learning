from Chef import Chef   #importo una Class para insertar su contenido en la nueva Class

class ChineseChef(Chef):    #Ahora tengo todas las funciones de Chef + las nuevas

    def make_fried_rice(self):
        print("the chef makes frie rice")

    def make_special_dish(self):
        print("the chef makes vegan food)") # reemplaza/ sobre escribe la función de la Class Chef
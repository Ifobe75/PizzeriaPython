print('==============================================================')
print('                     PIZZERIA NAPOLI                          ')
print('                        BIENVENIDO                            ')
print('==============================================================')
tipo = " "
ingrediente = " "

while tipo != "1" or "2":
    tipo = (input("Selecciona la opción que deseas para tu pizza: \n\n\t\t1.- Tradicional\n\n\t\t2.- Vegana \n\n¿Que Opción escoges?(1 o 2):"))
    print('==============================================================')
    if tipo == "1":
        tipoPizza = "Tradicional"
        print("    Todas nuestras pizzas incluyen tomate y mozzarella.\n   Personaliza tu pizza añadiendo un tercer ingrediente.")
        print('==============================================================')
        while ingrediente.lower() not in ["jamón", "peperoni", "salmón"]: 
            ingrediente = input("Estós son los ingredientes que puedes escoger:\n\n\t\tA) Jamón.\n\n\t\tB) Peperoni.\n\n\t\tC) Salmón.\n\n\t\t¿Cúal escoges?: ")
            if ingrediente.lower() in ["jamón", "peperoni", "salmón"]:
                print('==============================================================')
                print(f"Puedes recoger tu pizza {tipoPizza} con {ingrediente} en 15 minutos")
                print('==============================================================')
                break
            else:
                print('==============================================================')
                print(f"\t     Lo sentimos, no nos queda {ingrediente}")
                print('==============================================================')
        break
    elif tipo == "2":
        tipoPizza = "Vegana"
        print("    Todas nuestras pizzas incluyen tomate y mozzarella.\n   Personaliza tu pizza añadiendo un tercer ingrediente.")
        print('==============================================================')
        while ingrediente.lower() not in ["tofu", "pimiento"]:
            ingrediente = input("Estós son los ingredientes que puedes escoger:\n\n\t\tA) Tofu.\n\n\t\tB) Pimiento.\n\n\t\t¿Cúal escoges?: ")
            if ingrediente.lower() in ["tofu", "pimiento"]:
                print('==============================================================')
                print(f"Puedes recoger tu pizza {tipoPizza} con {ingrediente} en 15 minutos")
                print('==============================================================')
                break
            else:
                print('==============================================================')
                print(f"\t     Lo sentimos, no nos queda {ingrediente}")
                print('==============================================================')
        break
    else:
        print("\t\tNo tenemos ese tipo de pizza")
        print('==============================================================')
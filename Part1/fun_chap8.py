def fun_make_pizza(size, *toppings):
    print("\nMaking a "+str(size)+' inch pizza with following toppings:')
    for topping in toppings:
        print("- "+topping)
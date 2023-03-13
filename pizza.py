def cost_calculator(*pizzalist, drinks=[], wings=[], coupon=0):
    
    toppings = {"pepperoni": 1, "mushroom": .5, "olive": .5, "anch": 2, "ham": 1.5}
    drinks = {"small": 2, "medium": 3, "large": 3.5, "tub": 3.75}
    wings = {"10": 5, "20": 9, "40": 17.5, "100": 48}
    
    total = 0
    
    for pizza in pizzalist:
        if toppings in pizza:
            total =+ toppings[pizza]
        total =+ 13
        
    for i in drinks:
        total =+ drinks[i]

    
    
    
    
    
    total = total * 1.0625
    total = total * (1-coupon)
    total = round(total, 2)
    return total


print(cost_calculator(["mushroom"], drinks=["small"]))


#from bwsi_grader.python.pizza_shop import grader
#grader(cost_calculator)
from generador import select_with_weight

def simulate_seller():
    number_of_cars_options = [0,1,2,3,4,5]
    number_of_cars_weigths = [0.1,0.15,0.2,0.25,0.2,0.1]

    type_of_car_options = ['Compacto', 'Mediano', 'Lujo']
    type_of_car_weights = [0.4,0.35,0.25]

    medium_car_comission_options = [400, 500]
    medium_car_comission_weights = [0.4, 0.6]

    luxury_car_comission_options = [1000, 1500, 2000]
    luxury_car_comission_weights = [0.35, 0.4, 0.25]

    # Select a number of cars
    number_of_cars = select_with_weight(number_of_cars_options, number_of_cars_weigths)
    
    i = 0
    total = 0

    while i < number_of_cars:
        type_of_car = select_with_weight(type_of_car_options, type_of_car_weights)
        if type_of_car == 'Compacto':
            total += 250
        if type_of_car == 'Mediano':
            total += select_with_weight(medium_car_comission_options, medium_car_comission_weights)
        if type_of_car == 'Lujo':
            total += select_with_weight(luxury_car_comission_options, luxury_car_comission_weights)
        i += 1
    return total

def simulate_n_sellers(n):
    sellers = []
    for i in range(n):
        sellers.append(simulate_seller())
    
    return sum(sellers)/float(n)

if __name__ == "__main__":
    print(simulate_n_sellers(100000))
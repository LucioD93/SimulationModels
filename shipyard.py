# Ejercicio 5

from generador import select_with_weight

DAYS_BETWEEN_ARRIVALS_OPTIONS = [1, 2, 3, 4, 5]
DAYS_BETWEEN_ARRIVALS_WEIGTHS = [0.2, 0.25, 0.35, 0.15, 0.05]

SHIP_TYPE_OPTIONS = ['L', 'M', 'S']
SHIP_TYPE_WEIGHTS = [0.4, 0.35, 0.25]

class Ship():
    def __init__(self, type):
        self.type = type
        self.days_waiting = 0

    def add_day(self):
        self.days_waiting += 1

def simulate_ships():

    ship_queue = []
    # for i in range(100):
    #     ship_queue.append(select_with_weight(SHIP_TYPE_OPTIONS, SHIP_TYPE_WEIGHTS))
    ship_B_queue = [None, None, None, None]

    remaining_A_days = 0
    remaining_B_days = 0

    ship_in_A = None
    ship_in_B = None

    simulation_days = 365
    counter = 0

    ships_in_queue = []
    days_ship_waiting = []
    empty_A_days = 0
    empty_B_days = 0

    days_for_next_arrival = select_with_weight(DAYS_BETWEEN_ARRIVALS_OPTIONS, DAYS_BETWEEN_ARRIVALS_WEIGTHS)

    while counter <= simulation_days:
        # print('---------')
        # print(counter)
        # print(ship_queue)
        # print(days_for_next_arrival)
        # print(remaining_A_days, remaining_B_days)
        counter += 1

        if remaining_A_days:
            remaining_A_days -= 1
            A_is_empty = False
        else:
            A_is_empty = True
        if remaining_B_days:
            remaining_B_days -= 1
            B_is_empty = False
        else:
            B_is_empty = True

        if days_for_next_arrival != 0:
            days_for_next_arrival -= 1
            
        if days_for_next_arrival == 0:
            new_ship = Ship(select_with_weight(SHIP_TYPE_OPTIONS, SHIP_TYPE_WEIGHTS))
            ship_queue.append(new_ship)
            # days_for_next_arrival = select_with_weight(DAYS_BETWEEN_ARRIVALS_OPTIONS, DAYS_BETWEEN_ARRIVALS_WEIGTHS)

            # print(days_for_next_arrival)

        ships_in_queue.append(len(ship_queue))
        for ship in ship_queue:
            ship.add_day()
        if len(ship_queue) > 0 and (remaining_A_days == 0 or remaining_B_days == 0):
            next_ship = ship_queue.pop(0)
            days_ship_waiting.append(next_ship.days_waiting)
            #print('pop', next_ship.type, ship.days_waiting)
            if remaining_B_days == 0:
                #print(' in B')
                ship_in_B = next_ship.type
                B_is_empty = False
                if ship_in_B == 'L':
                    remaining_B_days = 3
                if ship_in_B == 'M':
                    remaining_B_days = 2
                if ship_in_B == 'S':
                    remaining_B_days = 1
            elif remaining_A_days == 0:
                ship_in_A = next_ship
                A_is_empty = False
                #print(' in A')
                if ship_in_A == 'L':
                    remaining_A_days = 4
                if ship_in_A == 'M':
                    remaining_A_days = 3
                if ship_in_A == 'S':
                    remaining_A_days = 2
        
        if A_is_empty:
            empty_A_days += 1
        if empty_B_days:
            empty_B_days += 1
    
    print( empty_A_days, empty_B_days,
     sum(days_ship_waiting)/float(len(days_ship_waiting)), sum(ships_in_queue)/float(simulation_days))


def n_simulations(n):
    for i in range(n):
        simulate_ships()

if __name__ == "__main__":
    print("A B promedioA promedioB")
    n_simulations(1000)

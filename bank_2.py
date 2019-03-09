from generador import select_with_weight
import numpy as np

class cliente:
    def __init__(self):
        self.time_waiting = 0

    def wait(self):
        self.time_waiting += 1

class cajero:
    def __init__(self):
        self.time_doing_nothing = 0
        self.busy = False
        self.time_to_end = 0
        self.talking_to = None

    def is_busy(self):
        return self.busy

    def serving(self, client):
        self.begins()
        self.busy = True
        self.talking_to = client

    def is_working(self):
        self.time_to_end -= 1
        if self.time_to_end == 0:
            x = self.talking_to
            self.talking_to = None
            self.busy = False
            return x

        return None

    def wait(self):
        self.time_doing_nothing += 1

    def begins(self):
        self.time_to_end =np.floor(np.random.uniform(3,6))

def simulate_tellers(hours):
    #CReamos nuestra listas
    cola = []
    finished = []
    never_queued = []


    teller_1 = cajero()
    teller_2 = cajero()
    teller_3 = cajero()
    teller_4 = cajero()

    tellers = [teller_1,teller_2, teller_3, teller_4]
    queue = [[],[],[],[]]



    time_in_minutes = hours * 60

    time = 0

    for i in range(time_in_minutes):
        # 1 h = 60m
        # Time while be the probability of a person in minutes
        # /60

        
        time = time + np.random.exponential(1)

        # How much people we add
        people_to_add = 0
        while time > 1:
            time = time - 1
            people_to_add += 1

        for j in range(people_to_add):
            cola = pick_teller(queue)
            if len(cola) < 6:
                cola.append(cliente())
            elif 6 <= len(cola) <= 8:
                x = select_with_weight(["leave", "stay"], [0.20,0.80])
                if x == "stay":
                    cola.append(cliente())
                else:
                    never_queued.append(cliente())
            elif 9 <= len(cola) <= 10:
                x = select_with_weight(["leave", "stay"], [0.40,0.60])
                if x == "stay":
                    cola.append(cliente())
                else:
                    never_queued.append(cliente())
            elif 11 <= len(cola) <= 14:
                x = select_with_weight(["leave", "stay"], [0.60,0.40])
                if x == "stay":
                    cola.append(cliente())
                else:
                    never_queued.append(cliente())
            else: 
                x = select_with_weight(["leave", "stay"], [0.80,0.20])
                if x == "stay":
                    cola.append(cliente())
                else:
                    never_queued.append(cliente())
        

        for i in range(len(tellers)):
            if not tellers[i].is_busy():
                tellers[i].wait()
                if len(queue[i]) != 0:
                    tellers[i].serving(queue[i].pop())
            else:
                client = tellers[i].is_working()
                if client:
                    finished.append(client)

        for cola in queue:
            for clients in cola:
                clients.wait()

    return (tellers, finished, never_queued)


def simulate_n_tellers(n):
    print("tiempo_espera %clientes_declinan %cajero0 %cajero1 %cajero2 %cajero3")
    for i in range(n):
        (tellers, finished, never_queued) = simulate_tellers(8)
        tiempo_espera = sum(clients.time_waiting for clients in finished)/len(finished)
        total_clientes = len(finished) + len(never_queued)
        clientes_declinan = (len(never_queued)/total_clientes)*100
        cajero0 = (tellers[0].time_doing_nothing/(8*60))*100
        cajero1 = (tellers[1].time_doing_nothing/(8*60))*100
        cajero2 = (tellers[2].time_doing_nothing/(8*60))*100
        cajero3 = (tellers[3].time_doing_nothing/(8*60))*100
        print(tiempo_espera, clientes_declinan, cajero0, cajero1, cajero2, cajero3)

def pick_teller(cola):
    minimo = min(len(x) for x in cola)
    for x in cola:
        if len(x) == minimo:
            return x




if __name__ == "__main__":
    simulate_n_tellers(1000)

        






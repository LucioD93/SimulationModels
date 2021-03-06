import random
import datetime

def random_0_1():
    random.seed(datetime.datetime.now())
    return random.uniform(0,1)

def select_any(options):
    random.seed(datetime.datetime.now())
    return random.choice(options)

# options: Array of the options
# weights: Array of the weights
def select_with_weight(options, weights):
    # assert(len(options) == len(weights))
    # assert(sum(weights) == 1 or sum(weights) == 1.0)
    distribution = [0]
    total = 0

    for i in weights:
        distribution.append(total + i)
        total += i
    
    r = random_0_1()

    # print(distribution)
    # print(r)

    for i in distribution:
        if i > r:
            # print(options[distribution.index(i)-1])
            return options[distribution.index(i)-1]

def random_uniform_range(min, max):
    return (random_0_1()*(max-min) + min)
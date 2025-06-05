def Sandwiches(*arg):
    lst=[*arg]
    for i in lst :
        print(f"I'm adding {i} in your sandwich")
    print('Your sandwich is ready.ENJOY !')

Sandwiches('gems','cheese','tomato','salad')
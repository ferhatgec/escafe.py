from escafe import escafe

with open('example.txt', 'r') as data:
    for line in data:
        print(end=escafe.run(line))

import random
correct_wire=random.randint(1,5)
a=int(input("Choose a wire to cut(1-5): "))
if a==correct_wire:
    print("Bomb defused!")
else:
    print("Boom! That was the wrong wire. It was wire ",correct_wire)

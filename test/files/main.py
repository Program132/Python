# Quand un message est envoyé

lines = []

with open('bdd.txt', 'r') as file:
    lines = file.readlines()
    file.close()


# Système de affichage de xp

found = False

for line in lines:
    line = line.strip()
    args = line.split()

    if args[0] == "JoJoS":
        print(args[1])
        found = True
        break
    
if not found:
    file = open('bdd.txt', 'w')

    for line in lines:
        file.write(line)
    file.write('\nText non trouve')

    file.close()
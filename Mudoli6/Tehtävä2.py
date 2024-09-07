import random
def heita_nappaa(faces):
    return random.randint(1, faces)
faces = int(input("Enter the number of faces on the dice: "))
i = 0
while i < faces:
    i = heita_nappaa(faces)
    print(i)

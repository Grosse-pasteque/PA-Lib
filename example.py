import PA_Lib
from random import randint

def random_meet(): return f"{randint(2, 5)}x meet"
cow = PA_Lib.Percent()
cow.add(50, random_meet)
cow.add(30, "some leather")
cow.add(20, "nothing -_-")
print(cow['constants'])

chiken = PA_Lib.Percent()
config = {
    40: "chiken",
    30: "feather",
    10: "chiken leg",
    20: "chiken egg"
}
chiken.setdirect(config)

animals = PA_Lib.Group(name="animals", version='0.0.1', description="some animals maybe for a game...")
animals.add(cow, name="cow")
animals.add(chiken, name="chiken")

random_animal, animal_name = animals.randgroup(return_choice=True)
print(f"You have obtained {random_animal.randperct()} from {animal_name}")



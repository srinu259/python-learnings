from m13_prescription_data import adverse_interactions

# unions are commutative, just like addition and multiplication
# 2 + 4 = 4 + 2, 2 * 4 = 4 * 2
farm_animals = {"cow", "dog", "sheep", "horse", "cat"}
wild_animals = {"tiger", "elephant", "sheep", "horse", "fox"}

all_animals_1 = farm_animals.union(wild_animals)
all_animals_2 = wild_animals.union(farm_animals)
all_animals_3 = farm_animals | wild_animals

print(all_animals_1)
print(all_animals_2)
print(all_animals_3)

# union-update-example
# union update operation is a efficient way to union two sets
# this is because you append values to existing union, instead of creating a new union everytime
meds_to_watch = set()
for interactions in adverse_interactions:
    # meds_to_watch = meds_to_watch.union(interactions)
    # meds_to_watch = meds_to_watch | interactions
    meds_to_watch.update(interactions)
    # meds_to_watch |= interactions
print(sorted(meds_to_watch))

meds_to_watch.clear()
# update takes iterable as input, so the code can further be simplified as
meds_to_watch.update(*adverse_interactions)
print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep='\n')


# create a set of things that bite or things that sting
# snakes and spiders bite, scorpions and vespas sting
scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellowjacket", "hornet", "paper wasp"}

bite = snakes.union(scorpions)
sting = spiders.union(vespas)
bite_or_sting = bite.union(sting)
bite_or_sting.clear()
bite_or_sting.update(bite, sting)
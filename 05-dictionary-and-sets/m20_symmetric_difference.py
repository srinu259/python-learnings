morning = {"Python", "Java", "C", "C#", "SQL"}
evening = {"Lisp", "C", "C#", "SQL", "Java"}

# symmetric difference is values in A and values in B, but not in both
# (A - B) U (B - A)
print(morning ^ evening)
print(morning.symmetric_difference(evening))

mor_eve = morning - evening
eve_mor = evening - morning
mor_n_eve = mor_eve | eve_mor
print(mor_n_eve)
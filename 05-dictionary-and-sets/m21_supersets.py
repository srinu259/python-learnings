animals = {"lion", "elephant", "kingfisher", "penguin", "eagle", "fox"}
birds = {"kingfisher", "penguin", "eagle"}

print(birds.issubset(animals))
print(animals.issuperset(birds))
print(birds <= animals)
print(birds < animals)
print(animals >= birds)
print(animals > birds)

required_skills = {"python", "oracle", "linux"}
candidates = {
    "annie": {"java", "aws", "python", "azure", "linux", "oracle"},
    "bob": {"python", "linux", "oracle"},
    "carol": {"c", "aws", "python", "azure", "linux", "oracle"},
    "daniel": {"java", "c#", "python", "azure", "linux", "oracle"},
    "ekani": {"java", "aws", "c", "azure", "linux", "oracle"},
    "fena": {"java", "aws", "python", "azure", "c#", "oracle"}
}

# include perfect subset
selected_candidates = set()
for candidate, skills in candidates.items():
    if skills >= required_skills:
        selected_candidates.add(candidate)
print(f"Candidates selected for interview: {selected_candidates}")

# exclude perfect subset
selected_candidates.clear()
for candidate, skills in candidates.items():
    if skills > required_skills:
        selected_candidates.add(candidate)
print(f"Candidates selected for interview: {selected_candidates}")
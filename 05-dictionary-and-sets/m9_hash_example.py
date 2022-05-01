import hashlib
import codecs

data = [
    ("orange", "a sweet, orange and citrus fruit"),
    ("apple", "an apple a day keeps doctor away"),
    ("lemon", "a small yellow sour tasty"),
    ("grape", "a small and sweet fruit")
]


def get_hash(s: str) -> int:
    """
    a simple `hash` function
    :param s: a single char string to get ascii value
    :return:
    """
    return ord(s[0]) % 10


def get_value(k: str) -> str:
    """
    returns the value from list if it exists else none
    :param k: key to check for
    :return: value from the list
    """
    hash_code = get_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


keys = [""]*10
values = keys.copy()
# ord - ordinal
print(ord("a"))
for key, value in data:
    simple_hash = get_hash(key)
    print(key, simple_hash, hash(key))
    keys[simple_hash] = key
    values[simple_hash] = value

print(keys)
print(values)
print(get_value("orange"))
print(get_value("tomato"))

print()
print(" --- Hash demonstration --- ")
a_program = "for i in range(10)" \
            "print(i)"
print(a_program.encode("utf-8"))
a_program_hash = hashlib.sha256(a_program.encode("utf-8"))
print(f"Original code SHA256: {a_program_hash.hexdigest()}")

a_program = "some new code"
a_new_program_hash = hashlib.sha256(a_program.encode("utf8"))
print(f"Modified code SHA256: {a_new_program_hash.hexdigest()}")

if a_program_hash.hexdigest() == a_new_program_hash.hexdigest():
    print("Code didn't change")
else:
    print("Code has changed")

print()
a_program = "for i in range(10)" \
            "print(i)"
print(a_program.encode("utf-8"))
a_new_program_hash = hashlib.sha256(a_program.encode("utf-8"))
print(f"Revert to original code SHA256: {a_new_program_hash.hexdigest()}")
if a_program_hash.hexdigest() == a_new_program_hash.hexdigest():
    print("Code didn't change")
else:
    print("Code has changed")

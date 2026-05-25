#   Count vowels and consonants in a sentence
sentence = "Loops are Fun!"
vowels = "aeiou"
v_count = 0
c_count = 0

for char in sentence.lower():
    if char.isalpha:
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print(f"Vowels: {v_count}")
print(f"Consonants: {c_count}")
"""Exercise 12. Count vowels and consonants in a sentence"""
str_original = "Loops are Fun!"
vowels = "aeiou"
vowels_count = 0
consonant_counts = 0

for item in str_original.lower():
    if item.isalpha():
        if item in vowels:
            vowels_count += 1
        else:
            consonant_counts += 1
print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonant_counts}")

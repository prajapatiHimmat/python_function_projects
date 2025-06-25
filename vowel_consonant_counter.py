print("Welcome to the vowel & consonant counter!\n")

text = input("Enter a sentence :").lower()

vowels = 0
consonants = 0 

vowel_letters = "aeiou"

for ch in text:
    if ch.isalpha():
        if ch in vowel_letters:
            vowels += 1 
        else: 
            consonants += 1

print(f"\nTotal Vowels:{ vowels}")
print(f"Total Consonant: {consonants}")
print("No tension number, space, symbol all things ki not count")
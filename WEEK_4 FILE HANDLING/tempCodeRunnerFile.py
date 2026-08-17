text = "programming"
vowel = "aeiou"
count = 0
for i in text:
    if i in vowel:
        count = count + 1
print(count)
if count == 0:
    print("No vowels in text")
characterCount = 0
wordCount = 1
var = input("Enter The senctence: \n")

for i in var:
    characterCount += 1
    var = var.strip()
    if i == ' ':
        wordCount += 1  # compund assignment
        wordCount = wordCount


print(characterCount)
print(wordCount)

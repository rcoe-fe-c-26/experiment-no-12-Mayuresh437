# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder: Mayuresh
# Date: 14-02-2026

print("--- Extracting Words from Text File ---\n")
num = int(input("Enter Length of Words: "))
result=[]
with open("story.txt") as file:
    content = file.read().split()
    
    for words in content:
        if len(words) ==num:
            result.append(words)
    print(f"Words with length {num} are {result}")

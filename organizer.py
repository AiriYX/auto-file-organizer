import os
import re

# Step 1: List everything in a directory
directory = "/Users/yweng/Documents/"
listOfDirectory = os.listdir(directory)

# print(f"Here is the list of directories -->", listOfDirectory)

# Step 2: List out only files
filesInDirectory = [file for file in listOfDirectory if os.path.isfile(os.path.join(directory, file))]

print(f"Here is the files in this directory: ", filesInDirectory)

# Step 3: Extract keyword from filenames using dictionary
for file in filesInDirectory:
    splitWords = re.findall(r'\b\w+\b', file)
    print(splitWords)

# Use dictionary to store the keywords and the occurances
word_counts = {}
for word in splitWords:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

appearedTwice = [key for key in word_counts if word_counts[key] > 1]

for key,value in word_counts.items():
    print(key)

# now that we know there is two that has more than 1 appearance, we can group them up

grouped_files = {}
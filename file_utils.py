#organizing, moving, grouping
import os, re, shutil

def organize_files(directory):
    # Step 1: List everything in a directory
    dir_ = "/Users/yweng/Documents/"
    listOfDirectory = os.listdir(dir_)

    # print(f"Here is the list of directories -->", listOfDirectory)

    # Step 2: List out only files
    filesInDirectory = [file for file in listOfDirectory if os.path.isfile(os.path.join(dir, file))]

    print(f"Here is the files in this directory: ", filesInDirectory)
    # This will track the occurences already
    word_counts = {}  
    # Stores words associated with each file instead of rewriting the var split words over and over again
    file_word_map = {}

    # Step 3: Extract keyword from filenames using dictionary
    for file in filesInDirectory:
        splitWords = re.findall(r'\b\w+\b', file) #extract indivual words
        file_word_map[file] = splitWords # Stores words for this file indiviually

        for word in splitWords:
            word_counts[word] = word_counts.get(word, 0) + 1 
        print(splitWords)


    for key,value in word_counts.items():
        print("This is the key: ", key, end=" | ")
        print("This is the value: ", value)

    # now that we know there is two that has more than 1 appearance, we can group them up
    grouped_files = {}
    for file, words in file_word_map.items():
        for word in words:
                if word_counts[word] > 1:
                    grouped_files.setdefault(word, []).append(file)

    #grouped result:
    for key,files in grouped_files.items():
        print(f"Keyword '{key}' is found in {files}")

    # Creating directory with 



    if not os.path.exists(directory):
        print("Invalid directory.")
        return


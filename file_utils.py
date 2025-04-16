import os, re, shutil

def organize_files(dir_, allow_extensions=False):
    # Step 1: List everything in a directory
    # dir_ = "/Users/yweng/Documents/"
    listOfDirectory = os.listdir(dir_)

    # print(f"Here is the list of directories -->", listOfDirectory)
    # validating directory
    if not os.path.exists(dir_):
        print("Invalid directory.")
        return
    
    # Step 2: List out only files
    filesInDirectory = [file for file in listOfDirectory if os.path.isfile(os.path.join(dir_, file))]

    print(f"Here is the files in this directory: ", filesInDirectory)
    # This will track the occurences already
    word_counts = {}  
    # Stores words associated with each file instead of rewriting the var split words over and over again
    file_word_map = {}

    # Step 3: Extract keyword from filenames using dictionary
    ignore_words = set() if allow_extensions else {"pdf", "txt", "docx", "pptx"}
    
    for file in filesInDirectory:
        splitWords = re.split(r'[_\-\.\s]', file.lower()) #extract indivual words
        file_word_map[file] = splitWords # Stores words for this file indiviually

        for word in splitWords:
            word_counts[word] = word_counts.get(word, 0) + 1 

    # now that we know there is two that has more than 1 appearance, we can group them up
    grouped_files = {}
    for file, words in file_word_map.items():
        for word in words:
            if word_counts[word] > 1 and word not in ignore_words:
                grouped_files.setdefault(word, []).append(file)

    # Creating directory with keywords and moving files
        #1. create a folder named after the keyword
        #2. move each associat3ed file into that folder

    for keyword, files in grouped_files.items():
        folder_path = os.path.join(dir_, keyword)
        os.makedirs(folder_path, exist_ok=True) # if the folderpath exists, then create a directory

        for file in files:
            source_path = os.path.join(dir_, file)
            destination_path = os.path.join(folder_path, file)

            try:
                shutil.move(source_path, destination_path)
                print(f"Moved '{file}' to '{keyword}/'")
            except FileNotFoundError:
                print(f"File '{file}' not found. Skipping.")

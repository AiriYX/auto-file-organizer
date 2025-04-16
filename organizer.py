# command-line logic, main script
#!/usr/bin/env/ python3
from file_utils import organize_files

if __name__ == "__main__":
    import argparse # what does this do? (helps accept command-line arguments fromm the terminal)

    parser = argparse.ArgumentParser(description = "Sort files by keyword grouping.")
    parser.add_argument("command", help="Type 'sort' to organize your current directory.")
    parser.add_argument("directory", help="Path to the directory you want to organize.")
    args = parser.parse_args()

    if args.command == "tidyup":
        organize_files(args.directory)
    else:
        print("Unknown command. Please use 'tidyup'.")
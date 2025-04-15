# command-line logic, main script
from file_utils import organize_files

if __name__ == "__main__":
    import argparse # what does this do?

    parser = argparse.ArgumentParser(description = "Sort files by keyword grouping.")
    parser.add_argument("command", help=="Type 'sort' to organize your current directory.")
    args = parser.parse.args()

    if args.command == "sort":
        organize_files("args.directory")

# Auto File Organizer 📂

A Python script that programmatically organizes files in a specified directory based on detected keyword patterns in filenames. It uses regular expressions to parse filenames, identifies recurring substrings, and moves files into categorized folders accordingly.

## ✨ Features

- Parses filenames using regular expressions to detect recurring keywords
- Aggregates keyword frequency and dynamically creates folder structures
- Moves files into corresponding directories based on matched patterns
- Supports multiple file formats (.pdf, .txt, .docx, etc.)
- Built for macOS with easily configurable cross-platform compatibility

## ⚙️ Usage

1. Clone the repository:

   ```
   git clone https://github.com/your-username/auto-file-organizer.git
   cd auto-file-organizer
   ```

2. Rename the main script to `tidyup` and make it executable:

   ```
   mv tidyup.py tidyup
   chmod +x tidyup
   ```

3. Add a shebang to the top of the file if it's not already there:

   ```
   #!/usr/bin/env python3
   ```

4. Run the script from the terminal:

   ```
   ./tidyup
   ```

5. What happens under the hood:
   - The script scans the target directory and retrieves all filenames.
   - It uses regular expressions to tokenize filenames into substrings.
   - It counts the frequency of each token across all files.
   - High-frequency keywords are used as labels for folder creation.
   - Files are moved into the appropriate folder(s) based on matched keywords.

## 🚀 Future Improvements

- Implement real-time **auto-sorting** when new files are added
- Add **GUI support** for drag-and-drop file organization
- Extend compatibility for **Windows & Linux**

## 🔒 License

This project is licensed under the MIT No Redistribution License. This means you may view and reference the code for personal and demonstration purposes only. Redistribution, commercial use, or modification without permission is strictly prohibited. See the LICENSE file for full terms.

# Auto File Organizer 📂

A Python script that programmatically organizes files in a specified directory based on detected keyword patterns in filenames. It uses regular expressions to parse filenames, identifies recurring substrings, and moves files into categorized folders accordingly.

## ✨ Features

- Parses filenames using regular expressions to detect recurring keywords
- Aggregates keyword frequency and dynamically creates folder structures
- Moves files into corresponding directories based on matched patterns
- Supports multiple file formats (.pdf, .txt, .docx, etc.)
- Built for macOS with easily configurable cross-platform compatibility

## 📌 How It Works

1. Scans the target directory and retrieves all filenames.
2. Uses regular expressions to tokenize filenames into substrings.
3. Counts the frequency of each token across all files.
4. Identifies high-frequency keywords as categorization labels.
5. Creates folders named after these keywords.
6. Moves files into folders based on which keyword(s) their filenames contain.

## 🚀 Future Improvements

- Implement real-time **auto-sorting** when new files are added
- Add **GUI support** for drag-and-drop file organization
- Extend compatibility for **Windows & Linux**

## 🔒 License

This project is licensed under the MIT No Redistribution License. This means you may view and reference the code for personal and demonstration purposes only. Redistribution, commercial use, or modification without permission is strictly prohibited. See the LICENSE file for full terms.

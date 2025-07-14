# BookBot - Text Analysis Tool

## Project Overview

This project is a command-line tool built in Python that provides a basic analysis of a text file. As my first guided project, its primary goal was to establish a solid foundation in Python fundamentals, including file I/O, string manipulation, and working with data structures like dictionaries and lists.

The program takes a path to a text file (such as a book from Project Gutenberg) as input and generates a report detailing the total word count and a frequency analysis of every alphabetic character in the text.

## Key Features

* **File I/O:** Reads the full content of a specified text file.
* **Word Count:** Calculates the total number of words in the document.
* **Character Frequency Analysis:** Counts the occurrences of each alphabetic character, case-insensitively.
* **Report Generation:** Presents a clean, sorted report in the console that summarizes the analysis.

## How It Works

The script executes the following steps:

1.  Accepts a path to a text file as a command-line argument.
2.  Reads the file content into memory.
3.  Splits the text into words to get a total word count.
4.  Converts all text to lowercase and iterates through the content to count the frequency of each alphabetic character.
5.  Generates and prints a detailed report to the console, showing the total word count followed by the character frequency list, sorted from most to least common.

## How to Run

To run the analysis on a text file, use the following command from the root of the project:

```bash
python3 src/main.py path/to/your/book.txt
```

Replace `path/to/your/book.txt` with the actual path to the text file you wish to analyze.

---

*This project was built as part of the backend development curriculum on [Boot.dev](https://www.boot.dev).*

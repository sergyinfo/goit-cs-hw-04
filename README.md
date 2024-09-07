
# Parallel Text File Keyword Search

This project provides a simple solution to search for specific keywords in text files using both multithreading and multiprocessing. The goal is to compare the performance and implementation of these two parallel processing techniques.

## Project Structure

```
/project_directory
    /files                   # Directory where generated text files will be stored
    /scripts                  # Contains the main scripts for the project
        common.py             # Common module with shared functions (e.g., file generation, searching)
        generate_test_files.py  # Script to generate test files for search
        search_threading.py    # Multithreading keyword search
        search_multiprocessing.py  # Multiprocessing keyword search
    README.md                 # Documentation
```

## Features

- **Multithreading**: Search for keywords in files using threads.
- **Multiprocessing**: Search for keywords in files using processes for better CPU-bound task handling.
- **Test File Generation**: Easily generate multiple text files with random content, including optional random keyword insertion for testing purposes.

## Requirements

- **Python 3.6+**
- **Required modules**:
  - `argparse`
  - `os`
  - `random`
  - `string`
  - `threading`
  - `multiprocessing`

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd project_directory
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install any required dependencies** (if using additional modules):
   ```bash
   pip install -r requirements.txt  # If necessary
   ```

4. **Ensure the `files` directory exists**:
   The scripts expect a `files` directory where text files will be generated and searched. If it doesn't exist, create it:
   ```bash
   mkdir files
   ```

## Usage

### 1. Generate Test Files

Before running the search scripts, you can generate random text files using `generate_test_files.py`:

```bash
python scripts/generate_test_files.py --dir ./files --num_files 10 --num_lines 100 --line_length 80 --keywords keyword1 keyword2
```

This command generates 10 random `.txt` files in the `./files` directory. Each file has 100 lines, each 80 characters long, with some files randomly containing `keyword1` or `keyword2`.

### 2. Run Multithreading Search

To search for keywords in text files using multithreading, run the following command:

```bash
python scripts/search_threading.py --dir ./files --keywords keyword1 keyword2
```

This will search for the specified keywords (`keyword1`, `keyword2`) in all `.txt` files in the `./files` directory, using multiple threads.

### 3. Run Multiprocessing Search

To search for keywords in text files using multiprocessing, run the following command:

```bash
python scripts/search_multiprocessing.py --dir ./files --keywords keyword1 keyword2
```

This will search for the specified keywords (`keyword1`, `keyword2`) in all `.txt` files in the `./files` directory, using multiple processes.

### Options

- **`--dir`**: Directory containing the text files. Default is `./files`.
- **`--keywords`**: Space-separated list of keywords to search for.

### Example

1. Generate 15 files with random text:
   ```bash
   python scripts/generate_test_files.py --dir ./files --num_files 15 --num_lines 50 --line_length 60 --keywords search find
   ```

2. Search the files using multithreading:
   ```bash
   python scripts/search_threading.py --dir ./files --keywords search find
   ```

3. Search the files using multiprocessing:
   ```bash
   python scripts/search_multiprocessing.py --dir ./files --keywords search find
   ```

## Performance Comparison

You can compare the performance of the two approaches by checking the execution time reported by both the multithreading and multiprocessing scripts. Generally, multiprocessing will perform better on CPU-bound tasks, while multithreading is more efficient for I/O-bound tasks.
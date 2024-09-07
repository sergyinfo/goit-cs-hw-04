import os
import random
import string
from typing import List, Dict, Optional, Union
import multiprocessing

def generate_random_text(num_lines: int, line_length: int) -> str:
    """
    Generates random text with a specified number of lines and characters per line.

    :param num_lines: Number of lines to generate
    :param line_length: Number of characters per line
    :return: Randomly generated text
    """
    text = []
    for _ in range(num_lines):
        line = ''.join(random.choices(string.ascii_lowercase + ' ', k=line_length))
        text.append(line)
    return '\n'.join(text)

def create_test_files(directory: str, num_files: int, num_lines: int, 
                      line_length: int, keywords: list) -> None:
    """
    Creates a specified number of test text files with random content.

    :param directory: Directory to store the files
    :param num_files: Number of files to create
    :param num_lines: Number of lines in each file
    :param line_length: Number of characters in each line
    :param keywords: List of keywords to randomly insert into some files
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(num_files):
        file_name = os.path.join(directory, f"test_file_{i+1}.txt")
        content = generate_random_text(num_lines, line_length)

        # Randomly insert a keyword in some files
        if random.choice([True, False]):
            keyword = random.choice(keywords)
            insertion_point = random.randint(0, num_lines - 1)
            lines = content.split('\n')
            lines[insertion_point] += f" {keyword}"
            content = '\n'.join(lines)

        with open(file_name, 'w') as f:
            f.write(content)

    print(f"Generated {num_files} test files in directory '{directory}'")

def get_files_from_directory(directory: str) -> List[str]:
    """
    Returns a list of text files from the specified directory.

    :param directory: Directory to search for text files
    :return: List of file paths in the directory
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f)) 
            and f.endswith('.txt')]

def search_keywords_in_file(file_path: str, keywords: List[str], 
                            results: Optional[Dict[str, List[str]]] = None,
                            queue: Optional[multiprocessing.Queue] = None) -> None:
    """
    Searches for the specified keywords in a file and either updates a results dictionary
    or sends the result via a multiprocessing queue.

    :param file_path: Path to the file to be searched
    :param keywords: List of keywords to search for
    :param results: Dictionary to store results (for threading or main process)
    :param queue: Queue to send results back to the main process (for multiprocessing)
    """
    result = {keyword: [] for keyword in keywords}

    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()
            for keyword in keywords:
                if keyword.lower() in content:
                    result[keyword].append(file_path)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

    # If using multiprocessing, pass results via queue
    if queue is not None:
        queue.put(result)
    # Otherwise, update the results dictionary directly
    elif results is not None:
        for keyword, files in result.items():
            results[keyword].extend(files)
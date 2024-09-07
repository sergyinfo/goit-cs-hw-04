import threading
import time
import argparse
from typing import List, Dict
from common import get_files_from_directory, search_keywords_in_file

# Function to process multiple files using multithreading
def process_files_threaded(file_paths: List[str], keywords: List[str]) -> Dict[str, List[str]]:
    """
    Processes files using multiple threads, each thread searching for keywords in one file.
    """
    results = {keyword: [] for keyword in keywords}
    threads = []

    # Create and start a thread for each file
    for file_path in file_paths:
        thread = threading.Thread(target=search_keywords_in_file, 
                                  args=(file_path, keywords, results, None))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return results

if __name__ == "__main__":
    # Command-line argument parser
    parser = argparse.ArgumentParser(description="Search keywords in files (Threading)")
    parser.add_argument('--dir', default='./files', help="Directory containing text files to process")
    parser.add_argument('--keywords', nargs='+', required=True, help="Keywords to search for")

    args = parser.parse_args()

    # Gather files from the specified directory
    file_paths = get_files_from_directory(args.dir)

    # Measure execution time
    start_time = time.time()
    results = process_files_threaded(file_paths, args.keywords)
    end_time = time.time()

    print("Results:", results)
    print(f"Threading Version took {end_time - start_time} seconds")

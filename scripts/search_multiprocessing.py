import multiprocessing
import time
import argparse
from typing import List, Dict
from common import get_files_from_directory, search_keywords_in_file

# Function to process multiple files using multiprocessing
def process_files_multiprocessing(file_paths: List[str], keywords: List[str]) -> Dict[str, List[str]]:
    """
    Processes files using multiple processes, each process searching for keywords in one file.
    """
    manager = multiprocessing.Manager()
    queue = manager.Queue()
    processes = []

    # Create and start a process for each file
    for file_path in file_paths:
        process = multiprocessing.Process(target=search_keywords_in_file, 
                                          args=(file_path, keywords, None, queue))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    # Gather results from the queue
    results = {keyword: [] for keyword in keywords}
    while not queue.empty():
        file_result = queue.get()
        for keyword in keywords:
            results[keyword].extend(file_result[keyword])

    return results

if __name__ == "__main__":
    # Command-line argument parser
    parser = argparse.ArgumentParser(description="Search keywords in files (Multiprocessing)")
    parser.add_argument('--dir', default='./files', help="Directory containing text files to process")
    parser.add_argument('--keywords', nargs='+', required=True, help="Keywords to search for")

    args = parser.parse_args()

    # Gather files from the specified directory
    file_paths = get_files_from_directory(args.dir)

    # Measure execution time
    start_time = time.time()
    results = process_files_multiprocessing(file_paths, args.keywords)
    end_time = time.time()

    print("Results:", results)
    print(f"Multiprocessing Version took {end_time - start_time} seconds")

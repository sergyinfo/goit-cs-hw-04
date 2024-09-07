import argparse
from common import create_test_files

if __name__ == "__main__":
    # Command-line argument parser
    parser = argparse.ArgumentParser(description="Generate test files with random content")
    parser.add_argument('--dir', default='./files', help="Directory to store generated files")
    parser.add_argument('--num_files', type=int, default=10, help="Number of files to generate")
    parser.add_argument('--num_lines', type=int, default=100, help="Number of lines per file")
    parser.add_argument('--line_length', type=int, default=80, help="Number of characters per line")
    parser.add_argument('--keywords', nargs='+', default=['keyword1', 'keyword2'], 
                        help="List of keywords to randomly insert into some files")

    args = parser.parse_args()

    # Generate test files using the common function
    create_test_files(args.dir, args.num_files, args.num_lines, args.line_length, args.keywords)

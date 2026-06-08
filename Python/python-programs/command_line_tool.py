import argparse
import os
import shutil


def move_file(source, destination):
    shutil.move(source, destination)
    print(f"Moved '{source}' to '{destination}'")


def delete_file(file_path):
    os.remove(file_path)
    print(f"Deleted '{file_path}'")


def main():
    parser = argparse.ArgumentParser(description="Simple command line tool to move or delete files")
    parser.add_argument("operation", choices=["move", "delete"], help="Operation to perform: move or delete")
    parser.add_argument("source", help="Source file path")
    parser.add_argument("destination", nargs="?", help="Destination file path (required for move operation)")

    args = parser.parse_args()

    if args.operation == "move":
        if not args.destination:
            parser.error("Destination file path is required for move operation")
        move_file(args.source, args.destination)
    elif args.operation == "delete":
        delete_file(args.source)


if __name__ == "__main__":
    main()

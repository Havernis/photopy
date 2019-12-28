# -*- coding: utf-8 -*-

"""Main module."""

from scanner import *
from database import *
from executor import *
import argparse
import os


DB_NAME = "PHOTOPY.DB"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help="Path to root folder")
    parser.add_argument('-d', '--database', help="Path to database (will be created if not existing)")
    parser.add_argument('-a', '--action', help="action to do - 'move' or 'delete'")  # implement a default or not a must value
    parser.add_argument('-f', '--folder', help="Path to duplicated folder")
    args = parser.parse_args()
    root_path = os.path.abspath(args.path)
    db_path = os.path.abspath(args.database)
    action = args.action
    duplicated_folder = args.folder
    print(f"Root path: {root_path}\nDatabase path: {db_path}")

    print(f"Creating/Connecting to database...", end='')
    db = Database(db_path)
    db.connect()
    db.cursor()
    if not db.table_exists():
        db.create_table()
    print("Success")

    print(f"Starting scan... Pounds (#) will be printed to show progress")
    scanner = Scanner(root_path)
    list_of_files = scanner.scan()
    print(f"\nFiles scanning completed, found total {len(list_of_files)} files")

    print(f"Populating files details into DB...")
    list_of_files_with_details = []
    for file in list_of_files:
        list_of_files_with_details.append(file.get_file_details())
        if len(list_of_files_with_details) == 1000:
            print('#', flush=True, end='')
            db.insert_records(list_of_files_with_details)
            list_of_files_with_details.clear()
    db.insert_records(list_of_files_with_details)
    print("\nCompleted")

    ordered_records = db.read_records()
    list_of_duplicates = scanner.scan_for_duplicates(ordered_records)
    # print(list_of_duplicates)
    if len(list_of_duplicates) != 0:
        exec = Executor()
        if exec.execute(list_of_duplicates, duplicated_folder, action):
            print(f"Duplicated files were {action}ed as requested")
        # What about else???
    else:
        print("Found no duplicated files, closing connections and script.")

    # ToDo:
    # Need to move the db connect, cursor, and close functions inside the class itself!
    db.close_cursor()
    db.close_connection()


if __name__ == "__main__":
    main()

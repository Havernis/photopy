# -*- coding: utf-8 -*-

"""Main module."""

from scanner import *
from database import *
import argparse
import os


DB_NAME = "PHOTOPY.DB"


def print_duplicates(ordered_records):
    clean_list = []
    for record in ordered_records:
        if len(clean_list) == 0:
            clean_list.append(record)
        elif record[2] == clean_list[-1][2]:
            print(f"Found duplicated files:\n{clean_list[-1]}\nfound in the clean list, and\n{record}")
        else:
            clean_list.append(record)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help="Path to root folder")
    parser.add_argument('-d', '--database', help="Path to database (will be created if not existing)")
    args = parser.parse_args()
    root_path = args.path
    db_path = args.database
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
    print("Completed")
    # ordered_records = db.read_records()
    # print_duplicates(ordered_records)

    db.close_cursor()
    db.close_connection()

# ToDo:
# Need to move the db connect, cursor, and close functions inside the class itself!


if __name__ == "__main__":
    main()

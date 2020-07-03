from __future__ import print_function
import csv
import os
import sys


def _csv_1():
    TEST_DATA_LIST = [["Bill", 40, 0], ["Alice", 42, 5],
                      ["Zane", 33, -1], ["Theodore", 72, 9001]]

    TEST_DATA_DICT = [{"Name": "Bill", "Age": 53, "Cool Factor": 0},
                      {"Name": "Alice", "Age": 42, "Cool Factor": 5},
                      {"Name": "Zane", "Age": 33, "Cool Factor": -1},
                      {"Name": "Theodore", "Age": 72, "Cool Factor": 9001}]
    def csv_writer_py2(data, header, output_directory, name=None):
        if name is None:
            name = "output.csv"

        print("[+] Writing {} to {}".format(name, output_directory))

        with open(os.path.join(output_directory, name), "wb") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)

            writer.writerows(data)
    def unicode_csv_dict_writer_py2(data, header, output_directory, name=None):
        try:
            import unicodecsv
        except ImportError:
            print("[+] Install unicodecsv module before executing this"
                  " function")
            sys.exit(1)
        if name is None:
            name = "output.csv"

        print("[+] Writing {} to {}".format(name, output_directory))
        with open(os.path.join(output_directory, name), "wb") as csvfile:
            writer = unicodecsv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()

            writer.writerows(data)
    def csv_writer_py3(data, header, output_directory, name=None):
        if name is None:
            name = "output.csv"

        print("[+] Writing {} to {}".format(name, output_directory))

        with open(os.path.join(output_directory, name), "w", newline="") as \
                csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)

            writer.writerows(data)
    if sys.version_info < (3, 0):
        csv_writer_py2(TEST_DATA_LIST, ["Name", "Age", "Cool Factor"],
                       os.getcwd())
        unicode_csv_dict_writer_py2(
            TEST_DATA_DICT, ["Name", "Age", "Cool Factor"], os.getcwd(),
            "dict_output.csv")
    elif sys.version_info >= (3, 0):
        csv_writer_py3(TEST_DATA_LIST, ["Name", "Age", "Cool Factor"],
                       os.getcwd())

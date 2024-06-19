#!/usr/bin/python3
"""This script is doing things"""
import sys
import re


status_dict = {}
counter = 0
all_file_size = 0
pattern = r'\"GET \/projects\/260 HTTP\/1\.1\"'


def dict_printer():
    """A printer to print, DUH"""
    print(f'File size: {all_file_size}')
    myKeys = list(status_dict.keys())
    myKeys.sort()
    sorted_dict = {i: status_dict[i] for i in myKeys}
    for key, value in sorted_dict.items():
        print(f'{key}: {value}')
    status_dict.clear()
    sorted_dict.clear()


try:
    for line in sys.stdin:
        if re.search(pattern, line):
            if counter == 10:
                dict_printer()
                counter = 0
            the_stuff_after_spliting = line.split(' ')
            status_code = the_stuff_after_spliting[7]
            try:
                status_code = int(status_code)
            except ValueError:
                status_code = None
            if status_code:
                if status_code not in status_dict:
                    status_dict[status_code] = 1
                else:
                    status_dict[status_code] = status_dict[status_code] + 1
            file_size = int(the_stuff_after_spliting[8])
            all_file_size = all_file_size + file_size
            counter = counter + 1
        else:
            continue
except KeyboardInterrupt:
    dict_printer()

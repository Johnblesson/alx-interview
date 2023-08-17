#!/usr/bin/python3

"""Script that reads stdin line by line and computes metrics"""

import sys

def print_statistics(statistics, total_size):
    """Prints information"""
    print("File size: {:d}".format(total_size))
    for status_code, count in sorted(statistics.items()):
        if count != 0:
            print("{}: {:d}".format(status_code, count))

statistics = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
              "404": 0, "405": 0, "500": 0}

total_count = 0
total_size = 0

try:
    for line in sys.stdin:
        if total_count != 0 and total_count % 10 == 0:
            print_statistics(statistics, total_size)

        tokens = line.split()
        total_count += 1

        try:
            size = int(tokens[-1])
            total_size += size
        except IndexError:
            pass
        except ValueError:
            pass

        try:
            status_code = tokens[-2]
            if status_code in statistics:
                statistics[status_code] += 1
        except IndexError:
            pass

    print_statistics(statistics, total_size)

except KeyboardInterrupt:
    print_statistics(statistics, total_size)
    raise

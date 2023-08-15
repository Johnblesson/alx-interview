#!/usr/bin/python3
"""Log Parser"""
import sys

def parse_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None

def print_statistics(total_size, status_counts):
    print(f"Total file size: {total_size}")
    for code, count in sorted(status_counts.items()):
        print(f"File size {code}: {count}")

def main():
    total_size = 0
    status_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_line(line.strip())
            if ip_address is not None:
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1

                line_count += 1

            if line_count == 10:
                print_statistics(total_size, status_counts)
                line_count = 0

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()

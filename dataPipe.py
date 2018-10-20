import concurrent.futures
import glob
import csv
from datetime import datetime
startTime = datetime.now()


def find_title(column):
    if 'engineer' in column:
        print(column)


def open_file(file):
    with open(file, 'r', encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[8]:
                find_title(row[8])


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        files = glob.glob("*.csv")
        executor.map(open_file, files)
    print(datetime.now() - startTime)


if __name__ == '__main__':
    main()

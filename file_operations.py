import csv

filename = 'note1.csv'
with open(filename) as f:
    reader = csv.reader(f, delimiter = ";") 
    # header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    for row in reader:
        print(row)


def read_file():
    # take header 
    # edit body
    print()
    
def write_file():
    # header 
    # body
    print()
    
def edit_file():
    # take header
    # edit body
    print()

def delete_file():
    # take header
    print()
    
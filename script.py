import pandas

pandas.set_option('display.max_columns',500) # useful for debugging

with open("data/indiv_header_file.csv") as f:
    headers = f.read().strip('\n').split(",")

types = {item: object for item in headers}  # passed in as types to

df = pandas.read_csv("data/itcont.txt", delimiter='|', names=headers, dtype=types)  # We will filter
                                                                                    # out specific types later

# TODO: use proper types and calculate total contributions by a specific person.
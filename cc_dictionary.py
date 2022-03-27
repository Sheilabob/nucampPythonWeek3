inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


""" def total_inches():
    accum = 0
    for inches in inches_snow.values():
        accum += inches
    print(f"Total snowfall inches:\t{accum}")


total_inches()
new_entry = input("How many inches of snow fell on Thursday?\t")
inches_snow["Thursday"] = int(new_entry)
total_inches() """


def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow:
        total_inches += inches_snow[inches]
    print(f"Total snowfall inches:\t{total_inches}")


print_total_snowfall(inches_snow)
new_entry = input("How many inches of snow fell on Thursday?\t")
inches_snow["Thursday"] = int(new_entry)
print_total_snowfall(inches_snow)

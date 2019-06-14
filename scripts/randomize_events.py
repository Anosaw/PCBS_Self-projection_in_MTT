"""
This script is used to randomize the order of events in the participant list

"""
import random
import csv

nb_events = 24

l = {}
i = 1

with open('documents/event_list.csv', encoding="utf-8") as events:
    r = csv.reader(events)
    next(r)  # skip header line
    for row in r:
        date, name = row[0], row[3]
        l.update({i : date + " : " + name})
        i += 1

nb = list(range(1 , nb_events + 1))
random.shuffle(nb)

for element in nb:
    print(l[element])

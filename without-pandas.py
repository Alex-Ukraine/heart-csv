import csv

import matplotlib.pyplot as plt


def to_match(age):
    if 25 <= age <= 34:
        return "25-34"
    elif 35 <= age <= 44:
        return "35-44"
    elif 45 <= age <= 54:
        return "45-54"
    elif 55 <= age <= 64:
        return "55-64"
    elif 65 <= age <= 74:
        return "65-74"
    elif 75 <= age <= 84:
        return "75-84"


reader = csv.reader(open('heart 1.csv'), delimiter=',')
next(reader)
result = []
dicty = dict()

for row in reader:
    if int(row[3]) >= 140:
        result.append(row)
        age = to_match(int(row[0]))
        if age in dicty:
            dicty[age][1] += 1
            dicty[age][0] += int(row[-1])
        else:
            dicty[age] = [int(row[-1]), 1]

for key, value in dicty.items():
    dicty[key] = value[0]/value[1]

dicty=sorted(dicty.items())

plt.title("Bar chart age range relate to average heartbeat")
plt.xlabel("age ranges")
plt.ylabel("average heartbeat")

plt.bar(*zip(*dicty))

if __name__ == '__main__':
    plt.show()

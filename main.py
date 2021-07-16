import matplotlib.pyplot as plt
import pandas as pd

result = pd.read_csv('heart 1.csv', delimiter=',')
result = result[result.thalachh >= 140]


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


result['diapazons'] = result['age'].apply(lambda x: to_match(x))

result = result.groupby('diapazons').thalachh.mean()
result.plot(kind='bar')

if __name__ == '__main__':
    plt.show()
    print(result.head())

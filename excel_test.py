import pandas as pd

data = {
    'Names':['Alice', 'Bob', 'Charlie'],
    'Math Scores': [80, 74, 45],
    'English Scores': [90, 88, 92],
}

df = pd.DataFrame(data)

df.to_excel('test_scores.xlsx', engine='openpyxl', index=False)

df = pd.read_excel('test_scores.xlsx', engine='openpyxl')

print('Data going into Excel')

print(df)

import pandas as pd

# create a sample DataFrame
df = pd.DataFrame({'text': ['The cat is on the mat.', 'The cat is in the hat.', 'The bat is on the mat.']})

# use the .str.replace() method to replace all occurrences of 'cat' with 'dog'
df['text'] = df['text'].str.replace('cat', 'dog')

# print the modified DataFrame
print(df)
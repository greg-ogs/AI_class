import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('credit_card.csv')

# Convert `CHECKING_ACCOUNT`, `EDUCATION`, and `MARRIAGE` to numerical representations
for column_name in ['CHECKING_ACCOUNT', 'EDUCATION', 'MARRIAGE']:
    df[column_name] = pd.factorize(df[column_name])[0]

# Print the updated dataframe
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

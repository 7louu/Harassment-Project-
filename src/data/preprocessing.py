import pandas as pd
import re
from pathlib import Path

DATASET_PATH = (
    Path(__file__).resolve().parent
    / "datasets"
    / "saifulislam7"
    / "cyberbullying-and-harassment-detection-using-ml"
    / "versions"
    / "1"
    / "Approach to Social Media Cyberbullying and Harassment Detection Using Advanced Machine Learning.csv"
)

df = pd.read_csv(DATASET_PATH)

# Display the first 10 rows of the DataFrame
print(df.head(10))

print(df.shape)
# Dataset contains 8452 rows and 3 columns Text, Label and Types

print(df.info())

print(df.isna().sum())
# The Type column cocntains 3627 null values and the label column contains 2 null values. Since the labels are supposeddly binary from
# the examples we saw 'Bullying' and 'Not Bullying' we can drop those two rows with null values or to conserve the data we can fill those two
# null values with 'Not Bullying'.

df['Label'] = df['Label'].fillna('Not Bullying')

print(f"Null values in 'Label' column: {df['Label'].isna().sum()}")
# This will print 0 since we no longer have any null values in the label column.

print(f"Unique values in 'Text' column: {df['Text'].nunique()}")

count = df['Label'].value_counts()
percentage = df['Label'].value_counts(normalize=True) * 100
imbalance_df = pd.DataFrame({'Count': count, 'Percentage': percentage})
print(f"Imbalance DataFrame:\n{imbalance_df}")
# I noticed something that the labels are written different thats why the counts are showing multiple entries
# for example : we have 'Not- Bullying';'Not-Bulyying' are being set as seperate labels.
# Let's make them binary

pattern = r'^Bull\w*'
df['Label'] = df['Label'].map(lambda x: '1' if re.search(pattern, x, re.IGNORECASE) else '0')
print(df['Label'].value_counts())
print(df.head(10))

# Since i'm working locally and not on colab i'm going to copy paste the entire imbalance code block
# to run it again after the changes we made
count = df['Label'].value_counts()
percentage = df['Label'].value_counts(normalize=True) * 100
imbalance_df = pd.DataFrame({'Count': count, 'Percentage': percentage})
print(f"Imbalance DataFrame:\n{imbalance_df}")
# Now there are 4834 rows with Label 1 (58% Bullying) and 3618 rows with Label 0 (43% Not Bullying)

print(f"Null values in 'Types' column: {df['Types'].isna().sum()}")
# There are 3627 null values in the types column which is 44% of the data so i'm going to drop this column for now.add()
df = df.drop(columns=['Types'])
print(f"New dataframe shape : {df.shape}")

# Now let's focus on the Text column and clean it up a bit, let's put it in lower case and remove whitespace
df['Text'] = df['Text'].str.strip()
df['Text'] = df['Text'].str.lower()
# I found some rows contain mentions of people accounts on social media like @username so let's remove them
df['Text'] = df['Text'].str.replace(r'@\w+', '', regex=True)
print(df.head(20))

print(f"Number of duplicated rows: {df.duplicated().sum()}")
# there are 2381 duplicated rows so let's drop them
df = df.drop_duplicates()
print(f"Number of duplicated rows: {df.duplicated().sum()}")
print(f"New dataframe shape after dropping duplicates: {df.shape}")
# The new shape is (6071, 2) of unique values the initial shape was (8452, 3) so we lost 2381 rows and the Types column. The new shape is (6071, 2) of unique values.

# I read in the dataset card that these comments were taken from social media i don't know if they're scraped or not but let's check
# if there are html tags in there
has_html = df['Text'].str.contains(r'<[^>]*>', regex=True).any()
print("Contains HTML:", has_html)
# Nice it returned False so we don't have to worry about that
# I think the current stage is not that bad, i'm going to save it since there are other steps to do. I'll be back if i noticed something else
# or needed to improve something.


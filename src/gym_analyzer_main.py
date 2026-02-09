#import the needed modules of pandas and numpy
import pandas as pd 
from data_cleaning import clean_dataset
from feature_engineering import feature_eng
from visualization import graphs


def main():
  #Main Execution block 
  df = pd.read_csv('gym_members_150_rows.csv', index_col='member_id')

  #checked the data was imported correctly and took a look at the data.
  #print(df.head())
  #print(df.shape)
  #print(df.info())
  #print(df.describe())
  #print(df.tail())
  #print(df.columns)
  #print(df.isna().sum())
  #print(df['age'].median())


  df = clean_dataset(df)
  df = feature_eng(df)
  graphs(df)
  #Save everything back to a new csv file
  df.to_csv('gym_members_cleaned&Engineered.csv', index=True)

if __name__ == "__main__":
    main()

#function to fill missing workout minutes
def fill_workout_minutes(df):
  #check to see if i should use median or mean for the avg workout minutes :

  #print(workout_days['avg_workout_minutes'].describe().T)
  #print(workout_days['avg_workout_minutes'].median())

  #turns out both were super close so there arent crazy outliers but i decided to use the median

  #fixed all NAN values from the avg workout time column.
  #used the median of the workout days per week grouped to get a good guess of avg workout minutes.
  days_median = df.groupby('workout_days_per_week')['avg_workout_minutes'].transform('median')
  df['avg_workout_minutes'] = df['avg_workout_minutes'].fillna(days_median)

  return df

#function to fill missing weights
def fill_missing_weight(df):
  #fix all the missing weight value by using avg based on height and the fitness goal 
  weight_median = df.groupby(['height_cm','goal'])['weight_kg'].transform('median')
  df['weight_kg'] = df['weight_kg'].fillna(weight_median)

  #fix missing weight for those that arent with goal using height
  #  because some heights have unique values and unique goals first clean still left some NAN values 
  weight_median2 = df.groupby(['height_cm'])['weight_kg'].transform('median')
  df['weight_kg'] = df['weight_kg'].fillna(weight_median2)

  #fix missing weight using only normal median for any nan that have unique heights so no median for them
  df['weight_kg'] = df['weight_kg'].fillna(df['weight_kg'].median())

  return df

#function to drop missing heights
def drop_missing_heights(df):
  #I have only 11 missing heights from 150 rows dataset. Height is harder than weights to predict or fill.
  # weight can not accuratley give me height so i will drop all rows with missing heights
  df = df.dropna(subset=['height_cm'])

  return df

#function to clean the dataset
def clean_dataset(df):
  df = fill_workout_minutes(df)
  df = fill_missing_weight(df)
  df = drop_missing_heights(df)

  return df

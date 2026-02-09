import numpy as np

# creates a new column called BMI
def add_bmi(df):
  df['bmi'] = df['weight_kg'] / ((df['height_cm'] / 100) ** 2)
  return df

#Creates a new column with bmi categorys 
def bmi_category(df):
 bmi_condition = [
    df['bmi'] < 18.5,
    (df['bmi'] >= 18.5) & (df['bmi'] < 25),
    (df['bmi'] >= 25) & (df['bmi'] < 30),
 ]
 bmi_categories = [
   "Underweight", 
   "Normal",
   "Overweight"
 ]
 df['bmi_category'] = np.select(bmi_condition, bmi_categories, default= "Obese" )

 return df

#creates a new column for activity
def activity(df):

  activity_conditions = [
    (df['workout_days_per_week'] > 0) & (df['workout_days_per_week'] <= 2), 
    (df['workout_days_per_week'] > 2) & (df['workout_days_per_week'] <= 4), 
    (df['workout_days_per_week'] >= 5) 
  ]
  act_category = [
    "low activity",
    "moderate activity",
    "high activity",
  ]

  df['activity'] = np.select(activity_conditions, act_category, default="No Training" )


  return df




#calls all the above functions
def feature_eng(df):
  df = add_bmi(df)
  df = bmi_category(df)
  df = activity(df)
  df['intensity'] = df['workout_days_per_week'] * df['avg_workout_minutes']

  return df
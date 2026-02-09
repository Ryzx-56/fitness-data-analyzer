import matplotlib.pyplot as plt
# Create the age and weight graph
def age_weight_graph(df):
  plt.scatter(df['age'],df['weight_kg'],
              alpha= 0.4,
              color= 'red',
              s = 30,
              edgecolors= 'black')

  plt.xlabel("Age")
  plt.ylabel("Weight in kg")
  plt.title("Age and weight")
  plt.savefig("Age_Weight_graph.png")
  plt.show()
  


# create the weight and height grapgh 
def weight_height_graph(df):
  plt.scatter(df['height_cm'], df['weight_kg'],
              alpha= 0.4,
              color= 'green',
              s = 30,
              edgecolors= 'black')

  plt.xlabel("Height in Cm")
  plt.ylabel("Weight in kg")
  plt.title("Height and weight")
  plt.savefig("weight_height_graph.png")
  plt.show()
  


# take the mean of the workout time for each goal than plot a bar graph 
def duration_goals(df):
  goal_mean = df.groupby('goal')['avg_workout_minutes'].mean()
  colors_plot1 = ['red' , 'black' , 'green']
  plt.bar(goal_mean.index, goal_mean,
          color = colors_plot1)
  plt.xlabel("Fitness Goals")
  plt.ylabel("Workout Time")
  plt.title("Workout Time and Goals")
  plt.savefig("duration_goals.png")
  plt.show()
  


#take the mean of the intensisty of each goal and then plot in a bar graph 
def goal_intensity(df):
  intensity_mean = df.groupby('goal')['intensity'].mean()
  colors_plot = ['cyan' , 'yellow' , 'orange']
  plt.bar(intensity_mean.index, intensity_mean, 
          color = colors_plot )
  plt.xlabel("Fitness Goals")
  plt.ylabel("Intensity")
  plt.title("Workout Intensity and Goals")
  plt.savefig("goal_intensity.png")
  plt.show()
  


#plot the age range on a histogram
def age_range(df):
  plt.hist(df['age'],
            rwidth=0.8,
            color = '#940899')
  plt.xlabel("Age")
  plt.title("Age Range")
  plt.savefig("age_range.png")
  plt.show()


# plot the duration and intensity on a scatter plot
def duration_intensity(df):
  plt.scatter(df['intensity'], df['avg_workout_minutes'], 
               alpha= 0.4,
              color= '#940609',
              s = 30,
              edgecolors= 'black')
  plt.xlabel("Intensity")
  plt.ylabel("Workout Duration ( Minutes)")
  plt.title("Duration and Intensity")
  plt.savefig("duration_intensity.png")
  plt.show()



#calls all the functions for the graphs
def graphs(df):
  age_weight_graph(df)
  weight_height_graph(df)
  duration_goals(df)
  goal_intensity(df)
  age_range(df)
  duration_intensity(df)
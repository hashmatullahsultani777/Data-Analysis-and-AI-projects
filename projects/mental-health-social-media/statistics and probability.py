import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
                             How Data is Collected
   Methodology: Data was gathered using online servey tools like Google Forms and 
   serveyMonkey   
                        
   Context: it is a Data set in Kaggle used for Data Science and Statistics projects for EDA (Exploratory Data Analysis)

   Source and Origin : 
       Primary Source: it was Orginally developed as a part Statistics and Data Science Course
       project at the University of Libral Arts of Bangaladesh (ULAB)

   

'''


# Loading the dataset
file_name = "Mental_Health_and_Social_Media_Balance_Dataset.csv"
df = pd.read_csv("E:/Mental_Health_and_Social_Media_Balance_Dataset.csv")

# Select only numeric or the number columns
numeric_df = df.select_dtypes(include=['number'])

# Calculate the descriptive statistics
descriptive_stats = numeric_df.describe()

# Calculate variance and add it to the descriptive statistics table
variance_series = numeric_df.var().rename('variance')
descriptive_stats.loc['variance'] = variance_series

print("### Complete Descriptive Statistics for Numeric Columns ###")
print(descriptive_stats.to_string())

print("\n--- Categorical Column Counts (Gender) ---")
print(df['Gender'].value_counts())

print("\n--- Categorical Column Counts (Social Media Platform) ---")
print(df['Social_Media_Platform'].value_counts())


'''
High Happeniess: if we look to Happeniess index and its mean almost all people are happy and its mean is 8.38 which shows high happeniess and lowest Happeniess score is 4  but 75th of half percentile is 10 and it skewed toward 10 .

Daily Screen Time(hrs): the range of daily screen time is between 1 hour to almost 11 hours and its mean is 5.53, and it has a crucial impact to measure it for balance . because High screen time is aften associated with negative mental health  outcomes

Stress Level (1-10): the range of stress from data set is from 2 to 10 and its Average is 6.62 which shows that more then half of the participant are in the Category of High Level Stress, even most of the Participant has High Happeniess index but they also struggle with Stress

Sleep Quality: the Average sleep Quality or the Hourse that participant sleep is 6.30 which is more then midpoint and generally okay but it need a little more improvement becuse Sleep Quality has direct connection with screen time and High level pressure spacialy those who use Phone or social media before going to sleep because poor sleep is aften due to screen time before bed


Exercise Frequency(in week): physical Activity is very importent for a positive and strong mental health but the average of Exercise in a week is 2.45 which is less and this show that alot of participants are not doing Exercise which could lead to a negative impact on health and impact on the mental health.


Categorical variable overview: if we look at Gender Distribution 248 are male, 229 are female and 23 are from other genders.

Widely used Social media paltforems: Tiktok is on the top used mostly and then Twitter and linked in


Overview : the Descriptive Statistics implied on the Data set shows that the population is  quiet happy but they also face more then Average rate of Stress and use alot of time in Social media 


'''


# --- Part 2: Visualization ---


# Load the dataset
file_name = "Mental_Health_and_Social_Media_Balance_Dataset.csv"
df = pd.read_csv("E:/Mental_Health_and_Social_Media_Balance_Dataset.csv")


# --- 1. Daily Screen Time (Histogram) ---
plt.figure(figsize=(10, 6))
plt.hist(df['Daily_Screen_Time(hrs)'], bins=20, edgecolor='black', color='skyblue')
plt.title('1. Distribution of Daily Screen Time (hrs)', fontsize=15)
plt.xlabel('Daily Screen Time (hrs)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.5)
plt.tight_layout()
plt.show()



# --- 2. Stress Level (Histogram) ---
plt.figure(figsize=(10, 6))
# Using align='left' to match bins to integer scores 2-10
plt.hist(df['Stress_Level(1-10)'], bins=9, edgecolor='black', color='salmon', align='left') 
plt.title('2. Distribution of Stress Level (1-10)', fontsize=15)
plt.xlabel('Stress Level (1-10)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(range(2, 11))
plt.grid(axis='y', alpha=0.5)
plt.tight_layout()
plt.show()

'''

'''
# --- 3. Happiness Index (Bar Chart - Value Counts) ---
happiness_counts = df['Happiness_Index(1-10)'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
happiness_counts.plot(kind='bar', edgecolor='black', color='lightgreen')
plt.title('3. Distribution of Happiness Index (1-10)', fontsize=15)
plt.xlabel('Happiness Index Score', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.tick_params(axis='x', rotation=0)
plt.grid(axis='y', alpha=0.5)
plt.tight_layout()
plt.show()

'''

'''
# --- 4. Sleep Quality (Bar Chart - Value Counts) ---
sleep_counts = df['Sleep_Quality(1-10)'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
sleep_counts.plot(kind='bar', edgecolor='black', color='gold')
plt.title('4. Distribution of Sleep Quality (1-10)', fontsize=15)
plt.xlabel('Sleep Quality Score', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.tick_params(axis='x', rotation=0)
plt.grid(axis='y', alpha=0.5)
plt.tight_layout()
plt.show()

'''

'''

# --- 5. Exercise Frequency (Bar Chart - Value Counts) ---
exercise_counts = df['Exercise_Frequency(week)'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
exercise_counts.plot(kind='bar', edgecolor='black', color='lightcoral')
plt.title('5. Distribution of Exercise Frequency (week)', fontsize=15)
plt.xlabel('Exercise Frequency (days/week)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.tick_params(axis='x', rotation=0)
plt.grid(axis='y', alpha=0.5)
plt.tight_layout()
plt.show()

'''



'''


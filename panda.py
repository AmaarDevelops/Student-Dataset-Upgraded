import pandas as pd
import numpy as np

df = pd.read_csv("Students_DataSet/student_dataset.csv",encoding='latin1')

missing = df.isnull().sum()
print('\nMissing Values :- ', missing)

df['ID'].fillna(df['ID'].mean(),inplace=True)

df['Gender'].fillna("undefined",inplace=True)

female_count = df['Gender'].value_counts()['Female']
male_count = df['Gender'].value_counts()['Male']

passed_count = df['Passed'].value_counts()[True]

max_avg = df['Average'].max()
min_avg = df['Average'].min()

unique_gender = df['Gender'].unique()

mean_attendance_for_passed = df[df['Passed'] == True]['Attendance'].mean()

female_avg = df[df['Gender'] == 'Female']['Average'].mean()
male_avg = df[df['Gender'] == 'Male']['Average'].mean()

top_5_highest_avg = df['Average'].nlargest(5)

student_older_than_20 = df[df['Age'] > 20]

students_failed_but_90percent = df[(df['Attendance'] > 90) & (df['Passed'] == 'No')]

studnets_who_scored_80_inmaths_and_cs = df[(df['CS'] > 80 ) & (df['Math'] > 80)]

students_under_18_withaverage_greatherthan70 = df[(df['Age'] < 18) & (df['Average'] > 70)]

df['Result'] =  df['Passed'].apply(lambda x: 'Pass' if x == True else "Fail")

df['Passed'] = df['Passed'].apply(lambda x:'Yes' if x == True else "No")

df['Total Marks'] = df['Math'] + df['Physics'] + df['CS']

def grade(avg):
    if avg >= 85:
        return 'A'
    elif avg > 75 and avg < 85:
        return 'B'
    elif avg > 50 and avg < 70:
        return 'C'
    else:
        return 'D'
    
df['Grade'] = df['Average'].apply(grade) 

topped_math = df.nlargest(3,'Math')[['Name','Math']]
topped_physics = df.nlargest(3,'Physics')[['Name','Physics']]
topped_CS = df.nlargest(3,'CS')[['Name','CS']]

df['Rank'] = df['Average'].rank(ascending=False,method='dense')

Topper = df[df['Rank'] == 1]['Name']

def bucket(age):
    if age <= 19:
        return 'Teen'
    elif age <= 22:
        return 'College'
    else:
        return 'Adult'

df['Age Group'] = df['Age'].apply(bucket)    
    
    



print('Male :-',male_count)
print('Female:-',female_count)
print('Passed :-', passed_count)
print('Max avg:-',max_avg)
print('Min avg:-',min_avg)
print("unique gender",unique_gender)
print("mean_attendance for passsed :-",mean_attendance_for_passed)
print('female_avg_score:-',female_avg)
print('male_avg_score:-',male_avg)
print("top 5 highest averages:-",top_5_highest_avg)
print("students older than 20:-",len(student_older_than_20))
print("Students iwth 90% attendance but failed",len(students_failed_but_90percent))
print("Students with more than 80 marks in CS and Maths:-",len(studnets_who_scored_80_inmaths_and_cs))
print("Students with greater than 70 avg under 18:-",len(students_under_18_withaverage_greatherthan70))
print("Top 3 in Maths:-",topped_math)
print('Top 3 In Physics:-',topped_physics)
print("Top 3 in CS:-",topped_CS)
print("Topper:-",Topper)

print('\nafter:-',df)
df.to_csv('Students_dataset-pandas.csv')
import pandas as pd

#Count of people per race
def race_count(df):
    return df["race"].value_counts()

#Average age of men
def avg_age_men(df):
    return round(df[df["sex"] == "Male"]["age"].mean(), 1)


# Percentage of people with a bachelor's degree
def percentage_bachelors(df):
    percentage = (df[df["education"] == "Bachelors"].shape[0] / df.shape[0]) * 100
    return round(percentage, 1)


# Percentage of people with advanced eduaction earning>50K by education level
def higher_education_rich(df):
    advanced_edu = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    percentage = (advanced_edu[advanced_edu["salary"] == ">50K"].shape[0] / advanced_edu.shape[0]) * 100
    return round(percentage, 1)

#Percentage of poeple without advanced eduaction earning>50K
def lower_education_rich(df):
    lower_edu = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    percentage = (lower_edu[lower_edu["salary"] == ">50K"].shape[0] / lower_edu.shape[0]) * 100
    return round(percentage, 1)

# Minumum hours per week
def min_work_hours(df):
    return df["hours-per-week"].min()


#Percentage of people working minimum houres earning>50K
def rich_percentage_min_workers(df):
    min_hours_workers = df[df["hours-per-week"] == df["hours-per-week"].min()]
    percentage = (min_hours_workers[min_hours_workers["salary"] == ">50K"].shape[0] / min_hours_workers.shape[0]) * 100
    return round(percentage, 1)

#Countries with the highest percentage of>50K earners
def highest_earning_country(df):
    countries = df.groupby("native-country")["salary"].value_counts(normalize=True).unstack()
    highest_country = countries[">50K"].idxmax()
    highest_percentage = round(countries[">50K"].max() * 100, 1)
    return highest_country, highest_percentage

#Most popular occupation for>50K earners in India
def top_occupation_india(df):
    india_high_earners = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    return india_high_earners["occupation"].value_counts().idxmax()


import pandas as pd

from demographic_data_analyzer import avg_age_men, higher_education_rich, highest_earning_country, lower_education_rich, min_work_hours, percentage_bachelors, race_count, rich_percentage_min_workers, top_occupation_india

df = pd.read_csv("adult.data.csv")
import demographic_data_analyzer
from unittest import main

# Run unit tests automatically

print("Race Count:\n", race_count(df))
print("Average Age of Men:", avg_age_men(df))
print("Percentage with Bachelors:", percentage_bachelors(df))
print("Higher Education earning >50K:", higher_education_rich(df))
print("Lower Education earning >50K:", lower_education_rich(df))
print("Minimum Work Hours:", min_work_hours(df))
print("Percentage of Rich Minimum Hour Workers:", rich_percentage_min_workers(df))
print("Highest Earning Country:", highest_earning_country(df))
print("Top Occupation in India:", top_occupation_india(df))

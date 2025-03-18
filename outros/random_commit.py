import os
import random
from datetime import date, time, timedelta, datetime


def daterange(start_date: date, end_date: date):
    days = int((end_date - start_date).days)
    for n in range(days):
        yield start_date + timedelta(n)


# Get number of commits from the user
try:
    max_commits = int(input("Enter the max number of commits per day to create (1-24): "))
    if (max_commits > 24):
        raise ValueError
except ValueError:
    print("Please enter a valid integer for the max number of commits per day.")
    exit(1)

# Get the year from the user
try:
    year = int(input("Enter the start year for the commits (e.g., 2020): "))
    if (year > date.today().year):
        raise ValueError
except ValueError:
    print("Please enter a valid year.")
    exit(1)

# Create a file for dummy commits
file_path = 'test.txt'
with open(file_path, 'a') as file:
    file.write('Initial commit\n')

start_date = date(year, 1, 1)
end_date = date.today()
base_hours = range(0, 23)
for current_date in daterange(start_date, end_date):
    num_commits = random.randint(1, max_commits)
    hours = random.sample(base_hours, num_commits)
    hours.sort()
    for hour in hours:
        new_time = time(hour, random.randint(0, 59), random.randint(0, 59))
        combined_date = datetime.combine(current_date, new_time)

        # Construct the commit date string
        commit_date_str = combined_date.strftime("%Y-%m-%d %H:%M:%S")

        # Write to file to create a change
        with open(file_path, 'a') as file:
            file.write(f'Commit for {commit_date_str}\n')
    
        # Add and commit changes with the specified date
        try:
            os.system('git add test.txt')
            os.system(f'git commit --date="{commit_date_str}" -m "Changes to {file_path}"')
        except Exception as e:
            print(f"Error during commit for day {commit_date_str}: {e}")

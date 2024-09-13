''' Final Draft

Module: Python With Bin - Reusable Module for My Data Analytics Projects

This is my first program for datafun-01-utils
'''

import statistics

#####################################
# Declare a global variables
#####################################

# boolean indicating if project is privately held. 
is_privately_held: bool = True

# integer representing the size of the team involved in the project.
team_size: int = 7

# list of strings representing the tools being used in the project. 
tools_used: list = ["Git", "GitHub", "Python"]

# list of floating-point numbers representing recent daily temperatures. 
daily_temperatures: list = [72.5, 75.0, 69.8, 71.6, 74.2]

# client satisfaction  ratings
client_satisfaction_ratings: list = [4.9, 4.8, 5.0, 5.0, 4.7]

#####################################
# calculate basic statistics for daily temperatures
#####################################

# calculate the minimum temperature
min_temp: float = min(daily_temperatures)

# calculate the maximum temperature
max_temp: float = max(daily_temperatures)

# calculate the mean (average) temperature
mean_temp: float = statistics.mean(daily_temperatures)

# calculate the standard deviation of temperatures
stdev_temp: float = statistics.stdev(daily_temperatures)

#####################################
# calculate basic statistics for client satisfaction
#####################################

# calculate the minimum temperature
min_rating: float = min(client_satisfaction_ratings)

# calculate the maximum temperature
max_rating: float = max(client_satisfaction_ratings)

# calculate the mean (average) temperature
mean_rating: float = statistics.mean(client_satisfaction_ratings)

# calculate the standard deviation of temperatures
stdev_rating: float = statistics.stdev(client_satisfaction_ratings)

#####################################
# declare a global variable named byline.
# make it a multiline f-string to show our info. 
#####################################

byline: str = f""" 
-------------------------------------------------
 Python With Bin: A Coding Company
-------------------------------------------------
Is Privately Held: {is_privately_held}
Number of Team Members: {team_size}
Tools Used: {tools_used}
Recent Daily Temperatures of the Office: {daily_temperatures}
Minimum Temperature: {min_temp:.2f}
Maximum Temperature: {max_temp:.2f}
Mean Temperature: {mean_temp:.2f}
Standard Deviation of Temperatures: {stdev_temp:.2f}

Client Satisfaction Ratings: {client_satisfaction_ratings}
Minimum Satisfaction Rating: {min_rating:.2f}
Maximum Satisfaction Rating: {max_rating:.2f}
Mean Satisfaction Rating: {mean_rating:.2f}
Standard Deviation of Satisfaction Ratings: {stdev_rating:.2f}
"""

#####################################
# Function to return the byline.
#####################################

# Function named get_byline.
# Returns the value of the byline variable.
def get_byline() -> str:
    '''Return the byline string.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# a function named main, returns byline when called

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(byline)

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
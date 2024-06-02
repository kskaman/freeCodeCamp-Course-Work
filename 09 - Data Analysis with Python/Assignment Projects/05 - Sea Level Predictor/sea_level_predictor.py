import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    fit = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level'])
    slope, intercept = fit.slope, fit.intercept
    minYear = df['Year'].min()
    x = pd.Series([i for i in range(minYear, 2051)])
    plt.plot(x , slope * x + intercept)

    # Create second line of best fit
    df_new = df[df['Year'] >= 2000]
    second_fit = linregress(
        df_new['Year'], df_new['CSIRO Adjusted Sea Level'])
    slope, intercept = second_fit.slope, second_fit.intercept
    
    x1 = pd.Series([i for i in range(2000, 2051)])
    plt.plot(x1 , slope * x1 + intercept)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
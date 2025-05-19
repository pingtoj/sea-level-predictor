import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')


    # Create scatter plot  
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Observed Data', alpha=0.6)

    # Create first line of best fit
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(1880, 2051)  # Predicting from 1880 to 2050
    sea_level_pred_all = res_all.slope * years_all + res_all.intercept
    plt.plot(years_all, sea_level_pred_all, 'r', label='Fit: All Data')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)  # Predicting from 2000 to 2050
    sea_level_pred_recent = res_recent.slope * years_recent + res_recent.intercept
    plt.plot(years_recent, sea_level_pred_recent, 'g', label='Fit: 2000+ Data')

    # Add labels and title

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
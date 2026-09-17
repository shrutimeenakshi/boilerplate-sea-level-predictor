import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    x = pd.Series(range(1880, 2051))
    y = slope * x + intercept

    plt.plot(x, y)

    df_recent = df[df["Year"] >= 2000]

    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    x_recent = pd.Series(range(2000, 2051))
    y_recent = slope_recent * x_recent + intercept_recent

    plt.plot(x_recent, y_recent)

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.savefig("sea_level_plot.png")
    return plt.gca()
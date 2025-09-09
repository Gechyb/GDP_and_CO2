import pandas as pd

data = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/refs/heads/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)
data.head()

mortaliity_rate = data["Mortality rate, infant (per 1,000 live births)"]

gdp_per_capita = data["GDP per capita (constant 2010 US$)"]
country_name = data["Country Name"]

import seaborn as sns
import matplotlib.pyplot as plt

plt.scatter(mortaliity_rate, gdp_per_capita)
plt.title("GDP per capita vs mortality rate")
plt.xlabel("Mortality rate")
plt.ylabel("GDP per capita")
plt.show()

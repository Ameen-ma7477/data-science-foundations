import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('logarithm/revenue1.csv')

print(df)

df.plot(
    x="company",
    y="revenue",
    kind="bar",
    color="blue",
    title="Company Revenue",
    logy=True
)

plt.show()
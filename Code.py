#https://seaborn.pydata.org/generated/seaborn.pairplot.html
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

penguins = pd.read_csv("penguins.csv")

sns.pairplot(penguins)
sns.pairplot(penguins, hue="species")
sns.pairplot(penguins, hue="species", diag_kind="hist")
sns.pairplot(penguins, kind="kde")
sns.pairplot(penguins, kind="hist")
sns.pairplot(penguins, hue="species", markers=["o", "s", "D"])
sns.pairplot(penguins, height=1.5)
sns.pairplot(
    penguins,
    x_vars=["bill_length_mm", "bill_depth_mm", "flipper_length_mm"],
    y_vars=["bill_length_mm", "bill_depth_mm"],
)

sns.pairplot(penguins, corner=True)
sns.pairplot(
    penguins,
    plot_kws=dict(marker="+", linewidth=1),
    diag_kws=dict(fill=False),
)
g = sns.pairplot(penguins, diag_kind="kde")
g.map_lower(sns.kdeplot, levels=4, color=".2")

plt.show()

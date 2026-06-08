import seaborn as sns
import matplotlib.pyplot as plt

# df = sns.load_dataset("penguins")
# sns.pairplot(df, hue="species")

tips = sns.load_dataset("tips")
sns.regplot(x="total_bill", y="tip", data=tips);

plt.show()
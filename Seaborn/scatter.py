# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset from seaborn
data = sns.load_dataset("iris")

# Create a scatter plot using Seaborn
sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species")

# Add titles and labels
plt.title("Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

# Show the plot
plt.show()

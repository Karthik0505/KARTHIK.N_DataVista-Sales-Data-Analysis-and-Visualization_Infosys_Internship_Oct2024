# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Create a line plot using Seaborn
# We'll use 'petal_length' as the x-axis and 'petal_width' as the y-axis,
# grouping by 'species' with a marker for each line.
sns.lineplot(data=data, x="petal_length", y="petal_width", hue="species", marker="o")

# Add titles and labels
plt.title("Petal Length vs Petal Width by Species")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")

# Show the plot
plt.show()

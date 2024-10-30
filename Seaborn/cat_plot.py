# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Create a catplot for petal length by species
sns.catplot(data=data, x="species", y="petal_length", kind="box", height=6, aspect=1.5, palette="Set2")

# Add titles and labels
plt.title("Catplot of Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")

# Show the plot
plt.show()

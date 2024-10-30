# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a point plot for average petal length by species
sns.pointplot(data=data, x="species", y="petal_length", palette="Set2", markers="o", scale=1.5)

# Add titles and labels
plt.title("Point Plot of Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")

# Show the plot
plt.show()

# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a swarm plot for petal length vs petal width
sns.swarmplot(data=data, x="petal_length", y="petal_width", hue="species", palette="Set2", dodge=True)

# Add titles and labels
plt.title("Swarm Plot of Petal Length vs. Petal Width by Species")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")

# Show the plot
plt.show()

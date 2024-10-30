# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a bar plot for the average petal length by species
sns.barplot(data=data, x="species", y="petal_length", palette="viridis", ci=None)

# Add titles and labels
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")

# Show the plot
plt.show()

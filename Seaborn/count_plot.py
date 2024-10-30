# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Set the figure size
plt.figure(figsize=(8, 6))

# Create a count plot for the species
sns.countplot(data=data, x="species", palette="Set2")

# Add titles and labels
plt.title("Count Plot of Iris Species")
plt.xlabel("Species")
plt.ylabel("Count")

# Show the plot
plt.show()

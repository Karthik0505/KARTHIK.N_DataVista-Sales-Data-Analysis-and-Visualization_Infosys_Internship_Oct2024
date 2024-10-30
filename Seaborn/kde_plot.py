# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a KDE plot for petal length
sns.kdeplot(data=data, x="petal_length", hue="species", fill=True, palette="Set2", common_norm=False)

# Add titles and labels
plt.title("KDE Plot of Petal Length by Species")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Density")

# Show the plot
plt.show()

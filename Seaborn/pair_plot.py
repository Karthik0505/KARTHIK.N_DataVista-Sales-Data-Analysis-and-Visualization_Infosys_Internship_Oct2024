# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Create a pair plot
sns.pairplot(data, hue="species", palette="Set2")

# Add titles and show the plot
plt.suptitle("Pair Plot of Iris Dataset", y=1.02)  # Adjust title position
plt.show()

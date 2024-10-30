# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Create a joint plot for petal length vs petal width
sns.jointplot(data=data, x="petal_length", y="petal_width", hue="species", palette="Set2", kind="scatter", height=7)

# Add titles
plt.suptitle("Joint Plot of Petal Length and Petal Width", y=1.02)  # Adjust title position

# Show the plot
plt.show()

# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Set the figure size
plt.figure(figsize=(10, 6))

# Create a regression plot for petal length vs petal width
sns.regplot(data=data, x="petal_length", y="petal_width", scatter_kws={"color": "blue"}, line_kws={"color": "red"})

# Add titles and labels
plt.title("Regression Plot of Petal Length vs. Petal Width")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")

# Show the plot
plt.show()

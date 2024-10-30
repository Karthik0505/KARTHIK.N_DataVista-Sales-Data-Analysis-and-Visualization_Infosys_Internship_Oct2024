# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Create a histogram for Petal Length
plt.figure(figsize=(12, 5))

# Histogram for Petal Length
plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
sns.histplot(data=data, x="petal_length", bins=20, kde=True, color="blue")
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")

# Histogram for Petal Width
plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
sns.histplot(data=data, x="petal_width", bins=20, kde=True, color="orange")
plt.title("Distribution of Petal Width")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")

# Show the plots
plt.tight_layout()  # Adjusts subplots to fit into the figure area.
plt.show()

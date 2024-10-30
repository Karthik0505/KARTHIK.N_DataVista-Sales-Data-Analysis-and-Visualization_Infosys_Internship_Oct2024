# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Create a FacetGrid
g = sns.FacetGrid(data, col="species", height=4, aspect=1)

# Map a scatter plot to the grid
g.map(sns.scatterplot, "petal_length", "petal_width", color="blue")

# Add titles and labels
g.set_axis_labels("Petal Length (cm)", "Petal Width (cm)")
g.set_titles(col_template="{col_name}")

# Show the plot
plt.subplots_adjust(top=0.9)  # Adjust the top space for the main title
g.fig.suptitle("Petal Length vs. Petal Width by Species")  # Add a main title
plt.show()

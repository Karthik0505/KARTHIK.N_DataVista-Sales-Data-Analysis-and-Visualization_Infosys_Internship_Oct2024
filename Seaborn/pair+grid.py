# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
data = sns.load_dataset("iris")

# Create a PairGrid
g = sns.PairGrid(data, hue="species", height=2.5)

# Map the upper triangle to scatter plots
g.map_upper(sns.scatterplot)

# Map the lower triangle to KDE plots
g.map_lower(sns.kdeplot, fill=True)

# Map the diagonal to histograms
g.map_diag(sns.histplot, kde=True)

# Add a legend
g.add_legend()

# Add titles
plt.suptitle("PairGrid of Iris Dataset", y=1.02)  # Adjust title position

# Show the plot
plt.show()

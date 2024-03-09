#Imported libraries 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from shiny.express import ui, input, render

#Added page options for app 
ui.page_opts(title="Cintel 01 Slider App", fillable= True)

#Sidebar with slider input
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)
    #Selected_number_of_bins that uniquely identifies this input value. 
    #Number of Bins to be displayed alongside the slider.
    #An integer representing the minimum number of bins (e.g., 0).
    #An integer representing the maximum number of bins (e.g., 100).
    #An integer representing the initial value of the slider (e.g., 20)

#Define a plot function for histogram
@render.plot(alt="A histogram")
def histogram():
    #Set a random Seed 
    np.random.seed(6)
    #Generate random data in histogram 
    x = 100 + 15 * np.random.randn(437)
    #Plot the histogram 
    plt.hist(x, input.selected_number_of_bins(), density=True)

#Define a plot function for scatterplot 
@render.plot(alt="A scatterplot")
def scatterplot():
    #Set a random Seed 
    np.random.seed(25)
    # random numbers for X-axis from a normal distribution and size the number of random numbers to generate
    x = np.random.normal(size=100)
    # random numbers for Y-axis from a normal distribution and size the number of random numbers to generate
    y = np.random.normal(size=100)
    #Plot the scatterplot (points and plot color)
    sns.scatterplot(x=x, y=y, color='purple')
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class CTkExtendedGraph(ctk.CTkFrame):
    """
    A CustomTkinter Widget for displaying a stacked bar chart.
    It provides a flexible way to visualize data with two categories.
    """
    
    def __init__(self, master=None, title="Stacked Bar Chart", data=None, category_labels=("Category 1", "Category 2"), category_colors=("#00FF00", "#AAAAAA"), unit="", width=600, height=400, **kwargs):
        """
        Initializes the stacked bar chart widget.
        
        :param master: Parent widget
        :param data: Dictionary with values for the two categories, e.g., {'Jan': (value1, value2), ...}
        :param category_labels: Tuple with the names of the two categories
        :param category_colors: Tuple with the colors for the two categories
        :param unit: Unit to display next to the numbers (e.g., kWh)
        :param width: Width of the widget
        :param height: Height of the widget
        """
        super().__init__(master, **kwargs)
        
        self.title = title
        self.width = width
        self.height = height
        self.data = data if data else {"Jan": (200, 50), "Feb": (180, 40), "Mar": (220, 30)}
        self.category_labels = category_labels
        self.category_colors = category_colors
        self.unit = unit
        self.canvas = None  # Initialize the canvas variable
        
        self.create_chart()
    
    def create_chart(self):
        """
        Creates the stacked bar chart using Matplotlib.
        """
        # Create Matplotlib figure
        figure, axis = plt.subplots(figsize=(self.width / 100, self.height / 100), facecolor='none')
        
        # Prepare data for plotting
        months = list(self.data.keys())
        category1_values = np.array([self.data[month][0] for month in months])
        category2_values = np.array([self.data[month][1] for month in months])
        
        bar_width = 0.5
        index_positions = np.arange(len(months))
        
        # Draw bars for the two categories
        axis.bar(index_positions, category1_values, bar_width, color=self.category_colors[0], label=self.category_labels[0])
        axis.bar(index_positions, category2_values, bar_width, color=self.category_colors[1], bottom=category1_values, label=self.category_labels[1])
        
        # Set axis labels
        axis.set_xticks(index_positions)
        axis.set_xticklabels(months, fontsize=10, color='white')
        axis.set_yticklabels([f"{tick} {self.unit}" for tick in axis.get_yticks()], fontsize=10, color='white')
        axis.set_title(self.title, fontsize=12, color='white')
        
        # Set background color
        axis.set_facecolor('#0A0A0A')
        figure.patch.set_facecolor('#0A0A0A')
        
        # Add legend
        legend = axis.legend(facecolor='#0A0A0A', edgecolor='white', fontsize=10)
        for text in legend.get_texts():
            text.set_color("white")
        
        # If there is an existing canvas, remove it
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        
        # Embed Matplotlib figure into CustomTkinter
        self.canvas = FigureCanvasTkAgg(figure, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill='both', expand=True)
    
    def add_new_entry(self, new_entry):
        """
        Adds a new data entry to the end of the bar chart and redraws the chart.
        If the entry already exists, it will overwrite the existing values.
        
        :param new_entry: Dictionary with a new month and corresponding values
                          (e.g., {'Jan': (value1, value2)})
        """
        # Check if the new_entry is a dictionary with exactly one key
        if isinstance(new_entry, dict) and len(new_entry) == 1:
            # Extract the new month and its corresponding values
            new_month, new_values = list(new_entry.items())[0]
            
            if isinstance(new_values, tuple) and len(new_values) == 2:
                # Update the data dictionary with the new entry
                self.data.update(new_entry)
                
                # Redraw the chart with the updated data
                self.create_chart()
            else:
                print("Error: The values must be a tuple with two elements.")
        else:
            print("Error: new_entry must be a dictionary with exactly one key.")

# Example usage of the method
if __name__ == "__main__":

    def on_button_click():
        graph.add_new_entry({"Jan": (100, 10)})

    app = ctk.CTk()
    app.geometry("700x500")
    button = ctk.CTkButton(app, text="Test", command=on_button_click)
    button.pack()

    data = {
        "Jan": (200, 0), "Feb": (180, 40), "Mar": (220, 30),
        "Apr": (250, 20), "May": (300, 15), "Jun": (350, 10),
        "Jul": (330, 20), "Aug": (310, 25), "Sep": (270, 30),
        "Oct": (230, 40), "Nov": (190, 50), "Dec": (180, 60)
    }
    
    graph = CTkExtendedGraph(app, "Charged Energy", data, category_labels=("Solar", "Grid"), category_colors=("#FF5733", "#33FFCE"), unit="kWh")
    graph.pack(fill='both', expand=True)
    
    app.mainloop()

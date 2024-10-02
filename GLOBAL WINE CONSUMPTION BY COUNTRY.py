import tkinter as tk
from tkinter import ttk
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
data = pd.read_csv(r"F:\PROGRESS\PROJECTS\wine_data.csv")

# Data preprocessing
X = data[['Per_Capita_Wine_Consumption_(liters)', 'Wine_Production_(thousands_of_liters)', 'GDP_Per_Capita_(USD)', 'Population']]
y = data['Total_Wine_Consumption_(liters)']

# Create a linear regression model
model = LinearRegression()
model.fit(X, y)

# Create a function to handle button click event
def predict_wine_consumption():
    try:
        # Get the values from entry fields
        per_capita_consumption = float(per_capita_entry.get())
        wine_production = float(wine_production_entry.get())
        gdp_per_capita = float(gdp_per_capita_entry.get())
        population = float(population_entry.get())
        
        # Create a DataFrame with custom details
        new_country_data = pd.DataFrame({
            'Per_Capita_Wine_Consumption_(liters)': [per_capita_consumption],
            'Wine_Production_(thousands_of_liters)': [wine_production],
            'GDP_Per_Capita_(USD)': [gdp_per_capita],
            'Population': [population]
        })

        # Predict wine consumption for the new country
        predicted_consumption = model.predict(new_country_data)

        # Display the results
        result_label.config(text=f"Predicted Wine Consumption: {predicted_consumption[0]:.2f} liters")
        
        # Visualize the results (for example, a bar chart)
        plt.figure(figsize=(10, 6))
        plt.subplot(2, 2, 1)
        plt.scatter(data['Per_Capita_Wine_Consumption_(liters)'], y, color='blue', label='Actual')
        plt.scatter(per_capita_consumption, predicted_consumption, color='red', label='Predicted')
        plt.xlabel('Per Capita Wine Consumption (liters)')
        plt.ylabel('Total Wine Consumption (liters)')
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.scatter(data['Wine_Production_(thousands_of_liters)'], y, color='blue', label='Actual')
        plt.scatter(wine_production, predicted_consumption, color='red', label='Predicted')
        plt.xlabel('Wine Production (thousands of liters)')
        plt.ylabel('Total Wine Consumption (liters)')
        plt.legend()

        plt.subplot(2, 2, 3)
        plt.scatter(data['GDP_Per_Capita_(USD)'], y, color='blue', label='Actual')
        plt.scatter(gdp_per_capita, predicted_consumption, color='red', label='Predicted')
        plt.xlabel('GDP Per Capita (USD)')
        plt.ylabel('Total Wine Consumption (liters)')
        plt.legend()

        plt.subplot(2, 2, 4)
        plt.scatter(data['Population'], y, color='blue', label='Actual')
        plt.scatter(population, predicted_consumption, color='red', label='Predicted')
        plt.xlabel('Population')
        plt.ylabel('Total Wine Consumption (liters)')
        plt.legend()

        plt.tight_layout()
        plt.show()
    
    except ValueError:
        # Handle the case where input values are not valid floats
        result_label.config(text="Please enter valid numeric values.")
   
# Create the main application window
root = tk.Tk()
root.title("Wine Consumption Prediction")

# Create labels and entry fields for user input
per_capita_label = ttk.Label(root, text="Per Capita Wine Consumption (liters):")
wine_production_label = ttk.Label(root, text="Wine Production (thousands of liters):")
gdp_per_capita_label = ttk.Label(root, text="GDP Per Capita (USD):")
population_label = ttk.Label(root, text="Population:")

per_capita_entry = ttk.Entry(root)
wine_production_entry = ttk.Entry(root)
gdp_per_capita_entry = ttk.Entry(root)
population_entry = ttk.Entry(root)

# Create a predict button
predict_button = ttk.Button(root, text="Predict Wine Consumption", command=predict_wine_consumption)

# Create a label to display the prediction result
result_label = ttk.Label(root, text="")

# Arrange widgets using grid layout
per_capita_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
wine_production_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
gdp_per_capita_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
population_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

per_capita_entry.grid(row=0, column=1, padx=5, pady=5)
wine_production_entry.grid(row=1, column=1, padx=5, pady=5)
gdp_per_capita_entry.grid(row=2, column=1, padx=5, pady=5)
population_entry.grid(row=3, column=1, padx=5, pady=5)

predict_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Start the Tkinter main loop
root.after(0, predict_wine_consumption)
root.mainloop()

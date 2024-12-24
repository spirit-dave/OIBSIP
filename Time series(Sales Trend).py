import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/storage/emulated/0/OIBSIP/retail_sales_dataset.csv'

retail_sales_data = pd.read_csv(file_path)

# Convert the 'Date' column to datetime format
retail_sales_data['Date'] = pd.to_datetime(retail_sales_data['Date'], errors='coerce')

# Aggregate sales by date
sales_trend = retail_sales_data.groupby('Date')['Total Amount'].sum()


# Save the aggregated sales trend to a CSV file
output_csv_path = '/storage/emulated/0/OIBSIP/sales_trend.csv'
sales_trend.to_csv(output_csv_path, header=True)
print(f"Sales trend data saved to: {output_csv_path}")

# Plot sales trends over time
plt.figure(figsize=(12, 6))
plt.plot(sales_trend.index, sales_trend.values, marker='o', linestyle='-', color='blue')
plt.title('Sales Trends Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Sales Amount', fontsize=12)
plt.grid(True)
plt.tight_layout()

# Save the plot to an image file
output_plot_path = '/storage/emulated/0/OIBSIP/sales_trend_plot.png'
plt.savefig(output_plot_path)
print(f"Sales trend plot saved to: {output_plot_path}")


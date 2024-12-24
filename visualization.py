import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/storage/emulated/0/OIBSIP/retail_sales_dataset.csv'  # Replace with your dataset path
retail_sales_data = pd.read_csv(file_path)

# Clean column names (remove leading/trailing spaces)
retail_sales_data.columns = retail_sales_data.columns.str.strip()

# Convert 'Date' column to datetime if not already done
retail_sales_data['Date'] = pd.to_datetime(retail_sales_data['Date'], errors='coerce')

# Drop rows where 'Date' or 'Total Amount' are NaN after conversion (if any)
retail_sales_data.dropna(subset=['Date', 'Total Amount'], inplace=True)

# ------------------------------------------
# 1. Sales Trends Over Time (Line Plot + CSV)
# ------------------------------------------
sales_trend = retail_sales_data.groupby('Date')['Total Amount'].sum()

# Save sales trends to CSV
sales_trend_csv_path = '/storage/emulated/0/OIBSIP/sales_trend.csv'
sales_trend.to_csv(sales_trend_csv_path, header=['Total Sales Amount'])
print(f"Sales trends data saved to: {sales_trend_csv_path}")

# Plot sales trend
plt.figure(figsize=(12, 6))
plt.plot(sales_trend.index, sales_trend.values, marker='o', linestyle='-', color='blue')
plt.title('Sales Trends Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Sales Amount', fontsize=12)
plt.grid(True)
plt.tight_layout()
sales_trend_plot_path = '/storage/emulated/0/OIBSIP/sales_trend_line_plot.png'
plt.savefig(sales_trend_plot_path)
plt.show()
print(f"Line plot for sales trends saved to: {sales_trend_plot_path}")

# -----------------------------------------------------------
# 2. Top 10 Product Categories by Sales (Bar Chart + CSV)
# -----------------------------------------------------------
if 'Product Category' in retail_sales_data.columns:
    top_categories = retail_sales_data.groupby('Product Category')['Total Amount'].sum().nlargest(10)
    
    # Save top categories data to CSV
    top_categories_csv_path = '/storage/emulated/0/OIBSIP/top_product_categories.csv'
    top_categories.to_csv(top_categories_csv_path, header=['Total Sales Amount'])
    print(f"Top product categories data saved to: {top_categories_csv_path}")

    # Plot bar chart
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_categories.values, y=top_categories.index, palette='viridis')
    plt.title('Top 10 Product Categories by Sales', fontsize=16)
    plt.xlabel('Total Sales Amount', fontsize=12)
    plt.ylabel('Product Category', fontsize=12)
    plt.tight_layout()
    top_categories_plot_path = '/storage/emulated/0/OIBSIP/top_product_categories_bar_chart.png'
    plt.savefig(top_categories_plot_path)
    plt.show()
    print(f"Bar chart for top product categories saved to: {top_categories_plot_path}")
else:
    print("Column 'Product Category' not found in the data.")
#----------------
# 3. Correlation Heatmap (Numerical Features + CSV)
# ---------------
numerical_columns = ['Quantity', 'Price per Unit', 'Total Amount']
if all(col in retail_sales_data.columns for col in numerical_columns):
    correlation_matrix = retail_sales_data[numerical_columns].corr()
    
    # Save correlation matrix to CSV
    correlation_csv_path = '/storage/emulated/0/OIBSIP/correlation_matrix.csv'
    correlation_matrix.to_csv(correlation_csv_path)
    print(f"Correlation matrix data saved to: {correlation_csv_path}")

    # Plot heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap of Numerical Features', fontsize=16)
    plt.tight_layout()
    heatmap_plot_path = '/storage/emulated/0/OIBSIP/correlation_heatmap.png'
    plt.savefig(heatmap_plot_path)
    plt.show()
    print(f"Heatmap for correlations saved to: {heatmap_plot_path}")
else:
    print(f"Some numerical columns are missing from the data.")

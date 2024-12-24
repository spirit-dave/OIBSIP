import pandas as pd

# Load the dataset
file_path = 'your_dataset_path.csv'  # Replace with the actual path to your dataset
retail_sales_data = pd.read_csv(file_path)

# Specify numerical columns
numerical_columns = ['Quantity', 'Price per Unit', 'Total Amount']

# Calculate statistics
statistics = {}
for column in numerical_columns:
    statistics[column] = {
        'Mean': retail_sales_data[column].mean(),
        'Median': retail_sales_data[column].median(),
        'Mode': retail_sales_data[column].mode().iloc[0],  # Extract the first mode
        'Standard Deviation': retail_sales_data[column].std()
    }

# Convert the results to a DataFrame for display
stats_df = pd.DataFrame(statistics).T

# Display the results
print(stats_df)

# Save the results to a CSV file if needed
stats_df.to_csv('basic_statistics.csv', index=True)

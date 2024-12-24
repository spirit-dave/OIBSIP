import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/storage/emulated/0/OIBSIP/retail_sales_dataset.csv' 

retail_sales_data = pd.read_csv(file_path)

# Analyze customer demographics
customer_gender = retail_sales_data['Gender'].value_counts()
customer_age_groups = pd.cut(retail_sales_data['Age'], bins=[0, 18, 35, 50, 100], labels=['<18', '18-35', '36-50', '50+'])
age_group_counts = customer_age_groups.value_counts()

# Analyze purchasing behavior by product category
product_sales = retail_sales_data.groupby('Product Category')['Total Amount'].sum()

# Save demographic analysis to a CSV
output_demographics_path = '/storage/emulated/0/OIBSIP/customer_demographics.csv'
demographics_data = pd.DataFrame({
    'Gender': customer_gender,
    'Age Group': age_group_counts
})
demographics_data.to_csv(output_demographics_path, index=True)
print(f"Customer demographic data saved to: {output_demographics_path}")

# Save product sales analysis to a CSV
output_product_sales_path = '/storage/emulated/0/OIBSIP/product_sales.csv'
product_sales.to_csv(output_product_sales_path, header=True)
print(f"Product sales data saved to: {output_product_sales_path}")

# Visualize and save customer demographics
plt.figure(figsize=(10, 5))

# Gender distribution
plt.subplot(1, 2, 1)
customer_gender.plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'pink'], startangle=90, ylabel="")
plt.title('Customer Gender Distribution')
gender_plot_path = '/storage/emulated/0/OIBSIP/gender_distribution.png'
plt.savefig(gender_plot_path)
print(f"Gender distribution plot saved to: {gender_plot_path}")

# Age group distribution
plt.subplot(1, 2, 2)
age_group_counts.sort_index().plot(kind='bar', color='lightgreen')
plt.title('Customer Age Group Distribution')
plt.xlabel('Age Group')
plt.ylabel('Number of Customers')
age_group_plot_path = '/storage/emulated/0/OIBSIP/age_group_distribution.png'
plt.tight_layout()
plt.savefig(age_group_plot_path)
print(f"Age group distribution plot saved to: {age_group_plot_path}")

# Visualize and save product category sales
plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.index, y=product_sales.values, palette='viridis')
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
product_sales_plot_path = '/storage/emulated/0/OIBSIP/product_sales_plot.png'
plt.tight_layout()
plt.savefig(product_sales_plot_path)
print(f"Product sales plot saved to: {product_sales_plot_path}")


# Retail Sales Analysis

This project involves an exploratory data analysis (EDA) of retail sales data to uncover insights, identify trends, and provide actionable recommendations for improving business performance.

## Project Overview

The analysis is structured into the following steps:

- Data Loading and Cleaning:

Importing the dataset and performing cleaning operations to ensure data quality.

- Descriptive Statistics:

Calculating summary statistics (mean, median, mode, standard deviation) to understand data distribution.

- Time Series Analysis:

Analyzing sales trends over time to identify seasonal patterns and peak periods.

- Customer and Product Analysis:

- Examining customer demographics and purchasing behavior.

Evaluating product category performance to highlight best-selling items.

- Visualization:

Presenting insights through visualizations including line plots, bar charts, and heatmaps.

- Recommendations:

Providing actionable business recommendations based on the findings.

## Technologies Used

- Python: Primary programming language for analysis.

- Pandas: For data manipulation and analysis.

- Matplotlib: For creating visualizations.

- Seaborn: For advanced statistical graphics.

## How to Run the Project

1. Clone the repository:

git clone https:https://github.com/spirit-dave/OIBSIP

2. Navigate to the project directory:

cd retail-sales-analysis

3. Install the required Python packages:

pip install -r requirements.txt

4. Place your dataset in the project directory and update the file path in the scripts.

5. Run the scripts for each step as needed:
  
- python step2_descriptive_statistics.py

- python step3_time_series_analysis.py

- python step4_customer_product_analysis.py

- python step5_visualization.py

## Results

The project provides:

- Detailed insights into sales trends and customer behavior.

- Visualizations to highlight key patterns in the data.

- Actionable recommendations to improve sales performance.

## Visualization Output Insignt & Actionable Recommendations

1. Heatmaps (Correlation Analysis):

Insight: Heatmaps helped identify relationships between numerical variables, such as:
- Strong correlations between sales and discounts suggest customers respond well to promotional offers.
- Weak correlations between customer demographics and total purchase value may indicate uniform spending behavior across groups.

Actionable Recommendation: Use data-driven insights to design effective discount strategies and refine customer segmentation approaches for personalized marketing.

![image](https://github.com/user-attachments/assets/628289b8-b92e-4de2-855b-ee7f526e7f48)

2. Line Plots (Sales Trends):

Insight: The line plot for sales trends highlighted peaks and troughs in sales over time. 
- Seasonal spikes during holiday months indicate increased shopping activity.
- Consistent dips in sales during off-peak months suggest a need for targeted promotions or campaigns during those times.

Actionable Recommendation: Align marketing and inventory strategies with these patterns to optimize revenue during peak seasons and drive sales during slower periods.

![image](https://github.com/user-attachments/assets/54546c37-8c7d-481b-88c9-350962559257)

3. Bar Charts (Top 10 Products by Sales):

Insight: The bar chart revealed which product categories generated the most revenue.
- Certain categories consistently dominated sales, indicating strong demand.
- Lower-performing categories might require investigation to understand poor performance (e.g., pricing, availability, or lack of demand).

Actionable Recommendation: Increase focus on high-performing categories by ensuring adequate stock levels and leveraging them in marketing campaigns. Consider discontinuing or revisiting strategies for underperforming categories.

![image](https://github.com/user-attachments/assets/691e61b6-0d75-4ba2-830a-002c2505e82b)

## General Key Recommendations:

1.	Inventory Management: Ensure sufficient stock for popular products and reduce stock for underperforming items.

2.	Targeted Promotions: Run promotions on high-margin products or those in underperforming categories.

3.	Customer Focus: Focus on the dominant customer age group and gender for marketing campaigns.

4.	Seasonal Trends: Prepare for peaks in sales trends by optimizing supply chain and logistics.

5.	Data-Driven Marketing: Use customer demographics for personalized offers and loyalty programs.

6.	Evaluation: Periodically reassess low-performing products for strategic improvements.



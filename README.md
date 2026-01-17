# FUTURE_DS_01

Project Overview
This project analyzes 4 years of sales data from a retail "Superstore" to identify growth opportunities and profitability gaps. The goal was to transform raw data into a client-ready dashboard and provide actionable business recommendations.

Key Objectives:
- Clean and prepare raw sales data (CSV).
- Analyze revenue trends, top products, and regional performance.
- Build an interactive dashboard for business stakeholders.
- Provide strategic recommendations to improve profitability.

Tools & Technologies
- Python (Pandas): For data cleaning, duplicate removal, and feature engineering.
- Power BI: For building the interactive dashboard and visualizations.
- VS Code: Development environment.

Key Business Insights
Based on the analysis of 9,994 sales records, here are the top findings:

1.Strong Revenue Growth: Annual sales have grown steadily, peaking at $733k in 2017 (a ~50% increase from 2014).

2.The "Furniture" Problem: While Furniture generates high revenue ($741k), it has the lowest profit margin (~2.4%) compared to Technology (17%). High shipping costs or discounts are likely eating into profits.

3.Top Performer: The "Canon imageCLASS 2200" is the single highest-revenue product (~$61k).

4.Regional Strategy: The "West Region" is the most profitable, while the Central Region lags behind.


Dashboard Analysis

From the dashboard we can answer some crucial questions given to us as a part of the task:

1.Which products generate the most revenue?
  "Fellowes PB500 Electric Punch Plastic Comb performs exceptionally well such that no product reached its level much less exceed with the  
   sole exception of Canon imageCLASS 2200 of course"

2.How do sales change over time?
  "As observed over an year the sales are highest in early to mid November and lowest in mid February"

3.Which categories or regions are most profitable?
  "West is providing an exceptionally high profit margin followed by East"

4.Where should the business focus to grow faster?
  "In terms of field technology should be the right way to go considering the success and sales of these items but if the context changes        
   to location West and East should be our way to go"

Recommendations
If I were advising the business owner, I would recommend:

1.Revise Furniture Pricing: Conduct an audit on "Tables" and "Bookcases." Consider reducing discounts or increasing shipping fees for these bulky items to improve margins.

2.Inventory Planning : Sales data shows a significant spike in November/December. Stock of top-selling Tech products must be increased by September to prevent stockouts.

3.Focus on Tech in the East: Shift marketing budget towards high-margin Technology products in the East and West regions, which have shown the strongest purchasing power.


Project Structure
- analysis.py - The Python script used to clean the raw data and calculate initial metrics.
- Cleaned_Superstore_Data.csv - The processed dataset ready for visualization.
- Sample - Superstore.csv - The raw original dataset.

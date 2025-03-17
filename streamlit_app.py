import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Data App Assignment, on Oct 7th")

st.write("### Input Data and Examples")
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=True)
st.dataframe(df)

# This bar chart will not have solid bars--but lines--because the detail data is being graphed independently
st.bar_chart(df, x="Category", y="Sales")

# Now let's do the same graph where we do the aggregation first in Pandas... (this results in a chart with solid bars)
st.dataframe(df.groupby("Category").sum())
# Using as_index=False here preserves the Category as a column.  If we exclude that, Category would become the datafram index and we would need to use x=None to tell bar_chart to use the index
st.bar_chart(df.groupby("Category", as_index=False).sum(), x="Category", y="Sales", color="#04f")
# added a drop down for Category
# Category selection
category = st.selectbox(
    "Category",
    ("Furniture", "Office Supplies", "Technology")  # Ensure correct tuple format
)

# Dictionary mapping categories to their respective subcategories
subcategories = {
    "Furniture": ["Bookcases", "Chairs", "Tables", "Furnishings"],
    "Office Supplies": ["Labels", "Storage", "Art", "Binders", "Appliances", "Paper", "Envelopes", "Fasteners", "Supplies"],
    "Technology": ["Phones", "Accessories", "Machines", "Copiers"]
}  # Make sure the dictionary is properly closed

# Dynamically update the multiselect options based on the selected category
selected_subcategories = st.multiselect(
    f"Select subcategories for {category}",  # Using f-string for dynamic text
    subcategories.get(category, [])  # Use .get() to avoid KeyError if category is missing
)


# Aggregate sales by month for selected subcategories
filtered_df.set_index("Order_Date", inplace=True)
sales_by_month = filtered_df.groupby(pd.Grouper(freq='M'))["Sales"].sum()

# Display the line chart
st.write("### Sales Trend for Selected Subcategories")
st.line_chart(sales_by_month)


# Aggregating by time
# Here we ensure Order_Date is in datetime format, then set is as an index to our dataframe
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df.set_index('Order_Date', inplace=True)
# Here the Grouper is using our newly set index to group by Month ('M')
sales_by_month = df.filter(items=['Sales']).groupby(pd.Grouper(freq='M')).sum()

st.dataframe(sales_by_month)

# Here the grouped months are the index and automatically used for the x axis
st.line_chart(sales_by_month, y="Sales")


st.write("## Your additions")
st.write("### (1) add a drop down for Category (https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)")
st.write("### (2) add a multi-select for Sub_Category *in the selected Category (1)* (https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)")
st.write("### (3) show a line chart of sales for the selected items in (2)")
st.write("### (4) show three metrics (https://docs.streamlit.io/library/api-reference/data/st.metric) for the selected items in (2): total sales, total profit, and overall profit margin (%)")
st.write("### (5) use the delta option in the overall profit margin metric to show the difference between the overall average profit margin (all products across all categories)")

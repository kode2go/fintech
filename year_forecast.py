import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from streamlit_lottie import st_lottie
import json

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

# Function to generate random numbers
def generate_random_numbers():
    return pd.DataFrame(np.random.randint(0, 101, size=(5, 5)), columns=[f'Column {i+1}' for i in range(5)])


def year_forecast():
    st.title("12 Year Forecast")

    with st.container():
        col1,col2=st.columns(2)
    with col1:
        st.markdown("""Generates forecasts for the next 12 months based on historical data, aiding in planning and budgeting.""")

    with col2:
        lottie2 = load_lottiefile("forecast.json")
        st_lottie(lottie2,key='place',height=300,width=300)

    st.subheader("Revenue assumption")

    # Create a dictionary with the data
    data = {
        "Revenue assumption": ["Number of stores", "Number of new stores", "Sq ft per store", "Sales per square foot ($/ft/yr)"],
        "Jan": [0.0, 0.0, 46000.0, 535.0],
        "Feb": [1.0, 1.0, 46000.0, 535.0],
        "Mar": [0.0, 0.0, 46000.0, 535.0],
        "Apr": [0.0, 0.0, 46000.0, 535.0],
        "May": [1.0, 1.0, 46000.0, 535.0],
        "Jun": [0.0, 0.0, 46000.0, 535.0],
        "Jul": [0.0, 0.0, 46000.0, 535.0],
        "Aug": [0.0, 0.0, 46000.0, 535.0],
        "Sep": [1.0, 1.0, 46000.0, 535.0],
        "Oct": [0.0, 0.0, 46000.0, 535.0],
        "Nov": [0.0, 0.0, 46000.0, 535.0],
        "Dec": [0.0, 0.0, 46000.0, 535.0]
    }

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)

    # Display the table
    st.table(df)

    # Plotting with Plotly
    fig = go.Figure()

    for col in df.columns[1:]:
        fig.add_trace(go.Bar(
            x=df['Revenue assumption'],
            y=df[col],
            name=col
        ))

    fig.update_layout(
        title="Revenue Assumptions",
        xaxis_title="Revenue Assumption",
        yaxis_title="Value",
        barmode='group'
    )

    st.plotly_chart(fig)

    st.divider()

    st.subheader("Operating cost assumptions")

    data2 = {
    "Operating cost assumptions": ["Gross margins", "SG&A", "SG&A as a percent of revenues"],
    "Jan": ["26.5%", 9500, None],
    "Feb": ["26.5%", 9500, None],
    "Mar": ["26.5%", 9500, None],
    "Apr": ["26.5%", 9500, None],
    "May": ["26.5%", 9500, None],
    "Jun": ["26.5%", 9500, None],
    "Jul": ["26.5%", 9500, None],
    "Aug": ["26.5%", 9500, None],
    "Sep": ["26.5%", 9500, None],
    "Oct": ["26.5%", 9500, None],
    "Nov": ["26.5%", 9500, None],
    "Dec": ["26.5%", 9500, None]
}

    # Create a DataFrame from the dictionary
    df2 = pd.DataFrame(data2)

    # Display the table
    st.table(df2)

    st.subheader("Tax assumptions")

    data3 = {
    "Tax assumptions": ["Effective tax rate"],
    "Jan": ["35.0%"],
    "Feb": ["35.0%"],
    "Mar": ["35.0%"],
    "Apr": ["35.0%"],
    "May": ["35.0%"],
    "Jun": ["35.0%"],
    "Jul": ["35.0%"],
    "Aug": ["35.0%"],
    "Sep": ["35.0%"],
    "Oct": ["35.0%"],
    "Nov": ["35.0%"],
    "Dec": ["35.0%"]
}

    # Create a DataFrame from the dictionary
    df3 = pd.DataFrame(data3)

    # Display the table
    st.table(df3)

    st.subheader("Working capital assumptions")

    data4 = {
    "Working capital assumptions": ["Receivable Days", "Inventory Days", "Payable Days"],
    "Jan": [7.0, 29.0, 28.0],
    "Feb": [7.0, 29.0, 28.0],
    "Mar": [7.0, 29.0, 28.0],
    "Apr": [7.0, 29.0, 28.0],
    "May": [7.0, 29.0, 28.0],
    "Jun": [7.0, 29.0, 28.0],
    "Jul": [7.0, 29.0, 28.0],
    "Aug": [7.0, 29.0, 28.0],
    "Sep": [7.0, 29.0, 28.0],
    "Oct": [7.0, 29.0, 28.0],
    "Nov": [7.0, 29.0, 28.0],
    "Dec": [7.0, 29.0, 28.0]
}

# Create a DataFrame from the dictionary
    df4 = pd.DataFrame(data4)

    # Display the table
    st.table(df4)

    st.subheader("Capital expenditure assumptions")

    # Create a dictionary with the data
    data5 = {
        "Capital expenditure assumptions": ["Depreciation rate", "Cost to build per square foot"],
        "Jan": ["10.0%", 100.0],
        "Feb": ["10.0%", 100.0],
        "Mar": ["10.0%", 100.0],
        "Apr": ["10.0%", 100.0],
        "May": ["10.0%", 100.0],
        "Jun": ["10.0%", 100.0],
        "Jul": ["10.0%", 100.0],
        "Aug": ["10.0%", 100.0],
        "Sep": ["10.0%", 100.0],
        "Oct": ["10.0%", 100.0],
        "Nov": ["10.0%", 100.0],
        "Dec": ["10.0%", 100.0]
    }

    # Create a DataFrame from the dictionary
    df5 = pd.DataFrame(data5)

    # Display the table
    st.table(df5)

    st.subheader("Financing assumptions")

    data6 = {
        "Financing assumptions": ["Equity raised (repurchased)", "Dividends paid", "Term debt issued",
                                "Term debt principal repayment", "Term debt interest rate",
                                "Debt/Equity ratio covenant", "Debt service coverage ratio covenant"],
        "Jan": [0.0, 0.0, 0.0, 500.0, "5.75%", "0.75x", "3.00x"],
        "Feb": [0.0, 0.0, 0.0, 500.0, "5.75%", "0.75x", "3.00x"],
        "Mar": [0.0, 0.0, 0.0, 500.0, "5.75%", "0.75x", "3.00x"],
        "Apr": [0.0, 0.0, 0.0, 500.0, "5.75%", "0.75x", "3.00x"],
        "May": [0.0, 0.0, 0.0, 500.0, "5.75%", "0.75x", "3.00x"],
        "Jun": [0.0, 0.0, 0.0, 500.0, "5.75%", "0.75x", "3.00x"],
        "Jul": [0.0, 0.0, 0.0, 500.0, "5.75%", "0.75x", "3.00x"],
        "Aug": [0.0, 0.0, 0.0, 500.0, "5.75%", "0.75x", "3.00x"],
        "Sep": [0.0, 0.0, 0.0, 500.0, "5.75%", "0.75x", "3.00x"],
        "Oct": [0.0, 0.0, 0.0, 500.0, "5.75%", "0.75x", "3.00x"],
        "Nov": [0.0, 0.0, 0.0, 500.0, "5.75%", "0.75x", "3.00x"],
        "Dec": [0.0, 0.0, 0.0, 500.0, "5.75%", "0.75x", "3.00x"]
    }

    # Create a DataFrame from the dictionary
    df6 = pd.DataFrame(data6)

    # Display the table
    st.table(df6)

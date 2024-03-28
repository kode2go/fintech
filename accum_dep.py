import streamlit as st
import pandas as pd
import plotly.express as px

from streamlit_lottie import st_lottie
import json

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

def calculate_depreciation(purchase_price, useful_life, salvage_value):
    depreciable_value = purchase_price - salvage_value
    annual_depreciation = depreciable_value / useful_life
    return depreciable_value, annual_depreciation

def accum_dep():

    st.title("Accumulated Depreciation")

    with st.container():
        col1,col2=st.columns(2)
    with col1:
        st.markdown("""This depreciation calculator provides a streamlined approach to estimate asset depreciation using the straight-line method. The user inputs three key parameters: the purchase price of the asset, its useful life in years, and the salvage value anticipated at the end of its useful life. Upon calculation, the tool generates a detailed table displaying the asset's book value, depreciation, accumulated depreciation, and end-of-year book value for each year within the specified useful life.""")

    with col2:
        lottie2 = load_lottiefile("spreadsheet_calc.json")
        st_lottie(lottie2,key='place',height=300,width=300)

    purchase_price = st.number_input('Purchase Price', value=1000)
    useful_life = st.number_input('Useful Life (in years)', value=4)
    salvage_value = st.number_input('Salvage Value', value=200)

    if st.button('Calculate'):
        depreciable_value, annual_depreciation = calculate_depreciation(purchase_price, useful_life, salvage_value)
        data_i = {
            'Purchase Price': [purchase_price],
            'Useful Life': [useful_life],
            'Salvage Value': [salvage_value],
            'Depreciable Value': [depreciable_value],
            'Annual Depreciation (Straight-line)': [annual_depreciation]
        }

        df = pd.DataFrame(data_i)
        st.write(df)

        data = []
        book_value = purchase_price
        accumulated_depreciation = annual_depreciation
        for year in range(1, useful_life + 1):
            data.append([year, book_value, annual_depreciation, accumulated_depreciation, book_value - annual_depreciation])
            accumulated_depreciation += annual_depreciation
            book_value -= annual_depreciation

        columns = ['Year', 'Book Value (Beginning of Year)', 'Depreciation', 'Accumulated Depreciation', 'Book Value (End of Year)']
        df2 = pd.DataFrame(data, columns=columns)
        st.write(df2)

        # Check if Book Value at the end of 4 Years equals Salvage Value
        if df2.iloc[-1]['Book Value (End of Year)'] == salvage_value:
            st.write(f"Yes, Book Value at the end of {useful_life} Years equals Salvage Value")
        else:
            st.write(f"No, Book Value at the end of {useful_life} Years does not equal Salvage Value")

        # df['Year'] = df['Year'].astype(str) 

        # Plot the data
        fig = px.line(df2, x='Year', y=['Book Value (Beginning of Year)', 'Depreciation', 'Accumulated Depreciation', 'Book Value (End of Year)'],
                      title='Depreciation Over Time')
        st.plotly_chart(fig)

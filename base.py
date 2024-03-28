import streamlit as st
from streamlit_lottie import st_lottie
import json

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

def base():
    #Header
    st.title('Welcome to Zenkos Investments (Pty) Ltd')
    st.subheader('*African Market Forecasting Platform*')

    st.divider()

    #Use Cases
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.header('Overiew')
            st.markdown(
                """
The objective of this project is to develop African Financial AI, a
comprehensive market forecasting and analysis platform tailored specifically
for the African market. African Financial AI aims to provide global investors
with accurate, timely, and actionable insights into investment opportunities
across various regions and sectors in Africa. By leveraging cutting-edge
technologies, open-source APIs, and advanced financial modeling tools, the
platform will empower investors to make informed decisions, mitigate risks,
and maximize returns in one of the world's fastest-growing regions.
                """
                )
        with col2:
            lottie2 = load_lottiefile("place2.json")
            st_lottie(lottie2,key='place',height=300,width=300)

    st.divider()

    st.header("Financial Services")
    categories = [
        ("Active Listening Diagnostic", "Tool for assessing and improving one's ability to actively listen and comprehend information."),
        ("12 Month Rolling Forecast", "Generates forecasts for the next 12 months based on historical data, aiding in planning and budgeting."),
        ("Accumulated Depreciation Template", "Helps track the total depreciation of assets over time for accounting purposes."),
        ("Activity-Based Costing Template", "Allocates costs to products or services based on the activities they require."),
        ("Additional Paid-in-Capital Template", "Tracks the amount of capital contributed by shareholders beyond the par value of stock."),
        ("Alpha Calculator", "Computes the risk-adjusted return of an investment compared to the market index."),
        ("Annual Income Calculator", "Calculates the total income earned over a year, aiding in financial planning."),
        ("Appraisal Checklist", "A checklist used by appraisers to ensure all relevant factors are considered during appraisal."),
        ("Balance Sheet Current Assets Template", "Provides a template for listing and calculating current assets on a balance sheet."),
        ("Bank Reconciliation Statement", "Compares the bank statement with the company's records to ensure accuracy and reconcile any discrepancies."),
        ("Beneish M-Score Calculator", "Calculates the M-Score, a model used to detect earnings manipulation in financial statements."),
        ("Beta Calculator", "Determines the volatility of an investment compared to the market as a whole.")
    ]



    st.markdown("| Tool Name | Description |\n| --- | --- |\n" + "\n".join([f"| {tool} | {description} |" for tool, description in categories]))

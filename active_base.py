import streamlit as st
import pandas as pd
import plotly.express as px

from streamlit_lottie import st_lottie
import json

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

def calculate_overhead_rate(row):
    estimated_overhead = row['Estimated Manufacturing Overhead']
    total_per_activity = row['Total Per Activity']
    if total_per_activity == 0:
        return 0
    else:
        return estimated_overhead / total_per_activity

def active_base():

    st.title("Activity Based Costing - Allocating Overhead Costs")

    with st.container():
        col1,col2=st.columns(2)
    with col1:
        st.markdown("""The app presents a table displaying various manufacturing activities 
        along with their estimated manufacturing overhead and total per activity. 
        Users can edit these values directly within the table using an interactive data editor. 
        Upon editing, the app dynamically recalculates the overhead rate for each activity a
        nd updates the display accordingly. Additionally, the app calculates and displays 
        the total estimated manufacturing overhead across all activities. 
        The interface is divided into two columns,
         with the editable table on the left and the updated overhead rates on the right.""")

    with col2:
        lottie2 = load_lottiefile("abacus.json")
        st_lottie(lottie2,key='place',height=300,width=300)

        # Define data
    data = {
        'Activity': ['Labour Related', 'Machine setups', 'Part administration', 
                     'Production Orders', 'Material Receipts', 'General factory machine hours'],
        'Estimated Manufacturing Overhead': [80000.00, 150000.00, 160000.00, 70000.00, 90000.00, 250000.00],
        'Total Per Activity': [50000, 5000, 80, 400, 750, 40000],
        'Unit': ["hours","setupts","parts","orders","receipts","machine hours"],

    }
    
    # Create DataFrame
    df = pd.DataFrame(data)

    with st.container():
        col1,col2=st.columns([3,1])
    with col1:
        # Display editable DataFrame
        edited_df = st.data_editor(df, hide_index=True)
        # Recalculate overhead rate
        edited_df['Overhead Rate (per activity)'] = edited_df.apply(calculate_overhead_rate, axis=1)
        total_overhead = edited_df['Estimated Manufacturing Overhead'].sum()
        st.write(f'Total Estimated Manufacturing Overhead: ${total_overhead:.2f}')

    with col2:
        # Display updated DataFrame
        st.dataframe(edited_df['Overhead Rate (per activity)'], hide_index=True)
        
    

    

    

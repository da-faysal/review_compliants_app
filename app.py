# Import required modules
import pandas as pd
import streamlit as st
import plotly.graph_objs as go

# Read in the compliant data extract from reviews

df_janets =  pd.read_csv("janets.csv")
df_cg = pd.read_csv("cg.csv")

# Select a provider
provider_options = st.sidebar.selectbox("Select a provider", ["One Education", "Janets", "Course Gate"])



# Set title
st.title("Compliants Frequency by Brands")


# If "One education" is selected
if provider_options=="One Education":

    # Read in one edu data
    df_one = pd.read_csv("one.csv")

    # Create trace
    trace = go.Pie(labels=df_one.issue, 
                        values=df_one.frequency,
                        rotation=90)
    # Create layout                    
    layout = go.Layout(
                    title="One Education's Percent Compliants Ratio",
                    font=dict(family='Arial', size=13, color='#909090')
                    )
    # Create figure obj
    fig = go.Figure(data=[trace], layout=layout)
    st.plotly_chart(fig)
    # Write takeaway from the plot
    st.markdown("**Takeaway: Over 32% compliants are associated with content (free or not satisfactory content) while 12.5% are related to late replies.**")


# if "Janets" is selected
if provider_options=="Janets":

    # Read in one edu data
    df_janets = pd.read_csv("janets.csv")

    # Create trace
    trace = go.Pie(labels=df_janets.issue, 
                        values=df_janets.frequency,
                        rotation=90)
    # Create layout                    
    layout = go.Layout(
                    title="Janets's Percent Compliants Ratio",
                    font=dict(family='Arial', size=13, color='#909090')
                    )
    # Create figure obj
    fig = go.Figure(data=[trace], layout=layout)
    st.plotly_chart(fig)
    # Write takeaway from the plot
    st.markdown("**Takeaway: There are only 2 types of compliants. 60% are associated with content (free or not satisfactory content) while 40% are exam issues (question quality problem).**")


# if "Course gate" is selected
if provider_options=="Course Gate":

    # Read in one edu data
    df_cg = pd.read_csv("cg.csv")

    # Create trace
    trace = go.Pie(labels=df_cg.issue, 
                        values=df_cg.frequency,
                        rotation=90)
    # Create layout                    
    layout = go.Layout(
                    title="Course Gate's Percent Compliants Ratio",
                    font=dict(family='Arial', size=13, color='#909090')
                    )
    # Create figure obj
    fig = go.Figure(data=[trace], layout=layout)
    st.plotly_chart(fig)
    # Write takeaway from the plot
    st.markdown("**Takeaway: Almost 28% compliants were related to content (free or not satisfactory) while over 22% were related to 'us reference'. Over 11% compliants were related to 'certificate'.**")

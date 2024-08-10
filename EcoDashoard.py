import streamlit as st
import os
from openai import OpenAI
import numpy as np
import pandas as pd
import PyPDF2
import random
import pinecone
import io
import plotly.express as px

from pinecone import Pinecone
from PIL import Image
from io import BytesIO
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame

# BUILDING COUNTRY ECONOMY COMPARISON # 

# Load the CSV file
#@st.cache  # Use caching to load the CSV only once
def load_data():
    path = "c1.csv"  # Adjust path accordingly
    return pd.read_csv(path)

df = load_data()

# Allow the user to select a country
country = st.sidebar.selectbox('Select a Country', df['Country'].unique())

# Filter data based on the selected country
filtered_df = df[df['Country'] == country]

# Create Plotly graphs
def create_graphs(df):
    fig0 = px.bar(df, x='Year', y='Gross domestic product, (constant prices US$)', title="Bar Chart")
    fig1 = px.line(df, x='Year', y='Real GDP growth (annual %)', title="Line Plot")
    fig2 = px.bar(df, x='Year', y='Inflation, consumer prices (annual %)', title="Inflation per Year")
    fig3 = px.scatter(df, x='Real GDP growth (annual %)', y='Inflation, consumer prices (annual %)', title="Scatter Plot")
    fig4 = px.histogram(df, x='Real GDP growth (annual %)', title="Histogram")
    fig5 = px.bar(df, y='Real per Capita GDP Growth Rate (annual %)', title="Real per Capita GDP Growth Rate (annual %)")
    fig6 = px.bar(df, x='Year', y='Exports of goods and services (current US$)', title="Exports of Goods and Services per Year")
    fig7 = px.bar(df, x='Year', y='Imports of goods and services (current US$)', title="Imports of Goods and Services per Year")
    fig8 = px.bar(df, x='Year', y='Gross domestic product, current prices (current US$)', title="Bar Chart")
    fig9 = px.violin(df, y='Exports of goods and services (current US$)', title="Violin Plot")
    fig10 = px.area(df, x='Year', y='Current account balance (Net, BoP, cur. US$)', title="Area Chart")
    return [fig0, fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10]

# Update other parts of your code to remove references to the now non-existent unemployment rate graph.



# Create graphs
graphs = create_graphs(filtered_df)

# Sidebar for graph selection
graph_selection = st.sidebar.multiselect(
    "Select Graphs to Display",
    ["Bar Chart", "Line Plot", "Inflation per Year", "Scatter Plot", "Histogram", "Real per Capita GDP Growth Rate (annual %)", "Exports of Goods and Services per Year", "Imports of Goods and Services per Year", "Pie Chart", "Violin Plot", "Area Chart"],
    ["Bar Chart", "Line Plot", "Inflation per Year", "Scatter Plot", "Histogram", "Real per Capita GDP Growth Rate (annual %)", "Exports of Goods and Services per Year", "Imports of Goods and Services per Year", "Pie Chart",  "Violin Plot", "Area Chart"]
)

# Map selected graphs to corresponding Plotly figures
graph_map = {
    "Bar Chart": graphs[0],
    "Line Plot": graphs[1],
    "Inflation per Year": graphs[2],
    "Scatter Plot": graphs[5],
    "Histogram": graphs[6],
    "Real per Capita GDP Growth Rate (annual %)": graphs[7],
    "Exports of Goods and Services per Year": graphs[3],
    "Imports of Goods and Services per Year": graphs[4],
    "Pie Chart": graphs[8],
    "Violin Plot": graphs[9],
    "Area Chart": graphs[10],
    #"GDP per Capita per Year": graphs[11],
    #"Unemployment Rate per Year": graphs[12],
    #"Government Debt to GDP Ratio per Year": graphs[12],
    #"Total Population per Year": graphs[13],
    #"Area Chart": graphs[14],
    #"FDI Inflow per Year": graphs[15]
}

# Display selected graphs in a single column and centered
for graph_name in graph_selection:
    st.plotly_chart(graph_map[graph_name], use_container_width=True)

# END OF BUILDING COUNTRY ECONOMY COMPARISON #


# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Ensure the entire app background is consistently applied */
        .stApp {
            background-color: #F4F4FF !important;
            padding: 00px;
        }

        /* Adjust the background color of the main content area */
        .block-container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
            margin-top: 80px;
            margin-bottom: 20px;
        }

        /* Styling for the generated text box */
        .generated-box {
            background-color: #F4F4FF;
            padding: 20px;
            border: 1px solid #0000001A;
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            white-space: pre-wrap; /* Preserve line breaks */
        }

        /* Style the header and subheader */
        h1, h2, h3 {
            color: #000;
            margin-bottom: 20px;
        }

        /* Style the buttons */
        button {
            background: #0025B8 !important;
            color: #fff !important;
            border: none !important;
            display: flex !important;
            width: fit-content !important;
            margin: auto !important;
        }

        button p {
            color: #fff !important;
        }

        /* General paragraph styling */
        p {  
            color: #000;
            font-size: 16px !important;
        }

        /* Style the links in the list */
        ul li a {
            padding: 10px 12px;
        }

        /* Centering specific elements */
        #blog-generator {
            text-align: center;
        }

        .stMarkdown {
            text-align: justify;
        }

        .eczjsme18 {
            background: #fff;
        }

        .st-ae {
            background: #F4F4FF;
            border: none;
        }

        .st-ae:focus {
            outline: none !important;
        }

        .st-emotion-cache-5k5r22:active {
            color: red !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)



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


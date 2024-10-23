import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pyvis.network import Network
import networkx as nx
import streamlit.components.v1 as components
from plotly.subplots import make_subplots

###################
# Data Loading
###################

@st.cache_data
def load_data():
    """Load and cache the comorbidity dataset"""
    try:
        df = pd.read_csv('assets/data/comorbidites.csv', delimiter=';', on_bad_lines='skip', na_values=[''])
        # Convert annee to int, handling any non-numeric values
        df['annee'] = pd.to_numeric(df['annee'], errors='coerce')
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return pd.DataFrame()

###################
# Helper Functions
###################

def filter_data(df, year=None, pathology=None):
    """Filter dataset by year and/or pathology"""
    filtered_df = df.copy()
    if year and not filtered_df.empty:
        filtered_df = filtered_df[filtered_df['annee'] == year]
    if pathology and not filtered_df.empty:
        filtered_df = filtered_df[filtered_df['patho_niv1'] == pathology]
    return filtered_df

def get_top_frequent(df, column, top_n=10):
    """Get the top N most frequent values in a column"""
    if df.empty or column not in df.columns:
        return []
    return df[column].dropna().value_counts().nlargest(top_n).index.tolist()

###################
# Basic Visualizations
###################

def explore_missing_data(df):
    """Create visualization for missing data patterns"""
    if df.empty:
        st.error("No data available for missing data analysis")
        return

    st.title("Exploring Missing Data Patterns")

    fig = make_subplots(rows=2, cols=1, 
                       subplot_titles=("Missing Comorbidities by Year", 
                                     "Missing Comorbidities by Pathology Level 1"))

    # Missing data by year
    missing_by_year = df.groupby('annee')['ncomorb'].apply(
        lambda x: x.isnull().sum()
    ).reset_index()
    fig.add_trace(
        go.Scatter(x=missing_by_year['annee'], 
                  y=missing_by_year['ncomorb'],
                  mode='lines+markers',
                  name='Missing by Year'),
        row=1, col=1
    )

    # Missing data by pathology
    missing_by_pathology1 = df.groupby('patho_niv1')['ncomorb'].apply(
        lambda x: x.isnull().sum()
    ).reset_index().sort_values('ncomorb', ascending=False)
    
    fig.add_trace(
        go.Bar(x=missing_by_pathology1['patho_niv1'],
               y=missing_by_pathology1['ncomorb'],
               name='Missing by Pathology'),
        row=2, col=1
    )

    fig.update_layout(height=800, title_text="Missing Data Analysis")
    fig.update_xaxes(title_text="Year", row=1, col=1)
    fig.update_xaxes(title_text="Pathology Level 1", row=2, col=1)
    fig.update_yaxes(title_text="Number of Missing Comorbidities", row=1, col=1)
    fig.update_yaxes(title_text="Number of Missing Comorbidities", row=2, col=1)

    st.plotly_chart(fig, use_container_width=True)

def analyze_pathology_distribution(df):
    """Analyze and visualize pathology distribution for a selected year"""
    if df.empty:
        st.error("No data available for pathology distribution analysis")
        return

    st.title("Pathology Distribution Analysis")
    
    # Get available years for selection
    available_years = sorted(df['annee'].dropna().unique())
    if not available_years:
        st.error("No valid years found in the dataset")
        return

    selected_year = st.select_slider(
        "Select Year",
        options=available_years
    )
    
    year_df = df[df['annee'] == selected_year]
    if year_df.empty:
        st.warning(f"No data available for year {selected_year}")
        return

    top_pathologies = year_df.groupby('patho_niv1')['ncomorb'].sum().nlargest(10)
    
    fig = px.pie(
        values=top_pathologies.values,
        names=top_pathologies.index,
        title=f'Top 10 Pathologies Distribution in {selected_year}'
    )
    
    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        hovertemplate="<b>%{label}</b><br>" +
                     "Count: %{value}<br>" +
                     "Percentage: %{percent}<extra></extra>"
    )
    
    fig.update_layout(
        height=600,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,
            xanchor="center",
            x=0.5
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        total_cases = year_df['ncomorb'].sum()
        st.metric("Total Cases", f"{total_cases:,.0f}")
    with col2:
        unique_pathologies = len(year_df['patho_niv1'].unique())
        st.metric("Unique Pathologies", unique_pathologies)

###################
# Advanced Visualizations
###################

def create_hierarchical_pathology_explorer(df):
    """Create interactive hierarchical visualization of pathologies"""
    if df.empty:
        st.error("No data available for hierarchical pathology exploration")
        return

    st.subheader("Hierarchical Pathology Explorer")
    
    available_years = sorted(df['annee'].dropna().unique())
    if not available_years:
        st.error("No valid years found in the dataset")
        return

    selected_year = st.select_slider(
        "Select Year",
        options=available_years,
        key="hierarchical_explorer_year"
    )
    
    # Filter data for selected year
    hierarchical_df = df[df['annee'] == selected_year].copy()
    
    # Handle missing values
    hierarchical_df['patho_niv2'] = hierarchical_df['patho_niv2'].fillna('Non spécifié')
    hierarchical_df['patho_niv3'] = hierarchical_df['patho_niv3'].fillna('Non spécifié')
    
    # Create hierarchical grouping
    grouped_df = (hierarchical_df.groupby(['patho_niv1', 'patho_niv2', 'patho_niv3'])
                 ['ncomorb'].sum()
                 .reset_index())
    
    if grouped_df.empty:
        st.warning(f"No hierarchical data available for year {selected_year}")
        return

    fig = px.sunburst(
        grouped_df,
        path=['patho_niv1', 'patho_niv2', 'patho_niv3'],
        values='ncomorb',
        title=f'Pathology Hierarchy Distribution in {selected_year}'
    )
    
    fig.update_layout(
        height=700,
        uniformtext=dict(minsize=10, mode='hide')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    This sunburst chart shows the hierarchical relationship between different levels of pathologies:
    - The inner circle represents Level 1 pathologies
    - The middle ring shows Level 2 pathologies
    - The outer ring displays Level 3 pathologies
    - The size of each section represents the number of comorbidities
    - Click on a section to zoom in and explore that branch of the hierarchy
    """)

def create_priority_distribution(df):
    """Create animated scatter plot of priority level distribution"""
    if df.empty:
        st.error("No data available for priority distribution analysis")
        return

    st.subheader("Priority Level Distribution Over Time")
    
    # Create a copy of the dataframe and handle missing values
    plot_df = df.copy()
    
    # Fill NaN values in ntop with the minimum non-zero value or 1
    min_ntop = plot_df['ntop'].dropna().min()
    plot_df['ntop'] = plot_df['ntop'].fillna(min_ntop if pd.notna(min_ntop) else 1)
    
    # Create the scatter plot
    fig = px.scatter(
        plot_df,
        x='proportion_comorb',
        y='ncomorb',
        size='ntop',
        color='niveau_prioritaire',
        animation_frame='annee',
        hover_name='patho_niv1',
        size_max=60,
        title='Priority Level Distribution (Play to see changes over time)',
        labels={
            'proportion_comorb': 'Comorbidity Proportion (%)',
            'ncomorb': 'Number of Comorbidities',
            'niveau_prioritaire': 'Priority Level'
        }
    )
    
    fig.update_layout(
        height=600,
        xaxis_title="Comorbidity Proportion (%)",
        yaxis_title="Number of Comorbidities",
        showlegend=True,
        legend_title="Priority Level"
    )
    
    fig.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>" +
                      "Comorbidity Proportion: %{x:.1f}%<br>" +
                      "Number of Comorbidities: %{y}<br>" +
                      "Priority Level: %{marker.color}<br>" +
                      "<extra></extra>"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    This visualization shows the relationship between:
    - Comorbidity Proportion (x-axis)
    - Number of Comorbidities (y-axis)
    - Priority Level (color)
    - Classification Count (bubble size)
    
    Play the animation to see how these relationships evolve over time.
    """)

def create_multilevel_comparison(df):
    """Create interactive multilevel pathology comparison"""
    if df.empty:
        st.error("No data available for multilevel comparison")
        return

    st.subheader("Multi-Level Pathology Analysis")
    
    # Handle NaN values in patho_niv1
    valid_level1 = df['patho_niv1'].dropna().unique()
    if len(valid_level1) == 0:
        st.error("No valid primary pathologies found")
        return
    
    col1, col2 = st.columns(2)
    with col1:
        selected_level1 = st.selectbox(
            "Select Primary Pathology",
            options=sorted(valid_level1)
        )
    
    # Handle NaN values in patho_niv2 for the selected level1
    level2_mask = (df['patho_niv1'] == selected_level1) & df['patho_niv2'].notna()
    level2_options = df[level2_mask]['patho_niv2'].unique()
    
    if len(level2_options) == 0:
        st.warning(f"No secondary pathologies found for {selected_level1}")
        return
    
    with col2:
        selected_level2 = st.selectbox(
            "Select Secondary Pathology",
            options=sorted(level2_options)
        )
    
    # Filter data for visualization
    filtered_df = df[
        (df['patho_niv1'] == selected_level1) &
        (df['patho_niv2'] == selected_level2)
    ].copy()
    
    # Handle NaN values in patho_niv3
    filtered_df['patho_niv3'] = filtered_df['patho_niv3'].fillna('Non spécifié')
    
    if len(filtered_df) > 0:
        fig = px.line(
            filtered_df,
            x='annee',
            y='ncomorb',
            color='patho_niv3',
            title=f'Evolution of Level 3 Pathologies for {selected_level2}',
            markers=True
        )
        
        fig.update_layout(
            height=600,
            xaxis_title="Year",
            yaxis_title="Number of Comorbidities",
            legend_title="Level 3 Pathology"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for the selected combination of pathologies.")

def analyze_comorbidity_pairs(df):
    """Analyze and visualize top comorbidity pairs"""
    if df.empty:
        st.error("No data available for comorbidity pairs analysis")
        return

    st.subheader("Top Comorbidity Pairs Analysis")
    
    available_years = sorted(df['annee'].dropna().unique())
    if not available_years:
        st.error("No valid years found in the dataset")
        return

    selected_year = st.select_slider(
        "Select Year",
        options=available_years,
        key="comorbidity_pairs_year"
    )
    
    year_df = df[df['annee'] == selected_year]
    if year_df.empty:
        st.warning(f"No data available for year {selected_year}")
        return

    pairs_df = year_df.groupby(
        ['patho_niv1', 'patho_niv1_comorb']
    )['proportion_comorb'].mean().reset_index()
    
    if pairs_df.empty:
        st.warning("No valid comorbidity pairs found")
        return

    top_pairs = pairs_df.nlargest(15, 'proportion_comorb')
    
    fig = px.bar(
        top_pairs,
        x='proportion_comorb',
        y='patho_niv1',
        color='patho_niv1_comorb',
        orientation='h',
        title=f'Top 15 Comorbidity Pairs in {selected_year}',
        labels={
            'proportion_comorb': 'Comorbidity Proportion',
            'patho_niv1': 'Primary Pathology',
            'patho_niv1_comorb': 'Comorbidity'
        }
    )
    
    fig.update_layout(height=800, showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

def create_interactive_network(df, top_pathologies, top_comorbidities):
    """Create interactive network visualization"""
    if df.empty or not top_pathologies or not top_comorbidities:
        st.error("Insufficient data for network visualization")
        return

    st.subheader("Interactive Pathology-Comorbidity Network")

    G = nx.Graph()
    
    for _, row in df.iterrows():
        pathology = row['patho_niv1']
        comorbidity = row['patho_niv1_comorb']
        
        if (pathology in top_pathologies and 
            pd.notna(comorbidity) and 
            comorbidity in top_comorbidities):
            # Scale weight to be between 1 and 10 for better visualization
            weight = min(10, max(1, row['proportion_comorb'] / 10))
            G.add_edge(pathology, comorbidity, weight=weight)

    if not G.nodes():
        st.warning("No valid connections found for network visualization")
        return

    net = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')
    net.from_nx(G)
    net.repulsion(
        node_distance=200,
        central_gravity=0.2,
        spring_length=200,
        spring_strength=0.05
    )

    # Customize node appearances
    for node in net.nodes:
        if node['id'] in top_pathologies:
            node['color'] = '#ff9999'  # Light red for pathologies
            node['size'] = 30
            node['title'] = f"Pathology: {node['id']}"
        else:
            node['color'] = '#99ccff'  # Light blue for comorbidities
            node['size'] = 20
            node['title'] = f"Comorbidity: {node['id']}"

    # Add legend
    legend_html = """
    <div style="position: absolute; top: 10px; left: 10px; background-color: rgba(255,255,255,0.7); 
         padding: 10px; border-radius: 5px;">
        <div><span style="color: #ff9999;">●</span> Top Pathologies</div>
        <div><span style="color: #99ccff;">●</span> Comorbidities</div>
        <div style="font-size: 0.8em; margin-top: 5px;">
            Drag nodes to explore relationships.<br>
            Zoom with mouse wheel.<br>
            Click nodes to highlight connections.
        </div>
    </div>
    """

    try:
        net_html = net.generate_html()
        net_html = net_html.replace('</body>', legend_html + '</body>')
        st.components.v1.html(net_html, height=800)
    except Exception as e:
        st.error(f"Error generating network visualization: {str(e)}")

import plotly.express as px
import streamlit as st

import plotly.express as px
import streamlit as st

def plot_top_comorbidities_over_time(df):
    """Plot specified top 5 comorbidities over time"""
    if df.empty:
        st.error("No data available for top comorbidities analysis")
        return

    st.subheader("Top 5 Comorbidities Over Time")

    try:
        # Define the specific comorbidities we want to track
        selected_comorbidities = [
            'Traitements antihypertenseurs (hors pathologies)',
            'Diabète',
            'Traitements anxiolytiques (hors pathologies)',
            'Maladies respiratoires chroniques (hors mucoviscidose)',
            'Traitements antidépresseurs ou régulateurs de l\'humeur (hors pathologies)'
        ]

        # Filter for only these comorbidities and aggregate by year
        top_comorbidities = (df[df['patho_niv1'].isin(selected_comorbidities)]
                            .groupby(['patho_niv1', 'annee'])['ncomorb']
                            .sum()
                            .reset_index())

        if top_comorbidities.empty:
            st.warning("No data found for the specified comorbidities")
            return

        # Create the line plot with markers for each year
        fig = px.line(
            top_comorbidities,
            x='annee',
            y='ncomorb',
            color='patho_niv1',
            title='Top 5 Comorbidities Over Time',
            labels={
                'ncomorb': 'Number of Cases',
                'annee': 'Year',
                'patho_niv1': 'Comorbidity'
            },
            line_shape='linear',
            color_discrete_sequence=['#1f77b4', '#2ca02c', '#d62728', '#ff7f0e', '#9467bd']  # Custom colors to match your chart
        )

        # Customize the layout to match the look of the graph
        fig.update_layout(
            height=600,
            legend_title_text="Comorbidity",
            yaxis_tickformat=",",
            hovermode='x unified',
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.4,
                xanchor="center",
                x=0.5
            ),
            yaxis=dict(
                rangemode='tozero'  # Start y-axis at zero
            ),
            margin=dict(l=40, r=40, t=40, b=40)
        )

        # Adjust line styles and add markers
        fig.update_traces(
            line=dict(width=3),
            mode='lines+markers',  # Add markers to the lines
            marker=dict(size=8)
        )

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Error generating top comorbidities plot: {str(e)}")


def show_insights():
    """Main function to display all insights and visualizations"""
    try:
        df = load_data()
        
        if df.empty:
            st.error("Unable to load dataset. Please check if the data file exists and is accessible.")
            return

        st.title("Comorbidity Dataset Insights")
        st.write("""
        This analysis explores patterns and relationships in comorbidity data across different pathologies and years.
        Use the visualizations below to understand various aspects of the dataset.
        """)

        # Create a sidebar for global filters
        st.sidebar.title("Global Filters")
        st.sidebar.info("""
        Some visualizations have their own specific filters.
        Use the sidebar filters for the network analysis section.
        """)

        # Create tabs for different analysis sections
        tabs = st.tabs([
            "Overview",
            "Missing Data",
            "Pathology Distribution",
            "Hierarchical Analysis",
            "Priority Analysis",
            "Multilevel Comparison",
            "Comorbidity Pairs",
            "Network Analysis",
            "Top 5 Comorbidities"
        ])

        # Overview tab
        with tabs[0]:
            st.header("Dataset Overview")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Records", f"{len(df):,}")
            with col2:
                year_min = df['annee'].min()
                year_max = df['annee'].max()
                if pd.notna(year_min) and pd.notna(year_max):
                    st.metric("Year Range", f"{year_min:.0f} - {year_max:.0f}")
                else:
                    st.metric("Year Range", "No valid years")
            with col3:
                st.metric("Unique Pathologies", f"{df['patho_niv1'].nunique():,}")
            
            st.subheader("Quick Statistics")
            st.dataframe(df.describe(include='all'), use_container_width=True)

        # Populate other tabs with corresponding visualizations
        with tabs[1]:
            explore_missing_data(df)
        
        with tabs[2]:
            analyze_pathology_distribution(df)
        
        with tabs[3]:
            create_hierarchical_pathology_explorer(df)
        
        with tabs[4]:
            create_priority_distribution(df)
        
        with tabs[5]:
            create_multilevel_comparison(df)
        
        with tabs[6]:
            analyze_comorbidity_pairs(df)
        
        with tabs[7]:
            # Network Analysis Options
            st.sidebar.subheader("Network Analysis Options")
            
            # Year selection
            available_years = sorted(df['annee'].dropna().unique().astype(int))
            selected_year = st.sidebar.selectbox(
                "Select Year",
                options=[None] + available_years,
                format_func=lambda x: 'All Years' if x is None else str(x)
            )
            
            # Pathology selection
            available_pathologies = sorted(df['patho_niv1'].dropna().unique())
            selected_pathology = st.sidebar.selectbox(
                "Select Pathology",
                options=[None] + available_pathologies,
                format_func=lambda x: 'All Pathologies' if x is None else str(x)
            )

            # Filter data based on selections
            filtered_data = filter_data(df, year=selected_year, pathology=selected_pathology)
            
            if not filtered_data.empty:
                top_pathologies = get_top_frequent(filtered_data, 'patho_niv1', top_n=10)
                top_comorbidities = get_top_frequent(filtered_data, 'patho_niv1_comorb', top_n=10)
                create_interactive_network(filtered_data, top_pathologies, top_comorbidities)
            else:
                st.warning("No data available for the selected filters")

        with tabs[8]:
            plot_top_comorbidities_over_time(df)

        # Add footer
        st.markdown("""---""")
        st.markdown("""
        <div style='text-align: center; color: grey;'>
        This dashboard provides comprehensive analysis of comorbidity data.<br>
        For questions or support, please contact the data team.
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"An error occurred while generating insights: {str(e)}")
        st.exception(e)

if __name__ == "__main__":
    show_insights()

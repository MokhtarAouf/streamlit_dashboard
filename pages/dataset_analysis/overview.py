import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Function to load CSV data with semicolon delimiter
def load_data():
    return pd.read_csv('assets/data/comorbidites.csv', delimiter=';', on_bad_lines='skip', na_values=[''])

def show_overview():
    st.title("Dataset Overview")
    
    # Load the data
    df = load_data()
    
    if df is not None:
        # 1. Preview of the Data
        st.subheader("Dataset Preview")
        st.dataframe(df.head())
        
        # 2. Shape of the Dataset
        st.subheader("Dataset Structure")
        col1, col2 = st.columns(2)
        col1.metric("Number of Rows", df.shape[0])
        col2.metric("Number of Columns", df.shape[1])
        
        # 3. Summary Statistics for Numerical Columns
        st.subheader("Summary Statistics")
        st.dataframe(df.describe())
        
        # 4. Missing Values
        st.subheader("Missing Values Visualization")
        missing_values = df.isnull().sum()
        missing_values = missing_values[missing_values > 0]
        if not missing_values.empty:
            fig = px.bar(x=missing_values.index, y=missing_values.values,
                         labels={'x': 'Columns', 'y': 'Missing Values'},
                         title='Missing Values per Column')
            st.plotly_chart(fig)
        else:
            st.info("No missing values in the dataset.")
        
        # 5. Categorical Columns Summary
        st.subheader("Categorical Columns Summary")
        categorical_cols = df.select_dtypes(include=['object']).columns
        selected_cat_col = st.selectbox("Select a categorical column:", categorical_cols)
        if selected_cat_col:
            top_categories = df[selected_cat_col].value_counts().head(10)
            fig = px.pie(values=top_categories.values, names=top_categories.index,
                         title=f'Top 10 Categories in {selected_cat_col}')
            st.plotly_chart(fig)
        
        # 6. Data Types and Column Names
        st.subheader("Column Names and Data Types")
        st.dataframe(df.dtypes.reset_index().rename(columns={'index': 'Column', 0: 'Data Type'}))
        
        # 7. Detecting Outliers
        st.subheader("Outlier Detection")
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        selected_num_col = st.selectbox("Select a numeric column for outlier detection:", numeric_cols)
        if selected_num_col:
            fig, ax = plt.subplots()
            sns.boxplot(x=df[selected_num_col], ax=ax)
            st.pyplot(fig)
        
        # 8. Detecting Duplicate Rows
        st.subheader("Duplicate Rows")
        duplicate_rows = df.duplicated().sum()
        st.metric("Number of duplicate rows", duplicate_rows)
        
        # 9. Year Distribution
        st.subheader("Year Distribution")
        year_counts = df['annee'].value_counts().sort_index()
        fig = px.line(x=year_counts.index, y=year_counts.values,
                      labels={'x': 'Year', 'y': 'Count'},
                      title='Distribution of Data Across Years')
        st.plotly_chart(fig)
        
        # 10. Top Comorbidities
        st.subheader("Top Comorbidities")
        top_comorbidities = df.groupby('libelle_comorbidite')['ncomorb'].sum().sort_values(ascending=False).head(10)
        fig = px.bar(x=top_comorbidities.index, y=top_comorbidities.values,
                     labels={'x': 'Comorbidity', 'y': 'Total Count'},
                     title='Top 10 Comorbidities')
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig)

if __name__ == "__main__":
    show_overview()

import streamlit as st
import pandas as pd
import numpy as np

"# Uber Pickups in New York"

DATE_COLUMN = "date/time"
DATA_URL = (
    "https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)


@st.cache_data
def load_data(nrows):
    """
    Load a dataframe from a CSV file and preprocess it.

    Parameters
    ----------
    nrows : int
        The number of rows to read from the file.

    Returns
    -------
    df : pandas.DataFrame
        The dataframe with lowercase column names and parsed dates.
    """
    df = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    df.rename(lowercase, axis="columns", inplace=True)
    df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN])
    return df


loading_state = st.text("Loading data...🔃")

df = load_data(nrows=10000)

loading_state.text("Here is the data 😎")

st.write(df.head())

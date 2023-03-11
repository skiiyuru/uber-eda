import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

"# Uber Pickups in New York"
# st.header("Uber Pickups in New York")

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

loading_state.text("")


if st.checkbox("Show data"):
    "## Raw data"
    df

"## Number of pickups by hour"

# Use NumPy to generate a histogram that breaks down pickup times binned by hour:
hours = df[DATE_COLUMN].dt.hour
hist_values, bin_edges = np.histogram(hours, bins=24, range=(0, 24))

# plot the chart
st.bar_chart(hist_values)

"## Map of pickups"
# filter pickups for busiest hour

# peak_hour = np.argmax(hist_values)
# df_filtered = df[hours == peak_hour]

# if st.checkbox(f"Only peak hour: {peak_hour}:00 Hrs"):
#     st.map(df_filtered)
# else:
#     st.map(df)


filtered_hour = st.slider("Hour", 0, 23, 17)  # min: 0h, max: 23h, default: 17h
df_filtered = df[hours == filtered_hour]
st.map(df_filtered)

"## How I built this"

st.markdown("Check out the code [here](https://github.com/skiiyuru/uber-eda)")


import streamlit as st
import pandas as pd
import numpy as np

st.tilte('전세계 코로나 뎅터 분석')

coronaDf = pd.reas_csv('covid_19_clean_complete')

st.dataframe(data = coronaDf)

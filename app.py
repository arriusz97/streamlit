import streamlit as st
import pandas as pd
import numpy as np

st.title('전세계 코로나 데이터터 분석')

coronaDf = pd.read_csv('covid_19_clean_complete.csv')

st.dataframe(data = coronaDf)

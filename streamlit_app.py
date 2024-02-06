import streamlit as st
import pandas as pd
st.title('My Project')
data= dict(volume=[3.5, 4.5, 8.5, 9.5, 5.5], mass=[10, 11, 12, 13, 14], velocity=[2, 5, 7, 9, 11])
df= pd.DataFrame(data)
st.table(df)


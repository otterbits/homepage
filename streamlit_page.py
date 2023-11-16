import streamlit as st
st.write('# Youtube view')
st.write('## view')
view = [100,150,30]
view
st.write('## bar chart')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview
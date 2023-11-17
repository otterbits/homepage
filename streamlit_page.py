import streamlit as st
import numpy as np

st.title('Welcome to :rainbow[Otterbit] world')
st.write('## coding is very :red[_awesome_] :sunglasses:')

st.divider()
st.link_button("youtube", "https://www.youtube.com/@racoonByteotterBit/")
tab1, tab2, tab3 = st.tabs(["INTRO", "PROJECT", "STUDY"])


with tab1:
   st.header("hello otter!")
   st.video('https://youtu.be/u52CGaPWk1M?feature=shared', format='video/mp4')

with tab2:
   st.header("working hard with communication")

with tab3:
   st.header("study knowledge")
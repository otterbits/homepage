import streamlit as st
import numpy as np

st.title('Welcome to :rainbow[Otterbit] world')
st.write('## coding is very :red[_awesome_] :sunglasses:')

st.divider()
st.link_button("youtube", "https://www.youtube.com/@racoonByteotterBit/")
tab1, tab2, tab3, tab4 = st.tabs(["INTRO", "PROJECT", "STUDY",])

with tab1:
   st.write("### hello otter!")
   st.video('https://youtu.be/u52CGaPWk1M?feature=shared', format='video/mp4')

with tab2:
   st.write("### working hard with communication")
   st.video('https://youtu.be/trS7V4g_8QI?feature=shared', format='video/mp4')

with tab3:
   st.write("### study knowledge")
   st.video('https://youtu.be/_TeeNkU1fpY?feature=shared', format='video/mp4')

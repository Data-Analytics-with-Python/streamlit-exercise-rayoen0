#%%writefile app.py
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Medals visualisation",layout="wide")
st.title("Medals visualisation")

#Dropdown menu
medal = st.selectbox("Select a medal type",["Gold","Silver","Bronze"])

#checkboxes
st.checkbox("Show Bar Chart", value = True)
st.checkbox("Show Pie Chart", value = True)

#two-col structure

col1, col2 = st.columns(2)

df = px.data.medals_wide()


#plot bar chart
if show_bar:
  fig_bar = px.bar(
      df,
      x = "nation",
      y=f"{medal}"
  )
  fig_bar.update_layout(
      title_x=0.5,
      xaxis_title="Country",
      yaxis_title="Count"
      width = 300, height = 300
      yaxis_title=f"{medal}"
  )
  col1.plotly_chart(fig_bar, use_container_width=True)

if show pie:
  fig_pie = px.pie(
    df,
    names= "Country",
    values=f" [medal)",
    title = f"Medals count ((medal))"
  )
  fig_pie.update_layout(
    title_x=8.5,
    height = 300)
co12. plotly_chart(fig_pie, use_container width=True)

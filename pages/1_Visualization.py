import os
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from resources.laptop_details import dataviz
import plotly.express as px



RESOURCES_PATH = os.path.join(os.getcwd(), 'resources')


plt1 = sns.displot(data=dataviz, x="MRP", kde=True,height=5,aspect=2)
plt2 = sns.catplot(data=dataviz, x="Ram Size", kind="count",height=5,aspect=2)
plt3 = sns.catplot(data=dataviz, x="Storage", kind="count",height=5,aspect=2)
plt4 = sns.catplot(data=dataviz, x="StorageType", kind="count",height=5,aspect=2)
plt5 = sns.catplot(data=dataviz, x="OS", kind="count",height=5,aspect=2)

univariatetext = """
The Above plots shows univariate plots of the data sets\n
* The first plot shows the distribution of the price which is the target variable and shows 
the need for data transformation base on the left skewness\n
* The Other plots shows the count of the various columns in the data
The Ram SIze, Storage Storage Type and the type Of operating system"""

fig1 = px.box(dataviz, x='Ram Size', y='MRP', title='Ram Size vs Price')

fig2 = px.box(dataviz, x='Storage', y='MRP', title='Storage vs Price')

fig3 = px.box(dataviz, x='StorageType', y='MRP', title='StorageType vs Price')

fig4 = px.box(dataviz, x='OS', y='MRP', title='OS vs Price')

multivariatetext = """
The above box plots shows the relationships between price and the various columns in the data\n
* The First plot show the relationship between the Ram Size and price
and shows the price seems to increase with increase in ram size
* The Second Plot shows the relationship between Storage and price
The price also seems to increase with increase in storage size
* Also the other plots shows relationship between StorageType and OS
"""
st.title('UniVariate Plots')
st.pyplot(plt1)
st.pyplot(plt2)
st.pyplot(plt3)
st.markdown(univariatetext)

st.title('MultiVariate Plots')
st.plotly_chart(fig1, theme=None, use_container_width=True)
st.plotly_chart(fig2, theme=None, use_container_width=True)
st.plotly_chart(fig3, theme=None, use_container_width=True)
st.plotly_chart(fig4, theme=None, use_container_width=True)


st.markdown(multivariatetext)
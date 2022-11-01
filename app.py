import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)


x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0,x_limit,1)

# Create a random array of data that we will use for our y values
#y_data = [random.random() for i in x_axis]

y_data = np.random.rand(100)

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)



st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)



scatter = alt.Chart(df).mark_point().encode(x='x', y='y')

st.altair_chart(scatter, use_container_width=True)


st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

scatter = alt.Chart(df,title = "Scatter Plot of X vs Y").mark_point().encode(
    
    x='x', 
    y='y', 
    size='y', 
    color='x', 
    tooltip=['x','y']).properties(width=500, height=500)

st.altair_chart(scatter.interactive(), use_container_width=False)

st.markdown("The five changes I made were.....")
st.markdown("""

The 5 changes I made were:
- Change 1 : Added size attribute as 'y'
- Change 2 : Added color attribute as 'x'
- Change 3 : Added tooltip attribute with 'x','y'
- Change 4 : Properties are adjusted with width = 500 and height = 500
- Change 5 : Use_container_width was changed to 'False'
- Change 6 : Interactive feature has been added to st.altair_chart
- Change 7 : Title has been named with title = "Scatter Plot of X vs Y"
""")



st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)
"""
source = data.stocks()

area_chart = alt.Chart(source).transform_filter(
    'datum.symbol==="GOOG"'
).mark_area(
    line={'color':'darkgreen'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='white', offset=0),
               alt.GradientStop(color='darkgreen', offset=1)],
        x1=1,
        x2=1,
        y1=1,
        y2=0
    )
).encode(
    alt.X('date:T'),
    alt.Y('price:Q')
)

st.altair_chart(area_chart, use_container_width=True)

source = data.stocks()

area_chart = alt.Chart(source,title = "Area Chart With Gradient").transform_filter(
    'datum.symbol==="GOOG"'
).mark_area(
    line={'color':'darkgreen'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='Black', offset=0),
               alt.GradientStop(color='red', offset=1)],
        x1=1,
        x2=0,
        y1=0,
        y2=1
    )
).encode(
    alt.X('date:T'),
    alt.Y('price:Q')
)

st.altair_chart(area_chart, use_container_width=True)
"""

#source = data.movies.url
#source = pd.read_json('Assignment/imdb.json')
source = pd.read_json('imdb.json')
st.write(source)

hist = alt.Chart(source).mark_bar().encode(
    alt.X("IMDB_Rating:Q", bin=True),
    y='count()',
)

st.altair_chart(hist, use_container_width=True)

st.markdown("""
The 2 changes I made were:
- Change 1 : Color palette has been changed to Black and Red.
- Change 2 : The area chart has been scaled along Y-axis(i.e. price)
- Change 3 : Title has been given with title = "Area Chart With Gradient"
"""
)


import streamlit

# Creating Title for App
streamlit.title('My Parents New Healthy Diner')

# Added in new section for Breakfast Menu and Items
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

# Added in new section to build your own fruit smoothie
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Importing pyhton libray pandas, importing csv data, displaying it on app
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Index displays fruit not number. 
my_fruit_list = my_fruit_list.set_index('Fruit')

# New displaying data and using a widget and put the list of selected fruits into a variable called fruits_selected. 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_lsit.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Index displays fruit not number. 
my_fruit_list = my_fruit_list.set_index('Fruit')

# New displaying data and using a widget 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


#Create a function 
def get_fruityvice_data(this_fruit_choice): 
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

# New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_fuction = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_fuction)

except URLError as e:
  streamlit.error()


#streamlit.stop()

streamlit.header("View Our Fruit List - Add Your Favourites!")
# Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from fruit_load_list")
       return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get Fruit List'):
       my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
       my_data_rows = get_fruit_load_list()
       my_cnx.close()
       streamlit.dataframe(my_data_rows)
  
# Allow the end usere to add a fruit to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('"+add_my_fruit +"')")
    return "Thanks for adding " + new_fruit
    
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button ('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)





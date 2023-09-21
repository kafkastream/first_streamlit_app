import streamlit
import pandas

streamlit.title("Preparando el examen Snowflake")
streamlit.title("1.- Arquitectura de Snowflake")
streamlit.title("2.- Usuarios, roles y permisos")
streamlit.title("3.- Carga de datos / Snowpipe")
streamlit.title("4.- Datos semi-estructurados")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

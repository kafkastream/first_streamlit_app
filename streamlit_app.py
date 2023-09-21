import streamlit
import pandas

streamlit.title("Preparando el examen Snowflake")
streamlit.title("1.- Arquitectura de Snowflake")
streamlit.title("2.- Usuarios, roles y permisos")
streamlit.title("3.- Carga de datos / Snowpipe")
streamlit.title("4.- Datos semi-estructurados")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

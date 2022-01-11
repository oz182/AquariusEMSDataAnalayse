import streamlit as st
import pandas as pd




def FirstLayout():
    global FileNameIN

    st.set_page_config(layout="wide")
    st.write("""## **CSV analysis From - AMS** """)

    my_expander = st.sidebar.expander(label='Files selection')
    with my_expander:
        FileNameIN = st.file_uploader('Choose a .csv file: ')



def main():
    FirstLayout()
    print('nothing yet')


if __name__ == "__main__":
    main()
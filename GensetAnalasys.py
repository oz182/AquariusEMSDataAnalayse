import streamlit as st
import pandas as pd


def DownSampleRate():
    print('Nothing')


def StreamLitGUI():
    left_column, right_column = st.columns(2)

    X = left_column.selectbox('', HaedersList)
    left_column.line_chart(data=df[X])

    Y = right_column.selectbox(' ', HaedersList)
    right_column.line_chart(data=df[Y])

    st.write("""# **The selected graphes combined** """)

    stdf = pd.DataFrame(data, columns=[X, Y])
    st.line_chart(stdf)



def CSVfileAnalyser(fp):
    global HaedersList, df, data

    data = pd.read_csv(fp)
    df = pd.DataFrame(data)
    HaedersList = list(df.columns.values)

    st.write(df)


def FirstLayout():
    global FileNameIN

    st.set_page_config(layout="wide")
    st.write("""## **CSV analysis From - AMS** """)

    my_expander = st.sidebar.expander(label='Files selection')
    with my_expander:
        FileNameIN = st.file_uploader('Choose a .csv file: ')


def main():
    FirstLayout()
    CSVfileAnalyser(FileNameIN)
    StreamLitGUI()




if __name__ == "__main__":
    main()


"""
    if X != Y:
        c = alt.Chart(stdf).mark_circle(size=60).encode(x=X, y=Y).interactive()
        st.altair_chart(c, use_container_width=True)
"""

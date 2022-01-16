import streamlit as st
import pandas as pd
import altair as alt
#import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report

def DownSampleRate():
    print('Nothing')


def StreamLitGUI():
    if FileName2 == None:
        left_column, right_column = st.columns(2)

        X = left_column.selectbox('', HaedersList)
        left_column.line_chart(data=df[X])

        Y = right_column.selectbox(' ', HaedersList)
        right_column.line_chart(data=df[Y])

        if X != Y:
            st.write("""# **The selected graphes combined** """)

            stdf = pd.DataFrame(data, columns=[X, Y])
            st.line_chart(stdf)

            c = alt.Chart(stdf).mark_circle(size=60).encode(x=X, y=Y).interactive()
            st.altair_chart(c, use_container_width=True)

            #just for now... this how to do a graph about the time axis but it is not dynamic
            #tempdf = pd.DataFrame(data, columns=['Time', X])
            #lineA = alt.Chart(tempdf).mark_line().encode(x='Time', y=X).interactive()
            #st.altair_chart(lineA)

        #pr = df.profile_report()
        #st_profile_report(pr)

    else:
        left_column, right_column = st.columns(2)

        left_column.write('File 1:')
        X = left_column.selectbox('', HaedersList)
        left_column.line_chart(data=df[X])

        right_column.write('File 2:')
        Y = right_column.selectbox(' ', HaedersList2)
        right_column.line_chart(data=df2[Y])



def CSVfileAnalyser(fp, fp2):
    global HaedersList, df, data
    global HaedersList2, df2, data2

    data = pd.read_csv(fp)
    df = pd.DataFrame(data)
    HaedersList = sorted(list(df.columns.values))

    if fp2 != None:
        data2 = pd.read_csv(fp2)
        df2 = pd.DataFrame(data2)
        HaedersList2 = sorted(list(df2.columns.values))


def FirstLayout():
    global FileNameIN, FileName2

    st.set_page_config(layout="wide")
    st.write("""## **CSV analysis From - AMS** """)

    my_expander = st.sidebar.expander(label='File selection')
    with my_expander:
        FileNameIN = st.file_uploader('Choose a .csv file: ')

    my_expander2 = st.sidebar.expander(label='Seccond File to compre:')
    with my_expander2:
        FileName2 = st.file_uploader('Choose a .csv file: ',key='key')


def main():
    FirstLayout()
    if FileNameIN != None:
        CSVfileAnalyser(FileNameIN, FileName2)
        StreamLitGUI()




if __name__ == "__main__":
    main()





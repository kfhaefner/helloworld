import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.markdown('Test')
st.markdown('''
            # Test
            ## Test Test
            ### Test test Test
            ''')

st.header('Title / Header')
st.subheader('Subheader / Subtitle')
st.caption('This is a caption.')

st.text('Hi.')
st.code('''
        import numpy as np
        dat = np.zeroes(4,4)
        print(dat)
        ''')

st.latex('''
          f(x) = a_3x^3 + a_2x^2 + a_1x + a_0 \\\\
         ''')
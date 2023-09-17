import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)

# import streamlit as st
# import pandas as pd

# # Create an empty DataFrame
# data = pd.DataFrame(columns=['Name', 'Age', 'Email'])

# # Add a button to add new rows to the table
# if st.button('Add Row'):
#     data.loc[len(data)] = ['New Name', 0, '']

# # Display the DataFrame as a table
# table = st.dataframe(data)

# # Allow users to edit the table
# for i in range(len(data)):
#     name = table.text_input(label='Name', value=data.loc[i, 'Name'], key=f'Name_{i}')
#     age = table.number_input(label='Age', value=data.loc[i, 'Age'], key=f'Age_{i}')
#     email = table.text_input(label='Email', value=data.loc[i, 'Email'], key=f'Email_{i}')
    
#     # Update the DataFrame with the edited values
#     data.loc[i] = [name, age, email]

# # Display the updated DataFrame
# st.write(data)
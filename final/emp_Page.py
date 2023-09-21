import streamlit as st
from final_gui import *
from my_queries import *
import pandas as pd

def add_skill():
    # Create a button and input field in Streamlit
    if st.button('Add Skills'):
        # Prompt the user to enter skills
        new_skill = st.text_input('Enter a skill:')
        
        # Check if the input is not empty
        if new_skill:
            # # Add the skill to the list
            # skills.append(new_skill)
            
            # Clear the input field
            st.text_input('Enter a skill:', value='')
            return new_skill
    

def present_SKILLS(userId):
    skills = group_by(userId)
    columns = st.columns(len(skills))
    # loop over skills and get tuple and number of element
    for i, data in enumerate(skills):
        # Extract the category and skills from the tuple
        category, skills = data
        # Split the skills into a list
        skill_list = skills.split(',')
        # Create a dataframe from the skill list
        df = pd.DataFrame(skill_list, columns=["Category"])
        with columns[i]:
            st.subheader(category)
            st.write(df)
            # Add skill button and input field
            new_skill = st.text_input(f'Enter a {category} skill:')
            if (st.button(f'Add {category} Skill') and new_skill ):
                # print("Pressed")
                # print(new_skill)

                skill_data=(new_skill, category, userId)
                insert_skill(skill_data)
                # print("Inserted")
                st.experimental_rerun()
            


# Define the employee page
def employee_page(userId):

    st.set_page_config(
        page_title="Skiils Matrix",
        page_icon="📈",
        layout="wide"
    )
    # display the user name in the page
    (Name,Department,Position) =  get_emp(userId)
    # presnet name department position in different columns
    # make title and header in middle of screen
    st.markdown("<h1 style='text-align: center; color:#083D77;'>"+"Skills Page"+"</ h1>", unsafe_allow_html=True)

    # st.title("Skills Page")
    # st.markdown("<h1 style='text-align: center; color:#083D77;'>"+str(Name)+"</ h1>", unsafe_allow_html=True)

    st.header(f'Welcome {Name}')

    # insert line
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Department : {Department}")
    with col2:
        st.write(f"Position : {Position}")

    # insert line
    st.markdown("---")

    # write Ahmed Skills in the middle of screen
    st.markdown("<h3 style='text-align: center; color:#083D77;'>"+str(Name)+" Skills"+"</ h3>", unsafe_allow_html=True)
    
    present_SKILLS(userId)

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        new_category = st.text_input('Enter a Category:')
    with col2:
        new_skill = st.text_input('Enter a skill:')

    new_category_bt = st.button('Enter a new category')
    if new_category_bt:
        print("Pressed")
        print(new_category)
        print(new_skill)
        skill_data=(new_skill, new_category, userId)
        insert_skill(skill_data)
        print("Inserted")
        st.experimental_rerun()
    # st.button('Logout', on_click=logout)
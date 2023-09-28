# Skills Matrix WebApp
Database and Website Gui for Company Users Skills Visualization and editing in user friendly way.
***
## Table of contents
* [Introduction](#introduction)
* [Project Structure](#project-structure)
* [Developer Guide](#developer_guide)
* [User Guide](#user_guide)
* [Technologies](#technologies)


## Introduction
- This project is a web application that allows users to view and edit the skills of the company's employees in a user-friendly way.
- The application is based on a database that contains all the information about the employees and their skills.
- Each user can view his skills and edit on them
- Only the **Admin** has The **Privilege** to view and edit all the employees data


## Project Structure

- The project is divided into two parts:
    - **Backend & Database** - The backend is responsible for the database and the server.
    - **Frontend** - The frontend is responsible for the website and the user interface.

### Database
- The database is based on **MySQL**.

- The database contains 2 tables:
    - **Employees** - Contains all the users in the company.
    - **Skills** - Contains the Skills for each user in the company.

#### ER Diagram

![ER Diagram](Images\ER_Diagram.png)

#### Employees Table

![Employee table](Images\Employee_table.png)

#### Skills Table

![Skills Table](Images\Skills_Table.png)

### Frontend
- The frontend is based on **Python Streamlit**.

- The frontend contains 3 pages:
    - **Login Page** - The login page is the first page that the user sees when he enters the website. The user must enter his username and password in order to enter the website.
 ![Login Page](Images\GUI\Login_Page.png)

    - **Skills Page** - The skills page is the main page of the website. The user can view his skills and edit them.
![User Page](Images\GUI\User_Page.png)

    - **Admin Page** - The admin page is a page that only the admin can enter. The admin can view and edit all the employees data.
![Admin Page](Images\GUI\Admin_Page.png)

```
Skills Matrix WebApp
├─  src
│  ├─ mainPage.py
│  ├─ pages_handler.py
│  ├─ utils.py
│  ├─  database
│     ├─  database_connection.py
│     ├─  database_init.py
│     ├─  fill_tables.py
│     └─  database_queries.py
README.md
```

## Developer Guide

### Prerequisites
- **Python 3.8** or higher
- **MySQL** server
- **MySQL Workbench** or **PhpMyadmin**
- **Streamlit** library
- **PyMySQL** library
- **Pandas** library

### DataBase Creation :
- Using phpmyadmin as described in the Database Developer Guide File 
- Or with using MySql Connector Librarry by running these to files : 
    - **database_init.py** - Create the database and the tables
    - **fill_tables.py** - Insert the data to the database tables

### Run the WebApp
```shell
 cd .\src\
 pip install streamlit
 streamlit run mainPage.py
```

## User Guide
- The user must enter his username and password in order to enter the website.
![Login Page](Images\GUI\Login_Page.png)

- The user can view his skills and edit them by adding new Skill in selected category or by adding new Category of Skills.
  ![User Page](Images\GUI\User_Page.png)

- The admin can view and edit all the employees data.
    - He Can view and Edit His Own Page
![Admin Page](Images\GUI\Admin_Page.png)
    - By Selecting All User From The Dashboard he can :
        - Display All users Data
          ![Screenshot (686)](Images\GUI\All_Users.png)

        - Add New User
          ![Screenshot (687)](Images\GUI\Add_USer.png)

        - Edit Specific User Data
          ![Screenshot (689)](Images\GUI\Edit_User.png)

    - By Selecting User Skills From The Dashboard he can Display any Selected user ID Skills Matrix and Edit on it  :
    ![Screenshot (690)](Images\GUI\All_Skills.png)


## Technologies
- Python 3.8
- MySQL
- MySQL Workbench
- PhpMyadmin
- Streamlit
- PyMySQL
- Pandas

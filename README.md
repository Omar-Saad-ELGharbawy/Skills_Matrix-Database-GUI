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

![ER Diagram](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/assets/84602951/7320f725-4599-42f4-9166-c63f5d0031d1)

#### Employees Table

![Employee table](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/assets/84602951/00cf1fcb-dc8e-4466-9edd-96ea725cbcfd)

#### Skills Table

![Skills Table](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/assets/84602951/01b9fa8c-1f87-4bbc-95ad-7e2d9314e975)

### Frontend
- The frontend is based on **Python Streamlit**.

- The frontend contains 3 pages:
    - **Login Page** - The login page is the first page that the user sees when he enters the website. The user must enter his username and password in order to enter the website.
 ![Login Page](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/assets/84602951/86b24d06-5d7f-42e4-849a-a64f076c29bd)

    - **Skills Page** - The skills page is the main page of the website. The user can view his skills and edit them.
![User Page](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/assets/84602951/6b3810ba-9ecb-4d90-96e3-deaa1ff8de01)

    - **Admin Page** - The admin page is a page that only the admin can enter. The admin can view and edit all the employees data.
![Admin Page](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/assets/84602951/ab37886e-30d7-44fd-9094-a9e04f36825b)

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
- Using phpmyadmin as described in the [Database_Developer_Guide_File](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/blob/main/Files/Database%20Developer%20Guide.pdf) 
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
![Login Page](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/assets/84602951/861eabe5-5933-4083-852f-07c4c6cbf73d)

- The user can view his skills and edit them by adding new Skill in selected category or by adding new Category of Skills.
  ![User Page](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/assets/84602951/50ffc378-7797-4f2c-9784-2476780c5b4b)

- The admin can view and edit all the employees data.
    - He Can view and Edit His Own Page
![Admin Page](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/assets/84602951/5a7640c4-10eb-442a-9d59-0043efa71f1a)
    - By Selecting All User From The Dashboard he can :
        - Display All users Data
          ![Screenshot (686)](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/assets/84602951/27e95e49-85ed-44e1-a082-1ff9db795f90)

        - Add New User
          ![Screenshot (687)](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/assets/84602951/a088fcc7-5f7a-4aae-bf4a-2a5f866c3f69)

        - Edit Specific User Data
          ![Screenshot (689)](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/assets/84602951/f7eaa819-0783-4437-b50e-6af8074d2d17)

    - By Selecting User Skills From The Dashboard he can Display any Selected user ID Skills Matrix and Edit on it  :
    ![Screenshot (690)](https://github.com/Omar-Saad-ELGharbawy/Skills_Matrix/assets/84602951/95f67417-4c9d-43b0-8ca0-d6add3d974c4)


## Technologies
- Python 3.8
- MySQL
- MySQL Workbench
- PhpMyadmin
- Streamlit
- PyMySQL
- Pandas

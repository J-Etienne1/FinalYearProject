=======================================
                
                INSTALLATION

=======================================



Assumption: 
This application was developed, run and tested on with the use of Microsoft Visual Studio Code, 
the assumption is that this is the environment it will be run on

Project Set up Guide:
- Unzip the project folder
- Open Visual Studio Code
- Open the project folder in Visual Studio Code
- In Visual Studio Code open a terminal
- Select Command Prompt as your interface
- Install a virtual environment if not already installed
- If not installed enter following command in the terminal: pip install virtualenv
- Create a virtual environment with the following command: virtualenv env
- Once the virtual environment has been created it need to be activated
- To activate the virtual env, navigate to the newly created virtual env folder
- Then navigate to a subfolder Scripts
- Then to activate the virtual environment enter the command: activate
- Once activated, indicated by the virtual env name to the left of the directory path
- Navigate back to the main project folder
- Now navigate to the folder called main
- Next the systems requirements need to install
- In the terminal enter the following command: pip install -r requirements.txt
- After the requirements have been installed run the following command to activate the systems:  python manage.py runserver
- The application can then accessed with the following link: http://127.0.0.1:8000/





=======================================
                
                Accounts
=======================================

The system has a Admin User created with the following credentials 

Username:           Password: 
admin               123456


There are also two standard accounts for testing and highlighting that users data is not viable by other users
The standard user credentials are as follows

Username:           Password: 
User1               Password!.0
User2               Password!.0





=======================================
        
        Registration Test Cards
=======================================

Successful payment:

Card Number - 4242 4242 4242 4242

CVC - Any 3 Digits

Date - Any Future Date


Declined payment:

Card Number - 4000 0000 0000 0002

CVC - Any 3 Digits

Date - Any Future Date

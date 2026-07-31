# SMART EXPENCE TRACKER API ##

This project is a REST API built using python and Flask to track personal expenses. The API allows you to:

-> Add an expense
-> View all the expenses
-> View expenses by category
-> Get statistics about the expenses(e.g. total amount of money spend, total spent by category)
-> Delete an expense
A simple web interface is also provided to make it easier to interact with the API.

# PROJECT SRUCTURE #

smart-expence-tracker/
---README.md
---AI_NOTES.md
---requirements.txt
---data.json
---src/
---tests/


# REQUIREMENTS #

-> Flask==3.1.1
-> pytest


# INSTALL REQUIREMENTS #

pip install -r requirements.txt

# RUN THE SERVER #

python src/app.py

The app will be running at: " http://127.0.0.1:5000/ "


# RUN TESTS #

pytest

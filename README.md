# cap1
##Competency Tracking Tool Overview

The tool will be a console application and will support the following features:

Login and logout. The tool should keep track of user emails and passwords to allow for secure login. The passwords should be hashed so that they are not stored in the database in plain-text.
Two User Types and their access to features.
A user is an individual that can only view their own competency and assessment data. They should have the ability to edit their own user data such as changing their name and editing their own password.
A manager is an individual that can manage users. They should be able to:
view all users in a list
search for users by first name or last name
view a report of all users and their competency levels for a given competency
view a competency level report for an individual user
view a list of assessments for a given user
Add
add a user
add a new competency
add a new assessment to a competency
add an assessment result for a user for an assessment (this is like recording test results for a user)
Edit
edit a user's information
edit a competency
edit an assessment
edit an assessment result
Delete
delete an assessment result
Export reports to CSV
Competency report by competency and users
Competency report for a single user
Import assessment results from CSV
The ability to import assessment results from a CSV file
The CSV file would contain columns user_id, assessment_id, score, date_taken
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
***first import the following modules to run***
from cgitb import text

import sqlite3

import pandas as pd



import bcrypt

import csv

import datetime

import sys


//then you will be brought to a display menu that looks like this
Menu
1). Add User
2). Edit User
3). Add Competency
4). Edit Competency
5). Add Assessment
6). Edit Assessment
7). Add Assessment Result
8). Edit Assessment Result
9). Export to CSV
e). Exit

How can I help you today?


***First you have to add a user, then add an assessment, then add an assessment_result. Once those are in there should be data in the sqlite db that you can export.***

# CS50.FinalProject
TagYourFriends is a quick way to reconnect with friends and have a little fun in the process

Add a personalized message to your tag! Use it to talk trash, show praise, or tell a joke!

See how long it takes someone to notice that they're "it"!

# File Descriptions

## Users

File | Description
--- | ---
/users/templates/users/login.html | Login screen
/templates/users/logout.html | Logout confirmation screen
/templates/users/register.html | User Registration screen
/users/forms.py | Form definition for User Registration screen
/users/sviews.py | User Registration logic

File | Description
--- | ---
/.gitignore | Defines files that should not be tracked by git (contains all \_\_pycache\_\_ folders)
/requirements.txt | All required components with component versions.

## FinalProject

File | Description
--- | ---
/finalproject/settings.py | Contains application settings, including timestamp information

## tag

File | Description
--- | ---
/tag/migrations/\_\_init\_\_.py | System-generated initial file
/tag/migrations/0001_initial.py | Model creation script (Django generated)
/tag/static/jquery.bootstrap.modal.forms.js | Bootstrap jquery module
/tag/templates/tag/index.html | Home page, list of recent tags
/tag/templates/tag/layouts.html | Base HTML layout for the applicaiton, contains nav bar code and commonly-used javascript
/tag/templates/tag/user.html | User stats page
/tag/admin.py | Registers custom models with the Django Admin application
/ordrs/forms.py | Contains form logic used in index.html for ordering
/tag/models.py | Contains data model definitions
/tag/urls.py | Registers all URLs used in the application (including internal URLs for updating application elements)
/tag/views.py | Main application logic, contains python code to tag users (including validations) as well as for gathering User statistics.
# Instagram
This is a clone of the popular istagram website. 12th March 2019
### By Lorna wanjiku

## Description
is a clone of the popular istagram website.

## Setup/Installation Requirements
To start using this project use the following commands:

* git clone https://github.com/wanjikuciku/lony-gram.git
* cd instagram
* atom .
* code . (this is if Visual Studio Code is your preferred text editor)

* The repo comes in a zipped or compressed format. Extract to your prefered location and open it.

* open your terminal and navigate to instagram then create a virtual environment.For detailed guide refer here

* To run the app, you'll have to run the following commands in your terminal

pip install -r requirements.txt

* On your terminal,Create database instagram using the command below.

CREATE DATABASE instagram;

* Migrate the database using the command below

python3.6 manage.py migrate

* Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

python manage.py runserver

* Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

* access the application on this localhost address http://127.0.0.1:8000

## Behaviour Driven Development
|  Behaviour |  Input  |  Output |
|------------|---------|---------|
| The program should display the explore page on load of the application | On page load | Explore page with all latest photos from all users |
| The program should navigate to sign up page when Sign Up is clicked  | Click on Sign Up on the registration form | Redirected to the sign up page |
|The program should navigate to the login page when Login is clicked | Click on Login on the registration form |Redirected to the login page |
|The program should direct the user to their timeline page when logged in | Login as a user | Redirected to the timeline page with photos of users you follow |
|The program should add a like or remove a like when the heart icon is clicked on | Click on the heart icon | Click on the heart icon | A like is added if it wasn't added before else it is removed |
|The program should have a comment section on an image | Write on the comment section | The comment will appear on the image| 

## Prerequisites
You need the following to work on the project: -Python version 3.6 -Django -Pip -virtualenv -A text Editor

## Link to Live Website https://lona-instagram.herokuapp.com/

## Known Bugs
None at the moment, but if found please contact.

## Technologies Used
* Python
* HTML
* Django micro-framework
* W3 schools
* Bootstrap(used for styling)

## License
MIT License

Copyright (c) 2019 LORNA WANJIKU

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

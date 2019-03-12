# Imstagram
This is a clone of the popular istagram website. 12th March 2019
### By Lorna wanjiku

## Description
is a clone of the popular istagram website.

## Specifications
Users can view pictures.
Users can search for category pictures.
Users can select a location of their interest to view pictures.

## Setup/Installation Requirements
To start using this project use the following commands:

* git clone https://github.com/wanjikuciku/piktures.git
* cd piktures
* atom .
* code . (this is if Visual Studio Code is your preferred text editor)

* The repo comes in a zipped or compressed format. Extract to your prefered location and open it.

* open your terminal and navigate to piktures then create a virtual environment.For detailed guide refer here

* To run the app, you'll have to run the following commands in your terminal

pip install -r requirements.txt

* On your terminal,Create database piktures2 using the command below.

CREATE DATABASE piktures2;

* Migrate the database using the command below

python3.6 manage.py migrate

* Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

python manage.py runserver

* Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

* access the application on this localhost address http://127.0.0.1:8000

## Behaviour Driven Development
|  Behaviour |  Input  |  Output |
|------------|---------|---------|
| Home | - | - |
|Click on location | enter a location | pictures |
|Search icon | Search on a category |images are displayed |

## Prerequisites
You need the following to work on the project: -Python version 3.6 -Django -Pip -virtualenv -A text Editor

## Link to Live Website https://lornapiktures.herokuapp.com/

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

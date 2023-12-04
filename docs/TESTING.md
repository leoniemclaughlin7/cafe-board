# Testing 

Café-Board was tested using both automated and manual testing methodology.

## Automated testing

### Python testing

The Python in this project was tested using python testing. Coverage was determined by installing Django-nose. Coverage by automated python tests in this project was 70%. This percentage could be higher however manual testing will cover the 30% that is missed by automated testing.

<img  src="../docs/testing_images/python-testing.png">

<img  src="../docs/testing_images/tests-run-python.png">

## Manual testing

Testing of the functionality of the website can be seen in the following tables. Each section of the website has been tested according to the feature and testing different devices and screen resolutions has been conducted using Google DevTools.

### Navigation Bar 

|Feature  | Expect  | Action | Result | 
|--|--|--|--|
| Logo  | When the logo is clicked it will return the user to the home page |Clicked logo | pass
| Home nav link| When clicked it will direct the user to the home page |Clicked Home on the nav bar | pass
|Menu nav link| When clicked it will direct the user to the menu |Clicked Menu on the nav bar | pass
|Register nav link| When clicked it will direct the user to the sign up page |Clicked Register on the nav bar | pass
| Sign in nav link| When clicked it will direct the user to the sign in page |Clicked Sign in on the nav bar | pass
|Nav menu responsive |When browser is resized the nav bar will remain responsive across all device sizes |Resized browser across different device sizes| pass

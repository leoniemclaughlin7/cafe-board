# Testing

Café-Board was tested using both automated and manual testing methodology.

## Automated testing

### Python testing

The Python in this project was tested using python testing. Coverage was determined by installing Django-nose. Coverage by automated python tests in this project was 70%. This percentage could be higher however manual testing will cover the 30% that is missed by automated testing.

<img  src="../docs/testing_images/python-testing.png">

<img  src="../docs/testing_images/tests-run-python.png">

## Manual testing

Testing of the functionality of the website can be seen in the following tables. Each section of the website has been tested according to the feature on the deployed site. Testing different devices and screen resolutions has been conducted using Google DevTools.

### Navigation Bar

|Feature  | Expect  | Action | Result |
|--|--|--|--|
| Logo  | When the logo is clicked it will return the user to the home page |Clicked logo | pass
| Home nav link| When clicked it will direct the user to the home page |Clicked Home on the nav bar | pass
|Menu nav link| When clicked it will direct the user to the menu |Clicked Menu on the nav bar | pass
|Register nav link| When clicked it will direct the user to the sign up page |Clicked Register on the nav bar | pass
| Sign in nav link| When clicked it will direct the user to the sign in page |Clicked Sign in on the nav bar | pass
|Nav menu responsive |When browser is resized the nav bar will remain responsive across all device sizes |Resized browser across different device sizes| pass

### Hero Image

|Feature | Expect | Action | Result |
|--|--|--|--|
|Hero image responsive |When the screen size is changed the image does not distort and fits to screen |Resized browser and checked hero image at different screen resolutions | pass
|Text overlay responsive |At different device resolutions the text overlay remains in position| Resized browser and checked the text overlay at different screen resolutions |pass

### About Section

|Feature | Expect | Action | Result |
|--|--|--|--|
|About cards responsive |When the screen size is changed the about cards will adapt to the different screen size |Resized browser and checked about cards at different screen resolutions | pass
|Menu icon clickable| When clicked the menu icon will open the menu page| Clicked the menu icon |pass
|Games icon clickable| When clicked the games icon will open the games page| Clicked the games icon |pass

### Address and reviews section

|Feature | Expect | Action | Result |
|--|--|--|--|
|Address and reviews section logged out |When user is logged out, address, logo and reviews should be shown to the user |Observed address and review section when user is logged out | pass
|Address and reviews section logged in |When user is logged in, address, review form and reviews should be shown to the user |Observed address and review section when user is logged in | pass
|Address I frame | The I frame allows you to zoom in and out of the map, move the map around by clicking and dragging the mouse and will open Google maps in a new tab when 'View larger map' is clicked |Zoomed in and out of I frame, clicked and dragged mouse over I frame and clicked 'View larger map' |pass
|Reviews scrollable| When the review container is full the user shall be able to scroll through reviews |Scrolled through reviews | pass
|Leave a review| When the user is logged in they can fill out a form to leave a review by pressing the submit button |Filled out review form and pressed submit button | pass
|Leave a review - form validation | If the user tries to submit the review form with either of the Two field left blank, a pop up message will detail that these fields are required |Press submit button with field left blank | pass
|Leave a review - success message |When user submits a review a success message will appear at the top of the page |Observed if a success message is displayed to the user upon submitting a review | pass
|Address and review section responsive |When the screen size is changed the address and review section will adapt to the different screen size |Resized browser and checked the address and review section at different screen resolutions | pass

### Games

|Feature | Expect | Action | Result |
|--|--|--|--|
|Games page responsive |When the screen size is changed the list of games will adapt to the different screen size |Resized browser and checked the games page at different screen resolutions | pass

### Menu

|Feature | Expect | Action | Result |
|--|--|--|--|
|Menu will expand when clicked |When the title of each menu section is clicked it will expand to show the full menu for each section |Clicked the title of each section of the menu | pass
|Menu page responsive |When the screen size is changed the menu page will adapt to the different screen size |Resized browser and checked the menu page at different screen resolutions | pass

### Register

|Feature | Expect | Action | Result |
|--|--|--|--|
|Sign in link |If the user clicks the sign in link they are redirected to the sign in page |Clicked sign in link | pass
|Register form |Once the register form is filled out correctly and sign up button is clicked it will create an account for the user and sign them into the site |Filled out all required fields of register form and clicked sign up | pass
|Register - success message |When user creates an account they are signed in to café-board and a success message is displayed |Created an account on the register page and observed the success message| pass
|Register form validation |If sign up is clicked without a required input field being filled a pop up will detail this to the user |Clicked sign up and left username blank| pass
|Register - password matching |If the user tries to use Two different passwords to create an account, a message will detail 'You must type the same password each time' |Try to create and account with Two different passwords | pass
|Register - username |If the user tries to create an account with an already in use username a message will appear 'A user with that username already exists' |Try to create and account with a username that already exists | pass
|Register page responsive |When the screen size is changed the register page will adapt to the different screen size |Resized browser and checked the register page at different screen resolutions | pass

### Sign in

|Feature | Expect | Action | Result |
|--|--|--|--|
|Sign up link |If the user clicks the sign up link they are redirected to the register page |Clicked sign up link | pass
|Sign in form |Once the sign in form is filled out correctly and sign in button is clicked it will sign them into the site |Filled out all required fields of sign in form and clicked sign in | pass
|Sign in - success message |When user signs in they are redirected to café-board home page and a success message is displayed |Signed in and observed the success message| pass
|Sign in form validation |If sign in is clicked without a required input field being filled a pop up will detail this to the user |Clicked sign in and left username blank| pass
|Sign in form incorrect details |If sign in is clicked with incorrect details entered a message detailing 'The username and/or password you specified are not correct' will appear |Clicked sign in with a not registered username| pass
|Sign in page responsive |When the screen size is changed the sign in page will adapt to the different screen size |Resized browser and checked the sign in page at different screen resolutions | pass

### Booking

|Feature | Expect | Action | Result |
|--|--|--|--|
|Booking form |Once the booking form is filled out correctly and submit button is clicked it will direct the user to their profile page| Filled in booking form and clicked submit |pass
|Booking form validation| If any of the required fields are left empty a pop up will detail that these fields are required for submission of the form |Submitted booking form with first name left blank |pass
|Booking - success message |Once the booking form is submitted successfully a success message will be displayed to the user |Submitted booking form an observed success message |pass
|Unavailable dates |Once a date is fully booked it will become unavailable for the user to choose |Entered 20 bookings on each time slot for the 30th of December |pass
|Booking date widget |The user wont be able to pick any date which is fully booked, this date will be disabled and in red |Tried to pick the 30th of December |pass
|Booking time widget |The user will only be able to pick a time when the café is open between 10am and 11pm |Observed the options in the time picker |pass
|Limit number of attendees |Only 20 spaces is available on any given time slot at the café, once a booking is confirmed it will limit the number of attendees for that time slot, as 2 people are confirmed on the 12th of December at 11 am, trying to book anymore than 18 will result in an error message |Tried to book 19 people in on the 12th of December at 11 am and observed error message |pass
|Profile icon |Clicking the profile icon will direct user to profile page |Clicked profile icon on booking page |pass
|Booking page responsive |When the screen size is changed the booking page will adapt to the different screen size |Resized browser and checked the booking page at different screen resolutions | pass

### Profile

|Feature | Expect | Action | Result |
|--|--|--|--|
|Welcome section |The users username will be displayed in a welcome message |Observed welcome section for different users |pass
|Profile information - edit |The user can edit their username or email by clicking the edit button and they will be directed to an edit page |Clicked edit button |pass
|Edit profile information |The user can edit their username or email by filling out the form on the edit user page and clicking update user |Edited username and clicked update user |pass
|Accessing a user account that is not users| If a user tries to edit a user account which is not theirs they will be redirected to the profile page with an error message or directed to the 404 page |Changed the id of a user account in the address bar |pass
|Delete profile| When the delete account button is clicked a modal will pop up to the user to confirm this action, once delete account is clicked the user will be redirected to the logged out home page with a warning message  |Clicked delete account and clicked delete account again on the modal, tried to sign in using the deleted account details |pass
|Booking display |If there are no bookings present the user is greeted with a message otherwise their booking is displayed |Checked different users profiles and observed the message or bookings |pass
|Edit bookings |By clicking edit next to a booking the user can edit details of their booking and confirm these edits by clicking update booking |Clicked edit and then edited the details of first name then clicked update booking |pass
|Delete bookings |Once the user clicks delete next to a booking the booking will be removed and a warning message is displayed to the user |Clicked delete on a booking |pass
|Booking container scrollable |If there is a large number of bookings for a profile the booking container will be scrollable |Observed a profile with large number of bookings |pass
|Accessing a booking that is not users| If a user tries to edit a booking which is not theirs they will be redirected to the profile page with an error message or directed to the 404 page |Changed the id of a booking in the address bar |pass
|Profile page responsive |When the screen size is changed the profile page will adapt to the different screen size |Resized browser and checked the profile page at different screen resolutions | pass

### Logout

|Feature | Expect | Action | Result |
|--|--|--|--|
|Logout |Users can logout of the site by clicking the sign out button, they will be redirected to the logged out home page |Clicked the sign out button |pass|
|Logout - warning message |Once logged out a message will detail this to the user |Logged out of the site and observed the message |pass
|Logout page responsive |When the screen size is changed the logout page will adapt to the different screen size |Resized browser and checked the logout page at different screen resolutions | pass

### Footer

|Feature | Expect | Action | Result |
|--|--|--|--|
|Facebook link clickable | When clicked the Facebook icon will open a new window to Facebook | Clicked the Facebook icon| pass
|Instagram link clickable | When clicked the Instagram icon will open a new window to Instagram | Clicked the Instagram icon| pass
|Contact us | When clicked the contact us link will open the contact form | Clicked the contact us link| pass
|Footer responsive | Footer will fit the screen size, down to 320px width| Resized the browser and checked the footer at different resolutions | pass

### Contact us

|Feature | Expect | Action | Result |
|--|--|--|--|
|Contact us form |Once successfully filled out and the submit button is clicked the from will send an email to admin of café-board |Filled out form and clicked submit |pass
|Contact us form validation |If the form is submitted with a required field empty a pop up will detail this to the user |Tried to submit form with empty name input |pass
|Email validation| Correct email format must be supplied in the email input, if not a pop up will inform user of this| Submitted contact us form with incorrect email format |pass
|Contact us page responsive |When the screen size is changed the contact us page will adapt to the different screen size |Resized browser and checked the contact us page at different screen resolutions | pass

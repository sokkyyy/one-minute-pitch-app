## Built By [Ray Ndegwa](https://github.com/sokkyyy/)

## Description
One Minute Pitch App is a web application that allows users to post short(preferrably, 1 minute) pitches. Users can register/login, create pitches, upvote and downvote the pitches, view their profiles and profiles of other users, comment on the pitches and view pitches in different categories.



## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I can:
* See the pitches other people have posted.
* Vote on a pitch by downvoting or upvoting.
* Login to leave a comment.
* Receive a welcoming email once I sign up.
* View the pitches I have created in my profile page.
* Comment on the different pitches and leave feedback.
* Submit a pitch in any category.
* View the different categories of pitches.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display pitches starting with the latest | **On page load** | List of various pitches |
| Display pitches from a certain category | **Click 'Pitch Category' Link on navbar** | Redirected to a page with a list of pitches from a category |
| Display the profile of a user | **Click username link or navbar Profile Pic** | Display user information and pitches they have submitted |
| Read comments for a pitch | **Click 'Comment Icon' on a Pitch** | Redirected to a comment's page that displays the pitch, comments(if any) and form to add a comment |
|Update Profile Picture|**Click 'Browse' on Profile Page**|Allows logged in user to choose a new profile pic.|

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* postgres database
* virtualenv

### Cloning
* In your terminal:
        
        $ git clone https://github.com/sokkyyy/one-minute-pitch-app.git
        $ cd one-minute-pitch-app

## Running the Application
* Creating the virtual environment:

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python 

* Installing Flask and other Modules:

        $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
        $ python3.6 -m pip install Flask-Script

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py tests

## Technologies Used
* Python3.6
* Flask
* Bootstrap
* Google Fonts
* FontAwesome
* Postgres SQL

## License
[Ray Ndegwa](https://github.com/sokkyyy/)
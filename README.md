

# Cook Book Plus
An online Cook Book where users can find and share their own recipies.

See it live on [Heroku](https://cookbook-project-4.herokuapp.com/)

## UX / User Stories

- As a user I want to share my recipies with the rest of the world
	- I can register an account with my unique name
	- I can post a recipe with ingredients and description and an optional image of the dish

- As a user I want to search for a certain recipe
	- I can do so by searching by name and/or ingredients

- As a user I don't know what exactly I'm looking for
	- The website allows me to sort and display recipies by different criteria. I might just choose something that has many upvotes, as it's likely to be tasty.

- As a user I want to change/delete my recipe
	- I can do so by logging in, navigating to the recipe in question ('Summary' link has all own recipies) and editing or deleting it.


## Features

- Searching for recipies
- Account creation / logging in
- Adding / deleting / editing recipies
- Different sort criteria
- Recipe upvoting
- Short summary/statistics of recipies available

### Future features

- Account options (editing personal info, display name, e-mail preferences, termination of the account)
- Comments section for each recipe where users can connect and share their experiences
- Pagination

## Technologies used

- Jquery
- Materialize
- Ajax
- Flask (python)

## Testing

 #### Registration
 The only rule is for the user name is to be unique. No further checks are made and as such the user can provide bogus e-mail address (not used anywhere) or a very short password. I've tried to create user with the same name and the website properly informs me such name already exists.
#### Login
Tried to log in as an existing user while providing a bad password, or no password and as expected the login is impossible.
#### Search
This feature searches for the keyword in both ingredients list and names of recipies. Initially, while adding ingredients to a recipe I did not control the ingredient's name letters case, which made it impossible to find the ingredients which started with, for ie Uppercase (because of them being keys in dictionary). When I found out about this limitation I started forcing all ingredient names to lowercase.

As a result the feature works as expected returning recpies that matches name or one of the ingredients, except for a few old recipies I've added initially.
 
 #### Summary
The link displays all the recipies that the logged in user posted, as well as the amount of recipies in each of the categories. Checking the page while being logged out displays only recipies count in each category, as expected.

#### Adding and updating a recipe
The javascript script checks for empty fields in both forms. Editing your name, as expected - is impossible. Clicking a plus button to add another ingredient is working as expected, clicking a 'minus' button to remove an ingredient also behaves as expected with a created/edited recipe not having any unexpected fields.

#### Other

I was not sure how to send an error response to the AJAX callback function (after upvoting) without triggering an actual error which you can see in the console when user has already voted. Nevertheless the behavior seems to be correct - a user can't vote for the same recipe more than once.

## Deployment

As I had a ready Github repository this was really easy.  I've run these commands from app root directory
```
pip freeze --local > requirements.txt
echo web: python app.py > Procfile
```
- Heroku
  * Created a new app
  * In the app settings -> deployment, connected to Github and chose project repository
  * Clicked Deploy from master branch


## Media
Random food images from google search

## Credits
I received inspiration for this project from CodeInstitute's milestone project outline
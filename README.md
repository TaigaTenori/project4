
# Cook Book Plus
An online Cook Book where users can find and share their own recipies.

## UX / User Stories

- As a user I want to share my recipies with the rest of the world
	- I can register an account with my unique name
	- I can post a recipe with ingredients and description and an optional image of the dish

- As a user I want to search for a certain recipe
	- I can do so by searching by name and/or ingredients

- As a user I don't know what I'm looking for
	- The website allows me to sort and display recipies by different criteria. I might just choose something that has many upvotes, as it's likely to be tasty.

- As a user I want to change/delete my recipe
	- I can do so by logging in, navigating to the recipe in question and editing or deleting it.


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

## Deployment

As I had a ready Github repository this was really easy.  I've run these commands from app root directory
```
pip freeze --local > requirements.txt
echo web: python app.py > Procfile
```
- Heroku
-- Created a new app
-- In the app settings -> deployment, connected to Github and chose project repository
-- clicked Deploy from master branch


## Media
Random food images from google search

## Credits
I received inspiration for this project from CodeInstitute's milestone project outline
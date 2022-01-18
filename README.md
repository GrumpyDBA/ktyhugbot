# Krypto Kitty Hug Bot


## What?
Kitty Hug Bot was written for the Krypto Kitty TG group, to make the community a better place in some small way.

---

## Who?
This is my first attempt at a python project and first attempt at a telegram bot. Forgive me for any ugliness in code and feel free to submit a PR.

---

## What does it do?
The bot Responds to a variety of inputs and gathers various kitty related resources from online APIs.
Currently you can ask for:

/hugz - will return either a feels good quote, a random internet kitty, or a procedurally generated cartoon cat.
/gief_my_kitty - will return a cartoon Kitty based upon the users TG ID. This is unique to them and should be static.

---


## What will it do?
- TODO - add sentiment analysis and respond to sad, mad etc messages. 
- TODO - add other kitty things, e.g. facts
- TODO - generate cats within app rather than API call
- TODO - generate names and backstories for the cats
- TODO - immortalise posts from the community
- TODO - many other things.
- TODO - error handling 
- TODO - tests - smeshts.
- TODO - fix local runs

---

## Where?
Currently deployed to Heroku.
Note that deploying to Heruko is a bit quirky.
Plenty of guides online but in short
- Get an account, create a droplet.
- Add your bot secret token key to Env variables within Heruko
- Create a proc file
- Create requirements using pip freeze > requirements.txt
- Ensure there's no pipenv stuff, (or if you do use pipenv, delete requirements.txt they don't play well with each other)
- Init the Heroku project
-- brew tap heroku/brew && brew install heroku
-- heroku login
-- heroku create
-- heroku git:remote -a ktyhugbot
- Push your changes to Heroku remote repo. This should auto build your app and deploy it.
-- git push heroku master
- check status with:
-- heroku logs --tail
- N.B. you can do this direct from your main git branch if you prefer. Or just keep your remote master as a seperate thing.  



---

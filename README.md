# Wine Connoisseur <br />

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### This is a full stack web application which is helpful for wine lovers to know more about wines and found the best variety according to their Country’s best wine.
## Technology Stack:
* Mysql
* Django Framework
* Python
* Html
* Css
* Javascript
* Jquery

## Features:

* User can read about price, Wine variety , winery .
* Responsive web app can be easily access in mobile, computer, tablet.
* You can find any wine’s variety of anywhere in the world.

## How to make webapp functional:
Assuming Google Chrome and Python3 is installed in your system.
* Clone Wine-Connoisseur repository in your home directory.
* Create virtual environment in <code> cd path/to/Wine-Connoisseur/wineproject' </code> <br />
`virtualenv .`
* Activate created virtualenv <br />
`source bin/activate`
* Install django in activated environment and other requirements <br />
`pip3 install django`<br>
`pip3 install django-widget-tweaks`<br />
`pip3 install django-filter>=2.0`<br />
`pip3 install django-filter>=2.0`<br />
* Install MySQL server
* Create new schema or database <br />
`CREATE SCHEMA schema_name ;`
* Import update.sql file to the database. <br />
`mysql -u username -p database_name < path/to/Wine-Connoisseur/DumpData/updated.sql`
* Update all the credentials of your database in `path/to/Wine-Connoisseur/wineproject/wineproject/settings.py`
* Now propagate all changes in django project. <br />
`python3 manage.py collectstatic` <br />
`python3 manage.py makemigratiion` <br />
`python3 manage.py migrate` <br />
* Finally run the server. <br />
`pip3 manage.py runserver`

## It will look something like this
![Image](https://github.com/lowjack1/Wine-Connoisseur/blob/master/wineproject/static/images/background/pic1.png) <br /><br />
![Image](https://github.com/lowjack1/Wine-Connoisseur/blob/master/wineproject/static/images/background/pic2.png) <br /><br />
![Image](https://github.com/lowjack1/Wine-Connoisseur/blob/master/wineproject/static/images/background/pic3.png) <br /><br />
![Image](https://github.com/lowjack1/Wine-Connoisseur/blob/master/wineproject/static/images/background/pic4.png) <br /><br />

# Scope For Improvements
* Infinite Scrolling makes the user stay for a longer time.
* Going through all the wines to find any particular wine is tedius, and while an alternative would be to add a search bar which can search any particular wine.


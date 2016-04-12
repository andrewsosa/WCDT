title: About
date: 2012-03-04


You must be wondering, what on *earth* is this?

Well one day, a bunch of programmers were sitting around thinking about how many celebrities had died recently. So they started a counter of "*Days since last celebrity death*" on their chalkboard.

But people kept erasing it, and the programmers were lazy, so one of them decided to make a web app to count for them.

### How It Works

This is a web app written in Flask, a Python framework. The data is fetched from Reddit by a separate web scrapping module.

The web scrapper pulls headlines from the Reddit API and identifies entities within each headline using the Natural Language Toolkit for Python. The entities are then cross-referenced with Wikipedia to check whether the entity is a person, and whether they are dead. The results are then uploaded to this server and stored in an instance of MongoDB. 

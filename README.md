# Commerce

This project's goal is to design an eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”

This project's source code includes 2 folders, a manage.py file which manages the whole application and an sqlite database file. Below are the **main files** under those folders.

auctions/:
* admin.py -> manages the content of the django admin panel.
* models.py -> stores the models of the application.
* urls.py -> stores the urls under this specific application
* views.py -> A view function, or view for short, is a Python function that takes a Web request and returns a Web response.([source](https://docs.djangoproject.com/en/3.1/topics/http/views/))
* the *static* and *templates* subfolders are for HTML and CSS source files.

commerce/:
* contains the application configuration files like *settings.py* and *urls.py*.

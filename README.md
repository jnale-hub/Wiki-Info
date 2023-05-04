# WIKI-INFO

## CS50 Web 2020 Project 1: Wiki

## CS50 Web - Programming with Python and JavaScript

### Project Aims:

The aim of this project was to build a Wikipedia-like online encyclopedia using the Python Django framework. Users can view available article entries, as well as search for entries on the site. New entries can be created by users, and existing entries can be edited. There is also a 'random page' function that selects and displays a page of the encyclopedia at random.


### Technologies:

* Back-end:
  * Python
  * Django

* Front-end:
  * HTML (with Django templating)
  * CSS (with some Bootstrap Components)


### Project Requirements:

* Entry Page: Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.
  * The view should get the content of the encyclopedia entry by calling the appropriate util function.
  * If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.
  * If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.
* Index Page: Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.
* Search: Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
  * If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
  * If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were Py, then Python should appear in the search results.
  * Clicking on any of the entry names on the search results page should take the user to that entry’s page.
* New Page: Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.
  * Users should be able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page.
  * Users should be able to click a button to save their new page.
  * When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.
  * Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.
* Edit Page: On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
  * The textarea should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial value of the textarea).
  * The user should be able to click a button to save the changes made to the entry.
  * Once the entry is saved, the user should be redirected back to that entry’s page.
* Random Page: Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.
* Markdown to HTML Conversion: On each entry’s page, any Markdown content in the entry file should be converted to HTML before being displayed to the user. You may use the python-markdown2 package to perform this conversion, installable via pip3 install markdown2.

When viewing any article on the site, an 'Edit Page' button is available. Clicking this takes users to a page with a form, allowing them to edit the contents of the article. When the form is updated and submited, the user is returned back to the updated article page.

Finally a 'Random Page' link is available in the side bar which when clicked will randomly select an article from all those available on the site and redirect the user to the selected article page.

Django form classes are used to handle all the forms on the site. The Django messages framework is also used to display success or error messages to the user when they attempt to create or edit articles.

### Usage:

Requires Python(3) and the Python Pacakage Installe (pip) to run:

* Install requirements (Django): `pip install -r requirements.txt`
* Run the app locally: `python manage.py runserver`

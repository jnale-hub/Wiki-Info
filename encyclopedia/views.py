from django.shortcuts import render
from markdown2 import Markdown
import random

from . import util


def convert_md_to_html(title):
    """
    Getting the content from the entry and convert it to html 
    content. If there is no content, return None. This function 
    is used to convert entries using the title.
    """
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


def index(request):
    """
    Render the index html and all the entries using 
    the list_entries function from util.
    """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        'active_page': 'home'
    })


def entry(request, title):
    """
    Convert the entry. If entry does not exist, deliver 
    an error message. Else, render the title and the converted 
    content on the entry html.
    """
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "This entry does not exist."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content,
        })


def search(request):
    if request.method == "POST":
        # Get the search entry using the q value
        entry_search = request.POST['q']
        html_content = convert_md_to_html(entry_search)
        # If there is an entry, render
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": html_content
            })
        # If there is None, make a recommendation using the letter in entries
        else:
            allEntries = util.list_entries()
            recommendation = []
            for entry in allEntries: 
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            if not recommendation:
                return render(request, "encyclopedia/error.html", {
                    "entry_search": entry_search,
                    "message": f'There is no result for <b>"{entry_search}"</b>. <a href="../new/">Try to add an entry</a>',
                })
            else:
                return render(request, "encyclopedia/search.html", {
                    "recommendation": recommendation
                })



def new_page(request):
    # Function to create a new page
    if request.method == "GET":
        return render(request, "encyclopedia/new.html", {'active_page': 'new_page'})
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        # Deliver an error message if there is an existing entry
        if titleExist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry page already exist."
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content,
            })


def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })


def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })


def rand(request):
    allEntries = util.list_entries()
    rand_entry = random.choice(allEntries)
    html_content = convert_md_to_html(rand_entry)
    return render(request, "encyclopedia/entry.html", {
        "title": rand_entry,
        "content": html_content,
        'active_page': 'rand'
    })

import random
from urllib.parse import unquote

from django.shortcuts import redirect, render
from markdown2 import Markdown

from . import util


def convert_md_to_html(title):
    """
    Convert Markdown content to HTML.
    """
    content = util.get_entry(title)
    markdowner = Markdown()
    if content is None:
        return None
    return markdowner.convert(content)


def index(request):
    """
    Render the index HTML and display a list of entries.
    """
    return render(
        request,
        "encyclopedia/index.html",
        {"entries": util.list_entries(), "active_page": "home"},
    )


def entry(request, title):
    """
    Render an entry by converting its Markdown content to HTML.
    """
    # Remove spaces and decode any URL-encoded spaces from the title
    title = unquote(title.replace(" ", "%20"))

    # Try to find an exact match for the provided title
    html_content = convert_md_to_html(title)

    if html_content is None:
        # If there's no exact match, attempt to find a case-insensitive match
        all_entries = util.list_entries()
        matching_entries = [
            entry for entry in all_entries if title.lower() == entry.lower()
        ]

        if matching_entries:
            # If a case-insensitive match is found, redirect to the correct entry
            return redirect("entry", title=matching_entries[0])

        # If no matches are found, display an error message
        return render(
            request,
            "encyclopedia/error.html",
            {"message": "This entry does not exist."},
        )

    return render(
        request,
        "encyclopedia/entry.html",
        {
            "title": title,
            "content": html_content,
        },
    )


def search(request):
    if request.method == "POST":
        entry_search = request.POST.get("q", "")
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(
                request,
                "encyclopedia/entry.html",
                {"title": entry_search, "content": html_content},
            )
        else:
            allEntries = util.list_entries()
            recommendation = [
                entry for entry in allEntries if entry_search.lower() in entry.lower()
            ]
            if not recommendation:
                return render(
                    request,
                    "encyclopedia/error.html",
                    {
                        "entry_search": entry_search,
                        "message": f'There is no result for <b>"{entry_search}"</b>. <a href="../new/">Try to add an entry</a>',
                    },
                )
            else:
                return render(
                    request,
                    "encyclopedia/search.html",
                    {"recommendation": recommendation},
                )


def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html", {"active_page": "new_page"})
    elif request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")

        if not title or not content:
            return render(
                request,
                "encyclopedia/error.html",
                {"message": "Title and content are required."},
            )

        if util.get_entry(title) is not None:
            return render(
                request, "encyclopedia/error.html", {"message": "Entry already exists."}
            )

        util.save_entry(title, content)
        return redirect("entry", title=title)  # Redirect to the newly created entry


def edit(request):
    if request.method == "POST":
        title = request.POST["entry_title"]
        content = util.get_entry(title)
        return render(
            request, "encyclopedia/edit.html", {"title": title, "content": content}
        )


def save_edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(
            request,
            "encyclopedia/entry.html",
            {"title": title, "content": html_content},
        )


def rand(request):
    allEntries = util.list_entries()
    rand_entry = random.choice(allEntries)
    html_content = convert_md_to_html(rand_entry)
    return render(
        request,
        "encyclopedia/entry.html",
        {"title": rand_entry, "content": html_content, "active_page": "rand"},
    )

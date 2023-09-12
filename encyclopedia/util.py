import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from urllib.parse import unquote  # Import the unquote function

def list_entries():
    """
    Returns a sorted list of all names of encyclopedia entries.
    """
    entry_files = default_storage.listdir("entries")[1]  # Get the filenames from the tuple
    # Decode the entry names to remove URL encoding
    return sorted([unquote(re.sub(r"\.md$", "", filename)) for filename in entry_files if filename.endswith(".md")])

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown content.
    If an existing entry with the same title already exists, it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such entry exists, the function returns None.
    """
    try:
        with default_storage.open(f"entries/{title}.md") as f:
            return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

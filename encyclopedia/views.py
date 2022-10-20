from django.shortcuts import render
import random
import markdown2

from . import util
from markdown2 import Markdown


markdown = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    if  request.method == 'POST':
        param = request.POST["search"]
        search_param = param.lower()
        list_entries_lowercase = [entry.lower() for entry in util.list_entries()]
        if  search_param in list_entries_lowercase:
            index = list_entries_lowercase.index(search_param)
            title_name = util.list_entries()
            return render(request, "encyclopedia/entry.html", {
                "title_name": title_name[index],
                "title": markdown.convert(util.get_entry(search_param))
            })
        else:
            return render(request, "encyclopedia/search.html", {
                "list_entry": util.list_entries(),
                "search_exist": util.search_exist(search_param), 
                "search_param": search_param 
            })
        
def create_page(request):
    if  request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]
        if  title and content: 
            if  title not in util.list_entries():
                util.save_entry(title, content)
                return render(request, "encyclopedia/entry.html",{
                    "title_name" : title,
                    "title": markdown.convert(util.get_entry(title))
                })
            else:
                return render(request, "encyclopedia/create_page.html",{
                    "error": True,
                    "text": title
                })
    return render(request, "encyclopedia/create_page.html",{
        "error": False
    })

def edit(request, title_name):
    return render(request, "encyclopedia/edit.html",{
        "title_name": title_name,
        "content": util.get_entry(title_name)
    })

def update(request):
    if  request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]
        if  title and content:
            util.save_entry(title, content)
            return render(request, "encyclopedia/entry.html",{
                "title_name" : title,
                "title": markdown.convert(util.get_entry(title))
            })
    return render(request, "encyclopedia/edit.html")

def random_page(request):
    all_titles = util.list_entries()
    random_title = random.choice(all_titles)
    return render(request, "encyclopedia/entry.html", {
        "title_name" : random_title,
        "title": markdown.convert(util.get_entry(random_title))
    })

def title(request, title):
   return render(request, "encyclopedia/entry.html", {
        "title_name" : title,
        "title": markdown.convert(util.get_entry(title))
    })
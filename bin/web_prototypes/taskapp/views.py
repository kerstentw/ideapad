from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):

    test_posts = [("propellor hat","A hat that has a giant propellor on it."),
                  ("hat propellor"," A giant propellor with a hat on it.")] 

    post_frame = "<br/><h3>{title}</h3><p>{post}</p><br/>"
    post_info = ''

    for post in test_posts:
        post_info = post_info + post_frame.format(title = post[0],post = post[1])

    templates = "index.html"

    templates = loader.get_template(templates)
        
    context = {
        "previous_posts" : post_info,
        "post_info" : request.POST}
    return HttpResponse(templates.render(context,request))

# Create your views here.

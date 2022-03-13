# Workflow startapp
> Web Browser (Request) >> mywebsite/urls.py >> blog/urls.py >> blog/urls.views >> templates >> Response

# Keypoint
1. startapp, most use `include` 
2. main urls (mywebsite/urls.py) for root urls and in blog urls(blog/urls.py) for sub dir
 
## use urls
**Basic Settings**
>mywebsite/urls.py >> `path('blog/', include('blog.urls'))` >> http://127.0.0.1:8000/blog

**Setting for path**
>blog/urls.py >> `path('blog/', view.index')` for http://127.0.0.1:8000/blog/blog (sub dir)

>blog/urls.py >> `path('', view.index')` for http://127.0.0.1:8000/blog (root dir)

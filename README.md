# Django Template Language

Introduce students to templating and DTL.

## What are the objectives?

- Understand what templates are and why use them
- Understand how to inject context into templates

## Pre-requisites

1. Clone this repo.
2. Create a virtual environment.
3. Install the deps using `pip install -r requirements/dev.lock`.
4. Create an admin account using `python manage.py createsuperuser` and create some `articles` and `authors`.

## Steps

1. Go to `articles/views.py` and create a detail view for an article, which looks something like this:

   ```python
   def get_article(request):
      return render(request, "article_detail.html")
   ```

2. Now create a templates folder inside the `articles` app, and explain that this is where our HTML will live.
3. Add the template `article_detail.html` and explain that it is named that way because it needs to match what we specified in the `render` call:

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta http-equiv="X-UA-Compatible" content="IE=edge" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>My article</title>
     </head>
     <body>
       <h1>My article</h1>
     </body>
   </html>
   ```

4. Our beautiful HTML needs to have some route for us to access, so add our detail view to `blog/urls.py`:

   ```python
   path('articles/', views.get_article),
   ```

5. Go to `http://localhost:8000/articles/` and show students that the template appears.
6. Let's add some context to our template to make it a bit more dynamic:

   ```python
   def get_article(request):
      context = {
         "article": {
            "title": "Natsu",
            "content": "Fire dragon slayer.",
            "author": "Hiro Mashima",
         },
      }
      return render(request, "article_detail.html", context)
   ```

7. Add the variables inside of our template and show them the `DTL` syntax (explain the dot-notation):

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta http-equiv="X-UA-Compatible" content="IE=edge" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>{{ article.title }}</title>
     </head>
     <body>
       <h1>{{ article.title }}</h1>
       <p>{{ article.content }}</p>
       <p>Written By: {{ article.author }}</p>
     </body>
   </html>
   ```

8. Now go to the browser and show them how the article looks like.
9. Add the `article id` in the `urls` to show them that this can be even more dynamic:

   ```python
   # urls.py
   path('articles/<int:article_id>', views.get_article),

   # views.py
   def get_article(request, article_id):
      context = {
         "article": {
            "id": article_id,
            "title": "Natsu",
            "content": "Fire dragon slayer.",
            "author": "Hiro Mashima",
         },
      }
      return render(request, "article_detail.html", context)
   ```

10. Add the `id` to the markup:

    ```html
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{{ article.title }}</title>
      </head>
      <body>
        <h1>{{ article.id }} - {{ article.title }}</h1>
        <p>{{ article.content }}</p>
        <p>Written By: {{ article.author }}</p>
      </body>
    </html>
    ```

11. Show them different paths gives them different articles. Now let us actually make our website dynamic:

    ```python
    def get_article(request, article_id):
       article = Article.objects.get(id=article_id)
       context = {
          "article": {
             "id": article_id,
             "title": article.title,
             "content": article.content,
             "author": str(article.author),
          },
       }
       return render(request, "article_detail.html", context)
    ```

    **Notice** the `str` call, this is so we can get the `first_name` and `last_name`.

12. Now show them existing articles, and non-existent articles.

# MRO Blog Update

This project demonstrates a Django application to manage blog posts with content replacement and voting functionality, as described in the job ad.

## Features

- Replace blog post content with new content.
- Update voting results for blog posts.
- View aggregated voting results.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/toniilic/mro-blog-update.git
    cd mro-blog-update
    ```

2. **Set up the virtual environment and install dependencies:**

    ```bash
    python3 -m venv mro_blog_update_env
    source mro_blog_update_env/bin/activate
    pip install django
    ```

3. **Run migrations:**

    ```bash
    python manage.py makemigrations blog
    python manage.py migrate
    ```

4. **Create a superuser (optional for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

1. **Access the admin interface:** [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
2. **Add a blog post in the admin interface.**
3. **View and update blog posts:** [http://127.0.0.1:8000/blog/post/1/](http://127.0.0.1:8000/blog/post/1/)
4. **View voting results:** [http://127.0.0.1:8000/blog/results/](http://127.0.0.1:8000/blog/results/)

## Project Structure

```
mro-blog-update/
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   └── blog/
│   │       ├── blog_post.html
│   │       └── voting_results.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── mro_blog_update/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Future Improvements

- Enhance the UI for a better user experience.
- Add authentication for content editors.
- Implement AJAX for real-time voting updates.

## License

This project is licensed under the MIT License.


# Kingston Library Management System

A web-based library management system built with Django. It allows users to browse, borrow, and return books, and provides admin features for managing the library collection.

## Features

- User-friendly interface for browsing books
- Search and filter books by name and author
- Borrow and return books with tracking
- Admin login for book entry and management
- Address system for book location (Shelf-Level-Column)
- Borrowed books tracking with due date and fine calculation
- Responsive design

## Technologies Used

- Python 3.x
- Django
- HTML, CSS (Montserrat & Sriracha fonts)
- JavaScript

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/chrisI0/library-kingston.git
   cd library-kingston
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the app**
   Open your browser and go to `http://127.0.0.1:8000/`

## Admin Login

- **Username:** kingston@lib.com
- **Password:** admin

## Project Structure

- `app1/` - Main Django app with models, views, templates
- `templates/` - HTML templates for all pages
- `static/` - Static files (CSS, JS, images)
- `db.sqlite3` - Default SQLite database

## How the Fine System Works

- Each borrowed book has a 30-day limit.
- If a book is overdue, a fine of 1 unit per day is applied.
- The fine and remaining days are shown in the borrowed books section.

## Deployment

- For static hosting, use GitHub Pages (frontend only).
- For full Django hosting, use platforms like Heroku, PythonAnywhere, AWS, or Vercel.
- Vercel can be used for hosting static frontends or serverless functions. See [Vercel Documentation](https://vercel.com/docs) for details.

## Screenshots

<img width="1919" height="1079" alt="Screenshot 2025-07-16 185621" src="https://github.com/user-attachments/assets/811c6430-cd26-4cc7-a39f-7cf3906a5da0" />
<img width="1919" height="1079" alt="Screenshot 2025-07-16 185637" src="https://github.com/user-attachments/assets/e171db28-c7ba-4af6-ba01-28a6ba12ec37" />
<img width="1919" height="1079" alt="Screenshot 2025-07-16 185742" src="https://github.com/user-attachments/assets/45c8eba3-354a-4553-a7ad-9f568fa6b54f" />

<img width="1919" height="1079" alt="Screenshot 2025-07-16 185702" src="https://github.com/user-attachments/assets/83edffdd-3ec2-41d6-bad7-2d70ad2185b5" />
<img width="1919" height="1079" alt="Screenshot 2025-07-16 185651" src="https://github.com/user-attachments/assets/a47a023c-d64b-4b97-8074-0efd3ee453d0" />
<img width="1919" height="1079" alt="Screenshot 2025-07-16 185714" src="https://github.com/user-attachments/assets/1b5a71a2-a226-4c54-beb3-8d0568a42372" />



## Author

Christy Ouseph


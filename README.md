# Book Bank Management System  

A web-based application designed to manage a book bank system efficiently. This project includes features for user registration, book borrowing, and returning, along with an intuitive interface for managing books and user profiles.

## Features  

1. **User Registration and Authentication**  
   - Secure user registration and login system.  
   - Profiles for users to view and manage their borrowing history.  

2. **Book Management**  
   - Add, update, and delete book records in the database.  
   - Categorization of books for easy search and management.  

3. **Borrowing and Returning Books**  
   - Users can borrow available books.  
   - Borrowed books are tracked, and users can return them within the specified time.  

4. **Static and Dynamic Pages**  
   - Beautiful static pages with images for user interface.  
   - Templates include `home.html` for the main interface.  

5. **Admin Panel**  
   - Admin dashboard to oversee book and user activities.  

## Technologies Used  

- **Backend**: Django  
- **Frontend**: HTML, CSS  
- **Database**: MySQL  
- **Static Files**: Images stored under `static/images`.  

## Prerequisites  

- Python 3.x  
- Django 4.x  
- MySQL Server  
- Virtual Environment (optional)  

## Installation and Setup  

1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/[your-username]/[your-repo-name].git  
   cd BookBankManagementSystem  
   ```  

2. **Create a Virtual Environment** (optional but recommended)  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. **Install Dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Set Up the Database**  
   - Create a MySQL database named `book_bank`.  
   - Update `settings.py` with your database credentials:  
     ```python  
     DATABASES = {  
         'default': {  
             'ENGINE': 'django.db.backends.mysql',  
             'NAME': 'book_bank',  
             'USER': 'your_username',  
             'PASSWORD': 'your_password',  
             'HOST': 'localhost',  
             'PORT': '3306',  
         }  
     }  
     ```  

5. **Run Migrations**  
   ```bash  
   python manage.py makemigrations  
   python manage.py migrate  
   ```  

6. **Create a Superuser**  
   ```bash  
   python manage.py createsuperuser  
   ```  

7. **Run the Development Server**  
   ```bash  
   python manage.py runserver  
   ```  

8. **Access the Application**  
   Open `http://127.0.0.1:8000` in your browser.  

## Screenshots/Demos  

*(Include screenshots or demo GIFs if available)*  

## Contributing  

Contributions are welcome! Feel free to fork the repository and submit pull requests.  

## License  

This project is licensed under the [MIT License](LICENSE).  

---

Let me know if you'd like further refinements or additional sections!

# karvaaa_django

1. Install Python:
   - Ensure Python is installed on your machine. Download it from python.org.

2. Clone project:
   - Open a terminal or command prompt.
   - Run: git clone https://github.com/prashant-paliwal/karvaaa_django.git

3. Create Virtual Environment:
   - Open a terminal or command prompt.
   - Run: python -m venv env

4. Activate Virtual Environment:

   For Windows:
   - Navigate to the 'Scripts' directory: cd env/Scripts
   - Activate the virtual environment: activate

   For Linux:
   - Activate the virtual environment: source env/bin/activate

5. Install Dependencies:
   - Go to the project root directory: cd karvaaa_django/karvaa_chatbot (check path carefully)
   - Install project dependencies: pip install -r requirements.txt

6. Run Migrations: (Optional for now)
   - Create and apply database migrations:
     - Run: python manage.py makemigrations
     - Run: python manage.py migrate

7. Running the Test Suite:
   - Run test cases: python manage.py test

8. Running the Server:
   - Start the development server: python manage.py runserver

After these steps, you can access the Chatbot at http://127.0.0.1:8000/api/chat in your web browser.
* Each time when you refresh it will return different response from chat api.


**If you have further queries, feel free to reach out at my email - prashantpaliwal203@gmail.com **
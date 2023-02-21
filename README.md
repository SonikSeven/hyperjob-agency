# HyperJob Agency

## About The Project

HyperJob Agency is a Django web application designed to facilitate job postings and resume submissions. This platform provides a user-friendly interface for job seekers to submit their resumes and for employers to post vacancies. It has separate sections for handling user accounts, including signup, login, and logout functionalities, and for displaying resumes and vacancies. 

## Key Features:

- **User Authentication**: Includes user sign-up, login, and logout functionalities.
- **Resume Submission**: Allows authenticated users to submit their resumes.
- **Vacancy Posting**: Permits staff users to post job vacancies.
- **Dynamic Web Pages**: Utilizes Django's powerful URL and view handling to serve dynamic content based on user roles and authentication status.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

1. **Clone the Repository**

   Open a terminal and run:
   ```
   git clone https://github.com/SonikSeven/hyperjob-agency.git
   ```

2. **Navigate to the project directory**
   ```
   cd hyperjob-agency
   ```

3. **Install Dependencies**

   It is recommended to use a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # For Unix/macOS
   venv\Scripts\activate  # For Windows
   ```
   Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. **Set Up Django**
   
   Navigate to the project root directory (`hyperjob-agency`) where `manage.py` is located, then run migrations to prepare your database.
   ```
   python manage.py migrate
   ```

5. **Start the Server**
   ```
   python manage.py runserver
   ```
   This command starts a local server. By default, the application runs at `http://127.0.0.1:8000/`.

## Usage

- Visit `http://127.0.0.1:8000/` in your web browser to access the HyperJob Agency portal.
- Utilize the sign-up page to create a new user account.
- Once logged in, you can navigate to the resumes or vacancies sections as per your role:
  - Regular Users can submit resumes.
  - Staff Users can post vacancies.

## License

Distributed under the MIT License. See [LICENSE](LICENSE.txt) for more information.

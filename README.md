 
# Django-Capstone-project ReadMe

Welcome to the Portfolio Site, a web application built using Django and designed to showcase your work, skills, and projects. This ReadMe file provides an overview of the project, installation instructions, key features, and other relevant information.

## Project Overview

The Portfolio Site is a dynamic website where you can display your projects, skills, and contact information. The site is built with Django, a high-level Python web framework, and incorporates HTML, CSS, JavaScript, and Bootstrap for design and interactivity.

## Key Features

- **Project Showcase**: Display your portfolio projects with descriptions, images, and links to repositories or live demos.
- **Skill Listing**: Highlight your skills and expertise in different technologies and tools.
- **Contact Form**: Allow visitors to contact you directly through a simple form.
- **Responsive Design**: The site is fully responsive, adapting to different screen sizes and devices.

## Installation Instructions

To run the Portfolio Site on your local environment, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Open in Browser**
   - Open a web browser and navigate to `http://127.0.0.1:8000/` to view the portfolio site.
   - If the above url renders a page not found error try navigating to through the login page at 'http://localhost:8000/user_auth/login/' and create a new user. 
https://github.com/Abx11/Django-Capstone-project
## Customization

To customize the Portfolio Site for your own use, consider the following:

- **Templates**: Modify the HTML templates in the `templates` directory to change the site structure and content.
- **Static Files**: Update CSS, JavaScript, and image files in the `static` directory to alter the site's design and behavior.
- **Models**: Edit the Django models to add or change database fields for projects, skills, etc.

## Contribution and Support

Contributions are welcome! If you'd like to contribute to this project, please open a pull request or create an issue to discuss changes. For support or questions, contact the repository maintainer or submit an issue on GitHub.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Contact Information

For inquiries, please contact [Your Contact Information].

---

We hope you enjoy working with the Portfolio Site. If you have any feedback or suggestions, we'd love to hear from you!

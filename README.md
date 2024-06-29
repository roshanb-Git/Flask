## For a Machine Learning (ML) engineer or developer working with Flask, it’s important to understand both the basics of Flask as a web framework and how to integrate ML models into a Flask application. Here are the key points to know:

# Basics of Flask

1) Framework Overview:

Flask is a lightweight, micro web framework written in Python.
It's designed to be simple and easy to use, with a modular approach that allows you to pick and choose the components you need.

2) Routing:

Define routes using @app.route('/path') to map URLs to Python functions.
Understand HTTP methods (GET, POST, etc.) and how to handle them in Flask.

3) Request and Response:

Handle incoming data using request object.
Return responses using return statement with strings, HTML, or templates.

4) Templates:

Use Jinja2 templating engine for rendering HTML with dynamic data.
Understand template inheritance, including base templates and extending templates.

5) Forms:

Handle form submissions and process form data.
Use Flask-WTF for enhanced form handling and validation.

6) Static Files:

Serve static files (CSS, JavaScript, images) using the static folder.
Use url_for('static', filename='path/to/file') to generate URLs for static files.

7) Blueprints:

Use Blueprints to organize application components into reusable modules.
Understand how to register Blueprints in the main application.

8) Configuration:

Configure your Flask app using environment variables, config files, or object-based configurations.
Manage different configurations for development, testing, and production environments.
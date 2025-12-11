# Dockerized Flask Application Guide

This guide details the steps to create, containerize, and run a fast, modern Flask web application using Docker.

## Project Overview

We will build a Student Portal registration application with a modern, responsive UI, containerize it using Docker, and run it with port mapping.

### Directory Structure

```text
student-portal/
├── app.py
├── requirements.txt
├── Dockerfile
└── templates/
    └── index.html
```

---

## Step 1: Create the Application

### 1. `app.py`
This is the main Flask application entry point. We have enhanced it to serve a proper HTML template.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # In production, use a WSGI server like gunicorn. 
    # For this demo, the built-in server is fine.
    app.run(host="0.0.0.0", port=5000)
```

### 2. `templates/index.html`
Create a folder named `templates` and add `index.html`. This file contains the enhanced UI with modern styling.

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #4f46e5;
            --primary-hover: #4338ca;
            --bg-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --card-bg: rgba(255, 255, 255, 0.95);
        }

        body {
            font-family: 'Inter', sans-serif;
            background: var(--bg-gradient);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0;
            color: #1f2937;
        }

        .container {
            background: var(--card-bg);
            padding: 2rem 3rem;
            border-radius: 1rem;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            width: 100%;
            max-width: 400px;
            animation: fadeIn 0.6s ease-out;
        }

        h1 {
            color: #111827;
            font-size: 1.875rem;
            font-weight: 600;
            text-align: center;
            margin-bottom: 0.5rem;
        }

        .subtitle {
            text-align: center;
            color: #6b7280;
            margin-bottom: 2rem;
        }

        .form-group {
            margin-bottom: 1.25rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-size: 0.875rem;
            font-weight: 500;
            color: #374151;
        }

        input {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #d1d5db;
            border-radius: 0.5rem;
            font-size: 1rem;
            transition: all 0.2s;
            box-sizing: border-box; /* Ensures padding doesn't affect width */
        }

        input:focus {
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
        }

        button {
            width: 100%;
            background-color: var(--primary-color);
            color: white;
            padding: 0.75rem;
            border: none;
            border-radius: 0.5rem;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: background-color 0.2s;
            margin-top: 1rem;
        }

        button:hover {
            background-color: var(--primary-hover);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Student Portal</h1>
        <p class="subtitle">Secure Registration Form</p>
        <form>
            <div class="form-group">
                <label for="name">Full Name</label>
                <input type="text" id="name" name="name" placeholder="John Doe" required>
            </div>
            
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" placeholder="john@university.edu" required>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" placeholder="+1 (555) 000-0000">
            </div>
            
            <div class="form-group">
                <label for="department">Department</label>
                <input type="text" id="department" name="department" placeholder="Computer Science">
            </div>

            <button type="submit">Register Now</button>
        </form>
    </div>
</body>
</html>
```

### 3. `requirements.txt`
Specify the dependencies.

```text
Flask==3.0.0
```

---

## Step 2: Containerize with Docker

### `Dockerfile`
Create a `Dockerfile` in the root directory to define the image.

```dockerfile
# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory to inside the container
WORKDIR /app

# Copy dependency definition first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
```

---

## Step 3: Build and Run

Open your terminal in the directory containing these files.

### 1. Build the Docker Image
This command reads the Dockerfile and builds an image named `student-portal` with tag `v1`.

```bash
docker build -t student-portal:v1 .
```

*Expected Output:*
```text
[+] Building 2.5s (10/10) FINISHED
...
 => writing image sha256:...
 => naming to docker.io/library/student-portal:v1
```

### 2. Run the Container
Run the container in detached mode (`-d`), mapping host port 5000 to container port 5000.

```bash
docker run -d --name student-portal -p 5000:5000 student-portal:v1
```

*Expected Output:*
```text
a1b2c3d4e5f6... (container ID)
```

---

## Step 4: Verify

You can verify the application is running by accessing it in your browser or using `curl`.

### Browser
Open [http://localhost:5000](http://localhost:5000)

### Terminal (Curl)
```bash
curl -s http://localhost:5000 | head -n 15
```

*Expected Output (Snippet):*
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    ...
    <title>Student Portal</title>
```

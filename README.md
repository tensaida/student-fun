# Give every student a chance!

This is a random student generator to make your tutorials more engaging and fun! You can get started pretty quickly:

1. Clone the repo
2. Add a file called `students.txt` with the names of your students to the directory where `server.py` is located.
3. Create a virtual environment and run `server.py`

# Getting Started with Your Python Virtual Environment

This README.md file will guide you through the process of setting up a Python virtual environment, activating it, and running a Python server.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python 3.x (You can download it from [python.org](https://www.python.org/downloads/))
- `venv` module (typically included with Python 3.x)
- `server.py` file (assuming you have a Python server script named `server.py`)

## Step 1: Create a Virtual Environment

Open your terminal or command prompt and navigate to the directory where you have your `server.py` file. Then, follow these steps to create a Python virtual environment:

```bash
# Navigate to your project directory (replace 'project_directory' with the actual path)
cd /path/to/your/project_directory

# Create a Python virtual environment (replace 'venv' with your preferred name)
python3 -m venv venv
```

This command will create a new directory named `venv` (or your specified name) containing a clean Python environment.

## Step 2: Activate the Virtual Environment

Now that you've created your virtual environment, you need to activate it. Activation ensures that your terminal session uses the isolated Python environment you just created.

### On Windows:

```bash
venv\Scripts\activate
```

### On macOS and Linux:

```bash
source venv/bin/activate
```

You should see the virtual environment name in your terminal prompt, indicating that it's activated.

## Step 3: Run Your Python Server

With the virtual environment activated, you can now run your Python server using the `server.py` script:

```bash
python3 server.py
```

Your server should now be up and running, and you can access it through a web browser or other HTTP clients.

## Deactivating the Virtual Environment

When you're finished with your project and want to exit the virtual environment, simply run:

```bash
deactivate
```

This will return you to your system's global Python environment.

## Conclusion

You've successfully set up and activated a Python virtual environment and run your Python server. If you encounter any issues or have questions, feel free to ask for assistance. Happy coding!
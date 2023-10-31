# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables (modify these as needed)
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=streaming_project.settings

# Create and set the working directory
WORKDIR /main

# Copy the current directory contents into the container at /app
ADD . /main

# Install any needed packages specified in requirements.txt
RUN pip install -r streaming_project/requirements.txt

# Expose a port for the Django development server
EXPOSE 8000

# Define the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
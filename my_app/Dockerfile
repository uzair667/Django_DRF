# Use an official Python runtime as a parent image
FROM python:latest

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /my_app

# Install dependencies
COPY requirements.txt /my_app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /my_app/

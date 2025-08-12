# Base image -> can be specified if building from scratch & create own image
FROM python:3.12-rc-bookworm 

# Set working directory in the container to /app -> default to Flask app
WORKDIR /app

# Copy current directory (.) contents into the container at /app
COPY . /app

# Install required packages
# --no-cache-dir -> not store downloaded packages in cache dir
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=app.py

# Add labels to image
# Can add multiple labels, common examples: vendor, version, description, etc.
# Use \ to avoid CL parsing
# Option 1
LABEL "com.example.site"="Docker Project"
LABEL version="1.0"
LABEL description="My first Docker project example website \
using Python base image!"

# # Option 2 ->using \ to put evenything in one line, like:
# LABEL "com.example.site"="Docker Project" \
# version="1.0" \
# description="My first Docker project example website \
# using Python base image!"

# Run the command to start Flask app -> added python & port for more reliable execution 
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]

# dockerfile ONLY USE THE FINAL COMMAND DEFINED -> make sure you got the right one here!
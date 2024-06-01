# Use an official Python 3.x image as the base
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set the working directory to /app/src
WORKDIR /app/src

# Define environment variables
ENV RSS_URL=https://news.yahoo.com/rss
ENV OUTPUT_FORMAT=json
ENV LIMIT=2

# Run the command to start the application with parameters
CMD python rss_reader.py ${RSS_URL} --${OUTPUT_FORMAT} --limit ${LIMIT}

# Using python 3.9 as base image
FROM python:3.9

# Set the working directory to /code 
WORKDIR /code

# Copy requirements.txt file to the working directory
COPY requirements.txt requirements.txt

# Install the requirements 
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . .

# Make port 6789 available to the world outside this container
EXPOSE 7000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7000","--timeout-keep-alive", "60"]
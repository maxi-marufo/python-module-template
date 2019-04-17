# Use an official Python runtime as a parent image
FROM python:3.5.2

# Set the working directory to /app
WORKDIR /dir

# Copy the current directory contents into the container at /app
COPY . /dir

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt -r test-requirements.txt --process-dependency-links --disable-pip-version-check --upgrade \
&& python setup.py install

# Run nosetests when the container launches
CMD [ "python", "setup.py" ,"nosetests"]

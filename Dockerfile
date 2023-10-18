# Base image with python
FROM python:3.9

#Working directory for the application
WORKDIR app/

#Copy code from system 
COPY app.py .

#Install required libraries
RUN pip install flask

#Run the application
CMD ["python","app.py"]


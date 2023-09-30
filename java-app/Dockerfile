
# Getting base image
FROM openjdk:11

# Create working directory where all code will be kept
WORKDIR app/

#Copy the app to current directory of container
COPY Hello.java .

#Compile code
RUN javac Hello.java

#Run java compiled code
CMD ["java","Hello"]

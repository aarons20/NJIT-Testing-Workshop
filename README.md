# NJIT-Testing-Workshop
This repo is intended for demonstrating how unit testing works in a professional setting. We will be using Sonarqube to do our code analysis with our simple python project. You'll be needing to install a few itmes to get started. Although installing Sonarqube is not necessary, this readme will provide simple instructions to install Sonarqube locally.  

## Installing SonarQube
### The following instructions will be installing SonarQube locally (PC/Laptop) on Windows. 

You'll need to install two items for SonarQube, the [SonarQube Platform](https://docs.sonarsource.com/sonarqube/9.9/analyzing-source-code/overview/) and the SonarScanner. Read more about the difference [here](https://stackoverflow.com/questions/43029897/sonarqube-vs-sonarscanner#:~:text=Sonarqube%20provides%20the%20intelligence%20to,organisation%20that%20developed%20SonarQube%20too.)

To install the SonarQube Platform you can go to https://www.sonarsource.com/products/sonarqube/downloads/ and installed the community edition.  After installing the platform you can install the SonarScanner [here](https://docs.sonarsource.com/sonarqube/9.9/analyzing-source-code/scanners/sonarscanner/). Once downloaded you'll need to extract both zip files and then go 
to the SonarQube Platform folder and you can click on the SonarStart.exe to start it. 

### PainPoints to be mindful

1. Storage - Make sure you have enough storage space when installing SonarQube locally. At the time of this, I had an issue where it was requesting at least 50gbs of free space.
2. Java Version - In the [requirement](https://docs.sonarsource.com/sonarqube/9.9/requirements/prerequisites-and-overview/) section you'll see that you need Java version 11 or 17 to run SonarQube. I went with 17 because version 11 was deprecated.  Go to your CMD and type the command below to check what version number you currently have.

CMD: 
```
java -version
```
Note:  If you have another version of Java installed you can change your environment variables to set version 17  as the default path. 



# NJIT-Testing-Workshop
This repo is intended for demonstrating how unit testing works in a professional setting. We will be using Sonarqube to do our code analysis with our simple python project. You'll be needing to install a few items to get started. Although installing Sonarqube is not necessary, this readme will provide simple instructions to install Sonarqube locally.  

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

### Installing PyTest

You'll need to install PyTest by using the command below. This is the testing libraries we will be using for Python. To view examples of how we will use them within this project you can click [here](https://github.com/PeePeePirate/NJIT-Testing-Workshop/blob/main/tests_bank.py)

For more instructions you can visit their site: https://docs.pytest.org/en/7.4.x/getting-started.html


CMD:
```
pip install -U pytest
```

### Installing Coverage

The final item you'll need to install is [Python Coverage](https://coverage.readthedocs.io/en/7.3.2/). This package will be used to create the report that will be feed into sonarqube to analysis.

For more insturctions you can visit their site: https://coverage.readthedocs.io/en/7.3.2/


CMD:
```
python3 -m pip install coverage
```

### Workshop Instructions

#### Test Driven Development (TDD) 
#### Banking Application

#### Project Overview:​

You are a new software engineer for a small credit union. The Credit Union is looking to modernize and has hired you to help develop software for their ATMs. As it stands, the application is lacking in the required features. 

It is your responsibility to implement the required tests and features needed to create a well-tested and functional application. 

#### Objectives:​ 

- Create In-depth unit tests for all functions of the application. 

- Implement necessary features into the application. 

#### ​​Requirements/Task(s):​ 

1. Clone the GitHub Repository 

2. Switch and work off the NJIT---Testing-Branch 

3. Create your assigned function(s) for the application. 

4. Stage and commit your changes. 

5. Push your changes to the NJIT---Testing-Branch. 

6. ​​Add the link to your project here:​ 

    a. Github Repo: https://github.com/PeePeePirate/NJIT-Testing-Workshop.git 

#### Deposit Function requirements: 

- Input validation tests  

- Letters  

- Characters  

- Bool  

- Account balance in negative  

- Account balance zero  

- Account balance in the positive 

#### Withdraw function requirements: 

- Input validation  

- Letters  

- Characters  

- Bool 

- Withdraw to zero  

- Withdraw to positive or negative 

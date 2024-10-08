# **CORTEVA Weather API**


## **Overview**
The CORTEVA Weather API is a part of the coding challange, that provides endpoints for ingesting, retrieving, and processing weather data. This application is built with Flask and Flask-RESTx, allowing interaction with weather data stored in a MySQL database. It includes functionalities for data ingestion, fetching weather data, and generating weather statistics. However this application is not hosted at the moment, 


## **Features**
   -  **Weather Data Ingestion:** Inserts data from the weather data file into MySQL database
   -  **Weather Data Rerieval:** Fetches weather data from database based on user filters(whereever applicable)
   -  **Weather Data Statistics:** Generates few insights on the weather data, also can be filtered


## **Installation**

### **Prerequisites**
   -  Python 3.9 or higher
   -  Git
   -  Flask
   -  Flask-RestX
   -  MySQL Database or any Relational Database (some queries wll change accordingly)
   -  Python packages specified in requirements.txt
   -  Access to github repository ->  [corteva_weather_apis](https://github.com/subratapanda17/corteva_weather_apis)
   - Access to raw data -> [data link github](https://github.com/corteva/code-challenge-template/tree/main/wx_data)


### **Setup**
   1. Clone the repository

      ```bash
      git clone https://github.com/subratapanda17/corteva_weather_apis.git
      cd corteva_weather_apis

   2. Create a virtual environment
      - using python virtualenv
         ```bash
         python -m venv corteva_weather_venv
         source corteva_weather_venv/bin/activate

      - using conda
         ```bash
         conda create -n "corteva_weather_env" python=3.9
         conda activate corteva_weather_env

   3. Install Dependencies
      ```bash
      pip install -r requirements.txt
      ```
   
   4. Raw Data
      - put the raw weather data files downloaded from [here](https://github.com/corteva/code-challenge-template/tree/main/wx_data) and put it inside the directory _`corteva_weather_apis/data/wx_data/`_
   

   5. Database Model
      - The database modelling has been done externally through MySQL DB. steps are as follows :- 
         -  __Step 1:__ Connect to MySQL Database
            ```bash
            mysql -u <user> -p
            Enter password:
            ```
            enter you password and connect to the database
      
         -  __Step 2:__ Create new Database
            ```sql
            CREATE DATABASE new_database;
            ```
         -  __Step 3:__ Select the database
            ```sql
            USE new_database;
            ```
         - __Step 3:__ Create New Table
            ```sql
            CREATE TABLE corteva_weather_record (
                  id INT PRIMARY KEY AUTO_INCREMENT,
                  weather_station_id VARCHAR(20) NOT NULL,
                  date INT NOT NULL,
                  maxtemp FLOAT NOT NULL,
                  mintemp FLOAT NOT NULL,
                  rainfall FLOAT NOT NULL,
                  uniq_id VARCHAR(100) NOT NULL UNIQUE,

                  INDEX idx_date (date),
                  INDEX idx_wst_id (weather_station_id),
                  INDEX idx_uniq_id (uniq_id)
            );
            ```
   


## **Running the Application**

### **Database Details**
   1. Connect to your mysql database

   2. Create a .env file at the root level of the api directory
      ```bash
      touch .env
      ```

   3. Add your MySQL db url in the .env file
      ```python
      MYSQL_LOCAL_URL = mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database_name>
      MYSQL_DEV_URL = mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database_name>
      MYSQL_PROD_URL = mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database_name>
      ```
   4. Configure database details in _`corteva_weather_apis/api/config/settings.py`_
         ```python
         DB_TYPE = 'LOCAL'
         SQL_TABLE_NAME = 'corteva_weather_record'
         ```

### **flask run**
   ```bash
   flask run --host=0.0.0.0 --port=5000 --reload
   ```

### **Docker** _(if used)_
   ```bash
   docker build -t corteva-weather-api .
   docker run -p 5000:5000 corteva-weather-api
   ```

### **Accessing the OpenAI Docs**
   - http://localhost:5000/docs/



## **API Details**

### **API Endpoints**
   - `/api/weatherIngestion/`
   - `/api/getWeatherData/`
   - `/api/getWeatherStats/`


### **API Details**
   1. **weatherIngestion**
      - url: http://localhost:5000/api/weatherIngestion/
      - method: `GET`
      - parameters: _None_

   2. **getWeatherData**
         - url: http://localhost:5000/api/getWeatherData/
         - method: `GET`
         - parameters: 
            - `date`: int (optional) ||    _YYYYMMDD format_
            - `weather_station_id`: str (optional) ||     _'USC00111280'_
            - `page_no`: int (optional) ||    _1_

   3. **getWeatherStats**
         - url: http://localhost:5000/api/getWeatherStats/
         - method: `GET`
         - parameters: 
            - `year`: int (optional) ||    YYYY format
            - `weather_station_id`: str (optional) ||    'USC00111280'
         
### **Configs & Logs**
   -  _`corteva_weather_apis/api/logs/app.log`_  -> stores the logs
   -  _`corteva_weather_apis/api/config/settings.py`_  -> tesing configurations and contant variables

### **Tests**
   - run tests using the following command from root directory
      ```bash
      pytest
      ```

## **Contributing**
   1. Fork the repository
   2. create new branch 
      ```bash
      git checkout -b <feature-branch>
      git pull origin master
      ```
   3. Commit changes
      ```bash
      git add <path/to/file>
      git commit -m "commit message"
      ```
   4. Publish changes
      ```bash
      git push origin <feature-branch>
      ```
   5. Any valuable addition to this app will be highly appreciated

## **Contact**
   For any additional queries contact
   - Email: subratapanda56@gmail.com
   - GitHub: [subratapanda17](https://github.com/subratapanda17)
   - LinkedIn: [subratapandav](https://www.linkedin.com/in/subratapandav/)

      



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
   -  MySQL Database or any SQL Database (some queries wll change accordingly)
   -  Python packages specified in requirements.txt

### **Setup**
   1. Clone the repository

      ```bash
      git clone https://github.com/subratapanda17/corveta_weather_apis.git
      cd corveta_weather_apis

   2. Create a virtual environment
      - using python virtualenv
         ```bash
         python -m venv corteva_weather_venv
         source corteva_weather_venv/bin/activate

      - using conda
         ```bash
         conda create -n "corteva_weather_env"
         conda activate corteva-env

   3. Install Dependencies
      ```bash
      pip install -r requirements.txt
   

## **Running the application**

### **Database Details**
   1. Connect to your mysql database

   2. Create a .env file at the root level of the api directory
      ```bash
      touch .env

   3. Add your MySQL db url in the .env file
      ```python
      MYSQL_LOCAL_URL = mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database_name>
      MYSQL_DEV_URL = mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database_name>
      MYSQL_PROD_URL = mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database_name>

### **flask run**
   ```bash
   flask run --host=0.0.0.0 --port=5000 --reload

### **Docker**
   ```bash
   docker build -t corveta-weather-api .
   docker run -p 5000:5000 corveta-weather-api

### **API Endpoints**
   - `/api/weatherIngestion/`
   - `/api/getWeatherData/`
   - `/api/getWeatherStats/`

### **API Docs URL**
   - `http://localhost:5000/docs/`

### **API Details**
   1. **weatherIngestion**
      - url: http://localhost:5000/api/weatherIngestion/
      - method: GET
      - parameters: None

   2. **getWeatherData**
         - url: http://localhost:5000/api/getWeatherData/
         - method: GET
         - parameters: 
            - date: int (optional) | YYYY/api/weatherIngestion/MMD format
            - weather_station_id: str (optional) | 'USC00111280'
            - page_no: int (optional) | 1

   3. **getWeatherStats**
         - url: http://localhost:5000/api/getWeatherStats/
         - method: GET
         - parameters: 
            - year: int (optional) | YYYY format
            - weather_station_id: str (optional) | 'USC00111280'

      



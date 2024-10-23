# Real-Time Data Processing System for Weather Monitoring

## Project Overview

This project implements a real-time data processing system to monitor weather conditions using data from the OpenWeatherMap API. It aggregates and summarizes weather data, allowing for effective monitoring and alerting based on user-defined thresholds.

## Installation Instructions

### Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerized deployment)

### Setup Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourhandle/weather-monitoring-system.git
    cd weather-monitoring-system
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set your OpenWeatherMap API key:**
   - Sign up at [OpenWeatherMap](https://openweathermap.org/) and obtain an API key.
   - Create a `.env` file in the root directory and add your API key:
     ```
     OPENWEATHERMAP_API_KEY=your_api_key_here
     ```

5. **Run the application:**
    ```bash
    python src/weather_monitor.py
    ```

6. **Alternatively, run the application using Docker:**
    ```bash
    docker-compose up
    ```

## API Endpoints

- **`GET /weather/update`**
  - **Description:** Retrieve and process the latest weather data from the API.
  - **Output:** Returns processed weather data including temperature and condition.

- **`GET /weather/summary`**
  - **Description:** Get daily weather summary for a specified date.
  - **Output:**
    ```json
    {
      "date": "YYYY-MM-DD",
      "average_temperature": 25,
      "max_temperature": 30,
      "min_temperature": 20,
      "dominant_condition": "Clear"
    }
    ```

- **`POST /alerts`**
  - **Input:**
    ```json
    {
      "threshold": {
        "temperature": 35,
        "condition": "Rain"
      }
    }
    ```
  - **Description:** Define user-configurable thresholds for weather alerts.
  - **Output:**
    ```json
    {
      "message": "Alert thresholds set successfully."
    }
    ```

## Processing and Analysis

- The system continuously calls the OpenWeatherMap API at a configurable interval (default: every 5 minutes) to retrieve weather data for major Indian metros (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
- For each weather update, temperature values are converted from Kelvin to Celsius (or Fahrenheit based on user preference).

## Rollups and Aggregates

1. **Daily Weather Summary:**
   - The system rolls up weather data daily, calculating aggregates for:
     - Average temperature
     - Maximum temperature
     - Minimum temperature
     - Dominant weather condition (based on frequency).
   - Daily summaries are stored in a database for further analysis.

2. **Alerting Thresholds:**
   - Users can set configurable thresholds for temperature or specific weather conditions.
   - The system tracks the latest weather data, triggering alerts if thresholds are breached (console output or email notifications).

3. **Visualizations:**
   - Implement visualizations to display daily summaries, historical trends, and triggered alerts using libraries like Matplotlib or Plotly.

## Testing

### Test Cases

1. **System Setup:**
   - Verify that the system starts successfully and connects to the OpenWeatherMap API with a valid API key.

2. **Data Retrieval:**
   - Simulate API calls at configurable intervals and ensure weather data is retrieved correctly.

3. **Temperature Conversion:**
   - Test conversion of temperature values from Kelvin to Celsius (or Fahrenheit).

4. **Daily Weather Summary:**
   - Simulate weather updates over several days and verify that daily summaries are calculated correctly.

5. **Alerting Thresholds:**
   - Define thresholds and simulate weather data to ensure alerts are triggered as expected.

### Running Tests

To run the tests, execute the following command:

```bash
python -m unittest src/tests.py
```

## Docker Setup
To run the application using Docker:

Build and run the containers:

docker-compose up
Access the API on http://localhost:5000

The Docker setup includes:

Flask API running in a web container.
MongoDB for storing daily weather summaries and user-defined thresholds (optional).

## Conclusion
This project provides a comprehensive solution for real-time weather monitoring, aggregation, and alerting. With the ability to define user-configurable thresholds and view historical data, it serves as an effective tool for monitoring weather conditions in real-time. The application is designed for easy deployment using Docker and includes robust error handling and testing coverage.

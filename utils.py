def convert_to_celsius(kelvin):
    return kelvin - 273.15

def calculate_aggregates(data, temp):
    # Sample implementation to calculate aggregates
    return {
        'date': data['dt'],  # Replace with actual date calculation
        'avg_temp': temp,
        'max_temp': max(temp, data['main']['temp_max']),
        'min_temp': min(temp, data['main']['temp_min']),
        'dominant_condition': data['weather'][0]['main']
    }

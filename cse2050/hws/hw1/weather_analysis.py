
def read_weather_data(file_path: str):
    '''
    Description: Reads weather data from the provided text file and returns it as a list of tuples.
    Parameters: file_path (str): The path to the weather data file. 
    Returns:List[Tuple(str, float, float)]: A list of tuples where each tuple contains the date(str), temperature (float), and rainfall (float).
    '''
    # generate a empty list
    weather_data = []
    # open weather data file and return as list of tuples
    with open(file_path,"r") as open_file:
        for line in open_file:
            line = line.strip()
            date, temp, rainfall = line.split(',')
            weather_data.append((str(date), float(temp), float(rainfall)))
    return weather_data

    
def calculate_average_temperature(weather_data):
    '''
    Description: Calculates and returns the average temperature.
    Parameters: data (List[Tuple(str, float, float)]): The weather data.
    Returns: float: The average temperature.
    '''
    total_temp = 0.0
    # read weather data and sum the temperature
    for date, temp, rainfall in weather_data:
        total_temp += temp
    # devide total temperature with number of data
    avg_temp = total_temp / len(weather_data)
    return float(avg_temp)

    
def calculate_total_rainfall(weather_data):
    '''
    Description: Calculates and returns the total rainfall.
    Parameters: data (List[Tuple(str, float, float)]): The weather data.
    Returns: float: The total rainfall.
    '''
    total_rainfall = 0.0
    # read weather data and sum the rainfall
    for date, temp, rainfall in weather_data:
        total_rainfall += rainfall
    return float(total_rainfall)

    
def find_highest_temperature(weather_data):
    '''
    Description: Finds the highest temperature and its date.
    Parameters:data (List[Tuple(str, float, float)]): The weather data.
    Returns:Tuple[str, float]: A tuple containing the date and temperature.
    '''
    # creat a list within all temperature
    temp_list = [temp for date, temp, rainfall in weather_data]
    # find max temperature
    max_temp = max(temp_list)
    # find index of that max temperature
    max_index = temp_list.index(max_temp)
    date, temp, rainfall = weather_data[max_index]
    return (str(date), float(temp))

    
def find_lowest_temperature(weather_data):
    '''
    # Description: Finds the lowest temperature and its date.
    # Parameters: data (List[Tuple(str, float, float)]): The weather data.
    # Returns: Tuple[str, float]: A tuple containing the date and temperature.
    '''
    # creat a list within all temperature
    temp_list = [temp for date, temp, rainfall in weather_data]
    # find min temperature
    min_temp = min(temp_list)
    # find index of that min temperature
    min_index = temp_list.index(min_temp)
    date, temp, rainfall = weather_data[min_index]
    return (str(date), float(temp))

    
def find_day_with_most_rainfall(weather_data):
    '''
    Description: Finds the day with the most rainfall and its value.
    Parameters: data (List[Tuple(str, float, float)]): The weather data.
    Returns: Tuple[str, float]: A tuple containing the date and rainfall.
    '''

    rain_list = [rainfall for date, temp, rainfall in weather_data]
    most_rain = max(rain_list)
    max_index = rain_list.index(most_rain)
    date, temp, rainfall = weather_data[max_index]
    return (str(date), float(rainfall))


# main.py
import weather_analysis

def weather_analyze(file_path:str):
    '''
    Description: Analyzes the weather data and returns a dictionary with statistical insights. 
    Parameters: file_path (str): The path to the weather data file. 
    Returns: dict: A dictionary containing the calculated statistics.
    '''
    weather_data = weather_analysis.read_weather_data(file_path)
    output_dict = {
        "average_temperature": weather_analysis.calculate_average_temperature(weather_data),
        "total_rainfall": weather_analysis.calculate_total_rainfall(weather_data),
        "highest_temperature": {"date": weather_analysis.find_highest_temperature(weather_data)[0],
                                "temperature": weather_analysis.find_highest_temperature(weather_data)[1]
                                },
        "lowest_temperature": {"date": weather_analysis.find_lowest_temperature(weather_data)[0],
                                "temperature": weather_analysis.find_lowest_temperature(weather_data)[1]
                                },
        "most_rainfall": {"date": weather_analysis.find_day_with_most_rainfall(weather_data)[0],
                          "temperature": weather_analysis.find_day_with_most_rainfall(weather_data)[1]
                            }

    }
    return output_dict



    


if __name__ == "__main__":

    results = weather_analyze("weather_data.txt") #or the path to the file
    print(results)
 

    
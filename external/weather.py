import requests


class Weather():
    """
    Creates Weather object containing information about Current weather
    """

    def __init__(self, area, appid):
        self.area = area
        self.weather_url = "http://api.openweathermap.org/"
        self.appid = appid

    def weather_condition(self):
        """
        returns current weather condition
        """
        weather_api = "{}data/2.5/weather?q={}&units=metric&APPID={}".format(
                                    self.weather_url, self.area, self.appid)

        r = requests.get(weather_api)

        weather_dict = r.json()
        current = weather_dict['main']['temp']
        conditions = weather_dict['weather'][0]['description']
        current = round(current)
        weather = {
                "area": self.area,
                "conditions": conditions,
                "temperature": current
                }
        return weather

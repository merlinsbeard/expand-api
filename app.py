from apistar import App, Include, Route, schema
from apistar.docs import docs_routes
from apistar.statics import static_routes

from external.gw2 import GW2
from external.weather import Weather


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

def gw2_raid(key):
    """
    Returns a Response of boss kills
    """
    payload = GW2(key)
    payload = payload.get_raid_kills()
    return payload

def gw2_daily_fracs(key):
    """
    Returns a response of current t4 fractal dailies
    """
    payload = GW2(key)
    payload = payload.get_t4_daily()
    return payload


# Schemas here

# Hook

class Profile(schema.Object):
    properties = {
            'name': schema.String(max_length=100),
            'age': schema.Integer(minimum=1)
            }


def create_profile(profile: Profile):
    return profile

def weather(area):
    """
    Wrapper for weather API

    Response:

    ```
    {
        "area": "manila",
        "conditions": "scattered clouds",
        "temperature": 31
    }

    """
    appid = os.getenv("WEATHER_APP_ID","5be49f19e5f9f928228c830fb67cf008")
    w = Weather(area, appid)
    return w.weather_condition()


routes = [
    # gw2/
    Route('/gw2/raid', 'POST', gw2_raid),
    Route('/gw2/t4', 'POST', gw2_daily_fracs),
    # profile/
    Route('/profile', 'POST', create_profile),
    # weather/
    Route('/weather', 'GET', weather),

    # Default
    Route('/', 'GET', welcome),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]

app = App(routes=routes)

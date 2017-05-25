from apistar import App, Include, Route, schema
from apistar.docs import docs_routes
from apistar.statics import static_routes

from external.gw2 import GW2


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

routes = [
    # gw2/
    Route('/gw2/raid', 'POST', gw2_raid),
    Route('/gw2/t4', 'POST', gw2_daily_fracs),
    # profile/
    Route('/profile', 'POST', create_profile),

    # Default
    Route('/', 'GET', welcome),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]

app = App(routes=routes)

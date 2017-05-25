from apistar import App, Include, Route
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

routes = [
    Route('/gw2/raid', 'POST', gw2_raid),
    Route('/gw2/t4', 'POST', gw2_daily_fracs),
    Route('/', 'GET', welcome),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]

app = App(routes=routes)

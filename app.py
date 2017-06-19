from apistar import App, Include, Route, schema
from apistar.docs import docs_routes
from apistar.statics import static_routes
from apistar.http import Response

from external.gw2 import GW2
from external.weather import Weather
from external.rh import HubGet
from external.reddit import Reddit
from external.partner import Partner
from external.kubelogs import KubeLog

from envparse import env
env.read_envfile("prod.env")


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

def gw2_raid():
    """
    Returns a Response of boss kills
    """
    key = env("GW2_KEY")
    payload = GW2(key)
    payload = payload.get_raid_kills()
    return payload

def gw2_daily_fracs():
    """
    Returns a response of current t4 fractal dailies
    """
    key = env("GW2_KEY")
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
    appid = env("WEATHER_APP_ID")
    w = Weather(area, appid)
    return w.weather_condition()


def hub_get(
        partner_id: schema.String,
        source_reference_number,
        key):
    """
    Get a remittance transaction
    """

    h = HubGet(partner_id=partner_id,
            source_reference_number=source_reference_number,
            authorization=key)
    return h.get_remittance()


class KafkaConsumer(schema.Object):
    properties = {
            'url': schema.String(max_length=100),
            'topics': schema.String(max_length=100)
            }

def kafka_consumer(kafka: KafkaConsumer):
    pass


def reddit_comment(comment_id):
    '''
    Returns a response of writing prompts
    comment with details
    '''
    reddit_secret = env('REDDIT_SECRET')
    reddit_id = env('REDDIT_ID')
    reddit_username = env('REDDIT_USERNAME')
    reddit_password = env('REDDIT_PASSWORD')
    r = Reddit(reddit_secret, reddit_id,
               reddit_username, reddit_password)
    comment = r.get_comment_body(comment_id)
    return comment

def partner(partner_id):
    p = Partner(partner_id=partner_id)
    data = p.get_partners_one()
    return data

def branch(token) -> Response:
    branch_url = env("BRANCH_URL")
    p = Partner(token=token, branch_url=branch_url)
    data = p.get_branches()
    return Response(data=data)

def branch_one(token, branch_code) -> Response:
    branch_url = env("BRANCH_URL")
    p = Partner(token=token, branch_url=branch_url)
    data = p.get_branches_one(branch_code)
    return Response(data=data)

def kubename(service, namespace):
    token = env("GIST_TOKEN")
    kubelogs = KubeLog(service=service, namespace=namespace, token=token)
    names = kubelogs.get_replicas()
    return names

def kubelog(service, namespace):
    token = env("GIST_TOKEN")
    kubelogs = KubeLog(service=service, namespace=namespace, token=token)
    names = kubelogs.get_replicas()
    logs_url = []
    for name in names:
        logs = kubelogs.get_replicas_logs(name)
        logs = kubelogs.post_in_gist(logs, name)
        logs_url.append(logs['html_url'])
    return logs_url


routes = [
    # gw2/
    Route('/gw2/raid', 'GET', gw2_raid),
    Route('/gw2/t4', 'GET', gw2_daily_fracs),
    # profile/
    Route('/profile', 'POST', create_profile),
    # weather/
    Route('/weather', 'GET', weather),
    # hub
    Route('/hub/get','POST',hub_get),
    # Reddit
    Route('/reddit/comment','GET', reddit_comment),
    # hub
    Route('/hub/get','POST',hub_get),
    # Partner
    Route('/partner/{partner_id}', 'GET', partner),
    Route('/branch/{token}', 'GET', branch),
    Route('/branch/{token}/{branch_code}', 'GET', branch_one),
    # KubeLogs
    Route('/kube/replicas', 'GET', kubename),
    Route('/kube/logs', 'POST', kubelog),
    # Default
    Route('/', 'GET', welcome),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]

app = App(routes=routes)

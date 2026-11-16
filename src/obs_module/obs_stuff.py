import obswebsocket as obs_client
import requests
from dotenv import load_dotenv
import os


def obs_time():
    load_dotenv()
    obs_password = os.getenv("OBS_PASSWORD")
    obs_port = int(os.getenv("OBS_PORT"))
    obs_host = os.getenv("OBS_HOST")
    return (obs_host, obs_password, obs_port)

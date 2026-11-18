import obswebsocket as obs_client
from obswebsocket import obsws, requests
from dotenv import load_dotenv
import os
from obs_module import obs_controls


def obs_time():
    load_dotenv()
    obs_password = os.getenv("OBS_PASSWORD")
    obs_port = int(os.getenv("OBS_PORT"))
    obs_host = os.getenv("OBS_HOST")
    return (obs_host, obs_port, obs_password)


def OBSscenes(obs_client):
    response_dict = obs_client.call(requests.GetSceneList())
    my_dict_data = response_dict.datain

    the_scenes = my_dict_data.get("scenes", [])
    for scene in the_scenes:
        print(f"{scene["sceneName"]}, {scene["sceneIndex"]}")
    return my_dict_data

import uvicorn
from obswebsocket import obsws, requests
from fastapi import FastAPI
from dotenv import load_dotenv
import os

import obs_module

load_dotenv()
my_host = os.getenv("my_HOST")
my_port = int(os.getenv("my_API_PORT"))
obs_data_tuple = obs_module.obs_time()

obs_client = obsws(*obs_data_tuple)

nodary_main = FastAPI()


@nodary_main.post("/{incoming_integer}")
def catch_number(incoming_integer: int):

    if incoming_integer in obs_module.OBS_CONTROL_DICT.keys():
        the_action = obs_module.OBS_CONTROL_DICT[incoming_integer]

        if callable(the_action):
            return the_action(obs_client)
        obs_client.call(the_action)

    else:
        print("Invalid Input")


uvicorn.run(nodary_main, host=my_host, port=my_port)

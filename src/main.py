import uvicorn
from obswebsocket import obsws, requests
from fastapi import FastAPI

import obs_module

obs_client = obsws("127.0.0.1", 4454, "qfewbHU51sMudQNx")
obs_client.connect()

nodary_main = FastAPI()


@nodary_main.post("/{incoming_integer}")
def catch_number(incoming_integer: int):

    if incoming_integer in obs_module.OBS_CONTROL_DICT.keys():
        obs_client.call(obs_module.OBS_CONTROL_DICT[incoming_integer])

    else:
        print("Not gonna work bud")


# Place module content here:
obs_tuple = obs_module.obs_time()

uvicorn.run(nodary_main, host=obs_tuple[0], port=obs_tuple[2])

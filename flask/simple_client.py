#!/usr/bin/env python3 

import requests
import logging
import http.client
import json

def httpLogger():
    http.client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

def apiWatch(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        results = response.json()
        return results
    except requests.exceptions.HTTPError as errh:
        raise SystemExit(errh)
    except requests.exceptions.ConnectionError as errc:
        raise SystemExit(errc)
    except requests.exceptions.Timeout as errt:
        raise SystemExit(errt)
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)

def triggerSim(sim_config):
    for setup in sim_config:
        if setup["setup_id"]:
            return setup["setup_id"]
        else:
            raise Exception("setup_id not provided")

def sim(setup_id):
    print("Simulation started...", setup_id)
    new_sim = {"current_simulated_data": "9.78"}
    return new_sim

def updateServer(api_url, sim_data):
    print("Pushing updates to sever...", sim_data)
    #response = requests.patch(api_url, json=sim_data)
    #response.json()

if __name__ == '__main__':
    enable_logger = httpLogger()
    api_url = "http://127.0.0.1:5000/simulation_config"
    get_sim_config = apiWatch(api_url)
    sim_input = triggerSim(get_sim_config)
    sim_results = sim(sim_input)
    update_server = updateServer(api_url, sim_results) 

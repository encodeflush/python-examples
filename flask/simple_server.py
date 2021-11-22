#!/usr/bin/env python3

from flask import Flask, json

simulation_config = [{"setup_id": "c554590e-7f1e-4c1c-a0c8-c03075dbd729", "sim_input" : "3.14" ,"current_simulated_data": "9.16"}]

api = Flask(__name__)

@api.route('/simulation_config', methods=['GET'])
def get_data():
  return json.dumps(simulation_config)

if __name__ == '__main__':
    api.run() 

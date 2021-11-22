import logging

a = 6
b = 0

try:
  c = a / b
except Exception as e:
  logging.exception("Exception accured")
  

import sys
import logging
from flask import Flask
from helpers.middleware import setup_metrics

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)-15s %(name)s - %(levelname)s - %(message)s")

app = Flask(__name__)
#Inicializar las metricas
setup_metrics(app)

@app.route('/')
def testing():
  logging.info("This endpoint has been hit!")
  return "Si corre en mi maquina pinche container.jpg!"

if __name__ == '__main__':
    app.run(host="0.0.0.0")



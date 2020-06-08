import sys
import logging
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from healthcheck import HealthCheck, EnvironmentDump

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)-15s %(name)s - %(levelname)s - %(message)s")

app = Flask(__name__)
# Prometheus metrics.
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.3')
# Health, readiness, liveness.
health = HealthCheck()
envdump = EnvironmentDump()

def some_db_available():
  # Check connection to druid, kafka, spark is ok.
  return True, "OK"

health.add_check(some_db_available)

app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())

@app.route('/')
@metrics.counter('hits_endpoint_hello', 'Hits in the endpoint.',
         labels={'endpoint': "hello"})
def hello():
  logging.info("This endpoint has been hit!")
  return "Hello Rodrigo!"

if __name__ == '__main__':
    app.run(host="0.0.0.0")


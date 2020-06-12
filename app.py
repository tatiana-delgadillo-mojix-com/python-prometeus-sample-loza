import sys
import logging
from flask import Flask



LOG_FILENAME = 'aplication.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
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
         labels={'endpoint': "Load_df"})
def Load_df():
  try:
    logging.info("Dataframe successfuly loaded!")
    return "Working..."
  except ValueError:
    print("Can't find a sensible root for value.")
    return "Not worwking..."

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
        DEBUG = os.environ.get('DEBUG','True') == "True"
    except ValueError:
        DEBUG = True
        PORT = 5000
    app.logger.info("Starting Service")
    print (HOST,PORT)
    app.run(host=HOST,port=PORT,debug=DEBUG)


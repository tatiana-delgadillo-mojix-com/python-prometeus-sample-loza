from flask import request
from prometheus_flask_exporter import PrometheusMetrics
from healthcheck import HealthCheck, EnvironmentDump
import time
import sys

#Configurar metricas
def setup_metrics(app):
    metrics = PrometheusMetrics(app, group_by='endpoint')
    metrics.info('app_info', 'Application info', version='1.0.3')
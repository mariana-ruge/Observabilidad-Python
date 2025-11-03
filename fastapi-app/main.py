#Importar librerias
import logging
import time
from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración de OpenTelemetry
#Consumo de servicios
resource = Resource(attributes={"service.name": "fastapi-service"})
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://alloy:4318/v1/traces"))

#Llamar a los objetos
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)


#Construir la app con FastAPI
app = FastAPI()


#Buscar el endpoint de la API
@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"Hello": "World"}

#Esperar respuestas de las API
@app.get("/slow")
def slow_endpoint():
    logger.info("Slow endpoint called")
    time.sleep(2)
    #Retornar el estado del endpoint
    return {"status": "slow request completed"}

# Instrumentar FastAPI con OpenTelemetry
FastAPIInstrumentor.instrument_app(app)
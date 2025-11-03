import logging
import time
from fastapi import FastAPI

# Prometheus
from prometheus_fastapi_instrumentator import Instrumentator

# OpenTelemetry
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


# Crear la app
app = FastAPI()

# Configurar logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app-logs")

# Configurar OpenTelemetry Trace → Alloy → Tempo
resource = Resource(attributes={"service.name": "fastapi-service"})
provider = TracerProvider(resource=resource)
span_exporter = OTLPSpanExporter(endpoint="http://alloy:4318/v1/traces")
provider.add_span_processor(BatchSpanProcessor(span_exporter))
trace.set_tracer_provider(provider)

# Instrumentación de FastAPI (Tracing automático)
FastAPIInstrumentor.instrument_app(app)

# Métricas Prometheus
@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)


# ---------------- Rutas de prueba ---------------- #

@app.get("/")
def root():
    logger.info("Root endpoint called ✅")
    return {"message": "Observabilidad funcionando 🚀"}


@app.get("/slow")
def slow():
    logger.warning("Slow endpoint processing... ⏳")
    time.sleep(2)
    return {"status": "Slow request completed ✅"}

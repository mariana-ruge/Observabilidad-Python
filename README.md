# Dashboard de métricas con Prometeus y Grafana
Este proyecto es un mockup de un dashboard de datos de tráfico de un página web estáticos, realizado para recolectar los datos y procesarlos posteriormente con Grafana en busca de alarmas e insights.

El proyecto esta construido con Prometeus, Grafana, Python, fast-api, alloy y Loki.

Los datos se analizan y se recopilan por medio de FastAPI, y en este caso el tráfico se simula con Python.
- Grafana permite modificar alertas, queries entre otras cosas.
- Muestra la actividad del sistema en tiempo real (aunque en este caso es con datos estaticos)

Puedes acceder o ver el despliegue de la app, en su primera versión por medio de docker.
[https://hub.docker.com/r/marianaruge/fastapi-app/tags](https://hub.docker.com/r/marianaruge/fastapi-app/tags)
# 1. Imagen base
FROM python:3.12-slim

# 2. Establecer directorio de trabajo
WORKDIR /app

# 3. Copiar requirements y instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el resto del código
COPY . .

# 5. Exponer el puerto que usarás dentro del contenedor
EXPOSE 8000

# 6. Comando para correr FastAPI con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

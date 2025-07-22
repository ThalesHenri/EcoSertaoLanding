# Dockerfile
FROM python:3.11-slim


# Expõe a porta
EXPOSE 8080

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    && apt-get clean


# Instala dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia todo o projeto




COPY . .
# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

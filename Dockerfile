FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.in /app/
RUN pip install pip-tools
RUN pip-compile requirements.in -o requirements.txt
RUN pip install -r requirements.txt
COPY . /app/

ENTRYPOINT [ "./docker_startup.sh" ]
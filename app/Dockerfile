FROM python:3.10-slim-buster

RUN pip install explainerdashboard
RUN pip install dill

COPY dashboard.py ./
COPY app.py ./
COPY processed_abalon.csv ./

RUN python dashboard.py

EXPOSE 9050
CMD ["python", "./app.py"]
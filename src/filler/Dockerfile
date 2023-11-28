FROM python:3.9-slim
WORKDIR src
RUN pip3 install mysql-connector-python python-dotenv --no-cache-dir
COPY DBManager.py .
WORKDIR filler
COPY filler/filler.py .
WORKDIR /src
CMD ["python3", "/src/filler/filler.py"]

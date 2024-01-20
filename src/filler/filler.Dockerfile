FROM python:3.9-slim
WORKDIR src
COPY filler/requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
EXPOSE 8000
COPY DBManager.py .
WORKDIR filler
COPY filler/filler.py .
WORKDIR /src
CMD ["python3", "/src/filler/filler.py"]

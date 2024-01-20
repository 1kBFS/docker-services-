FROM python:3.9-slim
WORKDIR /src
COPY web/requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY DBManager.py .
WORKDIR web
COPY web/web.py .
WORKDIR /src
CMD ["python3", "/src/web/web.py"]
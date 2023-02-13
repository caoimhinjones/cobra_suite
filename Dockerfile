FROM python:latest

ADD . .
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python","src/main.py"]
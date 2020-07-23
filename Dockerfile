FROM python:3.8
WORKDIR /app

RUN python3.8 -m pip install --no-cache-dir --upgrade pip gunicorn

COPY ./requirements.txt ./requirements.txt
RUN python3.8 -m pip install --no-cache-dir -r requirements.txt

COPY ./resources ./resources

CMD ["gunicorn", "--bind=0.0.0.0:80", "resources:app"]
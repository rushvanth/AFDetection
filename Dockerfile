FROM python:latest
WORKDIR /afdetection
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir
CMD [ "python", "src/main.py" ]
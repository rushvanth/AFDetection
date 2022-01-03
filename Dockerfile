FROM python:latest
RUN pip install --upgrade pip
WORKDIR /afdetection
COPY . .
RUN ls -la
RUN pip install -r requirements.txt
CMD [ "python", "src/main.py" ]
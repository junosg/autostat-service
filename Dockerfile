FROM python:3.9.10-alpine3.14
WORKDIR /src
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask-cors
RUN pip install scipy
RUN pip install numpy
RUN pip install pandas

COPY . /src
ENV FLASK_APP=app
CMD ["python","app.py"]
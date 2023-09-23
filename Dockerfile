FROM python:3.10-alpine3.17
WORKDIR /src
RUN pip install Cython
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask-cors
RUN pip install scipy
RUN pip install numpy
RUN pip install pandas
RUN pip install --upgrade patsy
RUN pip install -U statsmodels
RUN pip install scikit-posthocs

COPY . /src
ENV FLASK_APP=app
CMD ["python","app.py"]
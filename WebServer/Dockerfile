FROM python:slim
WORKDIR /WebServer
ADD . /WebServer
RUN pip install --trusted-host pypi.python.org pymongo
EXPOSE 8181
CMD ["python", "-u", "app.py"]
From python:3.7.5-slim
RUN pip install flask==1.1.1 redis==3.3.8
WORKDIR /src
COPY ./src/server.py /src/
ENV REDIS_HOST=localhost
ENTRYPOINT ["python", "-u", "server.py"]

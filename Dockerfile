#FROM hemanhp/djbase:4.2.4
FROM python:3.13-alpine3.20

ENV PYTHONUNBUFFERED=1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip
RUN apk add --update --no-cache postgresql-client
RUN apk add --update  postgresql-client build-base postgresql-dev musl-dev linux-headers libffi-dev libxslt-dev libxml2-dev
RUN    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers libffi-dev libjpeg zlib-dev jpeg-dev gcc musl-dev libxslt libxml2




COPY ./requirements /requirements
COPY ./scripts /scripts
COPY ./src /src

WORKDIR src

EXPOSE 8000
#EXPOSE 8086:8086
#ENV http_proxy=http://127.0.0.1:8086
#ENV HTTP_PROXY=http://127.0.0.1:8086
#ENV https_proxy=http://127.0.0.1:8086
#ENV HTTPS_PROXY=http://127.0.0.1:8086
#ENV ftp_proxy=http://127.0.0.1:8086


RUN /py/bin/pip install -r /requirements/development.txt

# RUN apk add  geos gdal


RUN chmod -R +x /scripts && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home djshop && \
    chown -R djshop:djshop /vol && \
    chmod -R 755 /vol


ENV PATH="/scripts:/py/bin:$PATH"

USER djshop

CMD ["run.sh"]
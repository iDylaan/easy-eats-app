FROM alpine:3.14

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN apk add --update --no-cache \
    python3=3.11.0-r0 \
    py3-pip=22.3.1-r0 \
    && python3 --version | grep -q "Python 3.11.0" \
    && pip3 --version | grep -q "pip 22.3.1"
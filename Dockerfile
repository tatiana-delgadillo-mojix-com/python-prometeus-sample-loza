FROM python:3.7-slim

ENV HOME_APP=/opt/ytem/ \
    PYTHONBUFFERED=1

WORKDIR "${HOME_APP}"

COPY app.py "${HOME_APP}"
COPY requirements.txt /
COPY run.sh /

RUN pip3 install -r /requirements.txt

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "-c"]
CMD ["/run.sh"]


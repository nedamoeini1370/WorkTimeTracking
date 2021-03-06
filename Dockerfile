# Builds a docer image based on gunicorn for Django app
FROM python:3.9


# Copy project files
COPY ./requirements.txt  /requirements.txt

# install required packages via PIP
RUN --mount=type=cache,target=/root/.cache \
    pip install -r /requirements.txt

# Copy project files
COPY ./entrypoint.sh /
ADD  src/ /opt/src/

# Set a work dir
WORKDIR /opt/src/
ENV PYTHONUNBUFFERED=1

HEALTHCHECK CMD curl --fail http://localhost:8002 || exit 1 --health-interval=5s --timeout=3s

# Tell the docker which cmd to run when using this image
ENTRYPOINT ["sh", "/entrypoint.sh"]
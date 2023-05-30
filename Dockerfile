FROM python:latest
LABEL maintainer="@JManzur - https://jmanzur.com"

WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

RUN groupadd -r nonroot && useradd -r -g nonroot nonroot
USER nonroot

EXPOSE 8889

CMD ["python", "/usr/src/app/app.py"]
FROM python:latest
LABEL maintainer="@JManzur - https://jmanzur.com"

# Copy the application source code and install dependencies:
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
# RUN mkdir logs && chmod 777 logs

# Fix security issue:
RUN apt-get update && apt-get upgrade -y && apt-get install -y openssl
RUN groupadd -r nonroot && useradd -r -g nonroot nonroot
RUN chown -R nonroot:nonroot /usr/src/app
USER nonroot

EXPOSE 8889

CMD ["python", "/usr/src/app/app.py"]
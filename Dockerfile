FROM python:latest
LABEL maintainer="@JManzur - https://jmanzur.com"

# Update and security fix:
RUN apt-get update && apt-get upgrade -y && apt-get install -y openssl

# Copy the application source code and install dependencies:
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
RUN mkdir logs && chmod 777 logs

EXPOSE 8889

CMD ["python", "/usr/src/app/app.py"]
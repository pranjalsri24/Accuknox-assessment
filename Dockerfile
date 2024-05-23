FROM ubuntu:20.04
WORKDIR /app
RUN apt-get update && apt-get install -y \
    fortune \
    cowsay \
    netcat \
    && rm -rf /var/lib/apt/lists/*
COPY . .

RUN chmod +x wisecow.sh
EXPOSE 4499

CMD ["./wisecow.sh"]

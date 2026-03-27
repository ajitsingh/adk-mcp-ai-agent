FROM debian:bookworm-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl ca-certificates && rm -rf /var/lib/apt/lists/*

ENV VERSION=0.23.0
RUN curl -O https://storage.googleapis.com/genai-toolbox/v$VERSION/linux/amd64/toolbox && \
    chmod +x toolbox

COPY tools.yaml /app/tools.yaml

EXPOSE 5000

CMD ["/app/toolbox", "--tools-file", "/app/tools.yaml"]
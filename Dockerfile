FROM python:3.12-slim-bullseye AS builder
# FROM ubuntu:22.04 AS builder

RUN apt-get update && apt-get install -y binutils python3-pip

WORKDIR /app

COPY . .
RUN pip3 install --break-system-packages --no-cache-dir . pyinstaller

RUN apt-get update && apt-get install -y --no-install-recommends \
    libegl-dev \
    libosmesa6-dev \
    libx11-dev \
    libxrender-dev \
    libxcb1 \
    && rm -rf /var/lib/apt/lists/*
    

RUN pyinstaller \
    --onefile \
    --collect-data opengeodeweb_viewer \
    --collect-data vease_viewer \
    --collect-all vtkmodules src/vease_viewer/app.py \
    --distpath dist \
    --name vease-viewer \
    --clean

ENV PYTHON_ENV="prod"

# FROM debian:12-slim
FROM ubuntu:22.04

# Install ONLY the runtime libraries your binary actually needs
# (this list was tested with VTK + PyQt6 + OpenGEODE apps in 2025)
RUN apt-get update && apt-get install -y --no-install-recommends \
    # libosmesa6-dev \
    # libx11-dev \
    # libxrender-dev \
    libxcb1 \
    && rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/dist/vease-viewer /usr/local/bin/vease-viewer
RUN chmod +x /usr/local/bin/vease-viewer

EXPOSE 1234
ENV PYTHON_ENV=prod
ENV DISPLAY=:0

ENTRYPOINT ["/usr/local/bin/vease-viewer"]
CMD ["--data_folder_path", "/data"]



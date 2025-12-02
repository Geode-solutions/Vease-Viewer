FROM python:3.12-slim-bookworm AS builder

RUN apt-get update && apt-get install -y binutils

WORKDIR /app

COPY . .
RUN pip3 install --no-cache-dir . pyinstaller

RUN pyinstaller \
    --onefile \
    --collect-data opengeodeweb_viewer\
    --collect-data vease_viewer\
    --collect-all vtkmodules \
    src/vease_viewer/app.py \
    --distpath dist \
    --name vease-viewer \
    --clean
ENV PYTHON_ENV="prod"

FROM debian:12-slim

# Install ONLY the runtime libraries your binary actually needs
# (this list was tested with VTK + PyQt6 + OpenGEODE apps in 2025)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libfontconfig1 \
    libxrender1 \
    libxext6 \
    libx11-6 \
    libxcb1 \
    libxkbcommon0 \
    libxkbcommon-x11-0 \
    libxi6 \
    libxtst6 \
    libsm6 \
    libice6 \
    libgtk-3-0 \
    libgssapi-krb5-2 \
    libkrb5-3 \
    libk5crypto3 \
    libcom-err2 \
    libkeyutils1 \
    zlib1g \
    libqt5core5a \
    libqt5gui5 \
    libqt5widgets5 \
    libqt5network5 \
    libqt5dbus5 \
    libopencv-core4.* \
    libosmesa6-dev \
    libx11-dev \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/dist/vease-viewer /usr/local/bin/vease-viewer
RUN chmod +x /usr/local/bin/vease-viewer

EXPOSE 1234
ENV PYTHON_ENV=prod
ENV DISPLAY=:0

ENTRYPOINT ["/usr/local/bin/vease-viewer"]
CMD ["--data_folder_path", "/data"]

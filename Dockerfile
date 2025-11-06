FROM python:3.12-slim

WORKDIR /app

COPY . .
RUN apt-get update && apt-get install -y libx11-dev libxrender-dev
RUN pip3 install .
ENV PYTHON_ENV="prod"

CMD ["vease-viewer", "--data_folder_path", "/data"]

EXPOSE 1234
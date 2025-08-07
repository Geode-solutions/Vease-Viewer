FROM python:3.12-slim

WORKDIR /app

COPY . .
RUN pip3 install --extra-index-url https://wheels.vtk.org .[cpu]
ENV PYTHONPATH="/usr/local:$PYTHONPATH"
ENV PYTHON_ENV="prod"

CMD ["vease-viewer", "--data_folder_path", "/data"]

EXPOSE 1234
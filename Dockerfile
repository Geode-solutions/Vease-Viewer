FROM python:3.12-slim

WORKDIR /app

COPY . .
RUN pip3 install --user -r requirements.txt && pip3 cache purge
RUN pip3 install https://www.vtk.org/files/release/9.3/vtk_osmesa-9.3.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
RUN pip3 install .
ENV PYTHONPATH="/usr/local:$PYTHONPATH"
ENV PYTHON_ENV="prod"

CMD ["vease-viewer", "--data_folder_path", "/data"]

EXPOSE 1234
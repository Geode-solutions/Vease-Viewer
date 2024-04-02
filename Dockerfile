FROM python:3.9-slim

WORKDIR /app

COPY . .
RUN pip3 install --user -r requirements.txt && pip3 cache purge
RUN pip3 install https://www.vtk.org/files/release/9.3/vtk_osmesa-9.3.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
ENV PYTHONPATH="/usr/local:$PYTHONPATH"
ENV PYTHON_ENV="prod"

CMD python app.py

EXPOSE 1234
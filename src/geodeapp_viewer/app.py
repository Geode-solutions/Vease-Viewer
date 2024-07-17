# Standard library imports
import dotenv
import os

# Local application imports
from opengeodeweb_viewer import vtkw_server

basedir = os.path.abspath(os.path.dirname(__file__))
dot_env_path = os.path.join(basedir, "./.env")
if os.path.isfile(dot_env_path):
    dotenv.load_dotenv(dot_env_path)


def run_viewer():
    vtkw_server.run_server()

if __name__ == "__main__":
    run_viewer()

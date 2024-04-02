from opengeodeweb_viewer import vtkw_server
import os
import dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
dot_env_path = os.path.join(basedir, "./.env")
if os.path.isfile(dot_env_path):
    dotenv.load_dotenv(dot_env_path)

if __name__ == "__main__":
    vtkw_server.run_server()

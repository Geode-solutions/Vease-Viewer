# Standard library imports

# Third party imports
from opengeodeweb_viewer import vtkw_server

# Local application imports


def run_viewer():
    vtkw_server.run_server()

if __name__ == "__main__":
    run_viewer()

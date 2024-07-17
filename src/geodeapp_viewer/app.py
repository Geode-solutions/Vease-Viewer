# Standard library imports

# Third party imports

# Local application imports
from opengeodeweb_viewer import vtkw_server


def run_viewer():
    vtkw_server.run_server()

if __name__ == "__main__":
    run_viewer()

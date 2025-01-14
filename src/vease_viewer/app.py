# Standard library imports

# Third party imports
from opengeodeweb_viewer.vtkw_server import _Server, run_server

# Local application imports
from vease_viewer.rpc.protocols import VtkVeaseViewerView

def run_viewer():
    _Server.custom_protocols.append(VtkVeaseViewerView())
    run_server()

if __name__ == "__main__":
    run_viewer()

# Standard library imports

# Third party imports
from opengeodeweb_viewer.vtkw_server import _Server, run_server

# Local application imports
from vease_viewer.rpc.protocols import VtkVeaseViewerView

class VeaseViewerServer(_Server):
    def initialize(self):
        _Server.initialize(self)
        self.registerVtkWebProtocol(VtkVeaseViewerView())
        

def run_viewer():
    run_server(VeaseViewerServer)

if __name__ == "__main__":
    run_viewer()

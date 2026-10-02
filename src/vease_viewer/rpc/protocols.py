# Standard library imports
import importlib.metadata as metadata

# Third party imports
from opengeodeweb_viewer.typed_rpc import typed_rpc
from vtkmodules.web import protocols as vtk_protocols

# Local application imports
from . import schemas


class VtkVeaseViewerView(vtk_protocols.vtkWebProtocol):
    prefix = "vease_viewer."

    def __init__(self) -> None:
        super().__init__()

    @typed_rpc(prefix, schemas.microservice_version_route)
    def microservice_version(
        self, params: schemas.MicroserviceVersion
    ) -> schemas.MicroserviceVersionResponse:
        return schemas.MicroserviceVersionResponse(
            microservice_version=metadata.distribution("vease_viewer").version
        )

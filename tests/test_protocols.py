# Standard library imports
import importlib.metadata as metadata

# Local application imports
from opengeodeweb_viewer.typed_rpc import TYPED_RPC_MARKER
from vease_viewer.rpc.protocols import VtkVeaseViewerView


def test_microservice_version_is_typed() -> None:
    assert getattr(VtkVeaseViewerView.microservice_version, TYPED_RPC_MARKER, False)


def test_microservice_version() -> None:
    assert VtkVeaseViewerView().microservice_version({}) == {
        "microservice_version": metadata.distribution("vease_viewer").version
    }

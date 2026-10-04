from opengeodeweb_microservice.schemas import Route, load_schema
from dataclasses_json import DataClassJsonMixin
from opengeodeweb_microservice.schemas import print_dataclass
from dataclasses import dataclass


@dataclass
class MicroserviceVersion(DataClassJsonMixin):
    def __post_init__(self) -> None:
        print_dataclass(self)

    pass


@dataclass
class MicroserviceVersionResponse(DataClassJsonMixin):
    def __post_init__(self) -> None:
        print_dataclass(self)

    microservice_version: str


microservice_version_route = Route(
    schema=load_schema(__file__),
    params=MicroserviceVersion,
    response=MicroserviceVersionResponse,
)

__all__ = ["MicroserviceVersion", "MicroserviceVersionResponse", "microservice_version_route"]

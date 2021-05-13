# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    Name: Optional[str]
    MinimumPasswordLength: Optional[int]
    RequireSymbols: Optional[bool]
    RequireNumbers: Optional[bool]
    RequireUppercaseCharacters: Optional[bool]
    RequireLowercaseCharacters: Optional[bool]
    AllowUsersToChangePassword: Optional[bool]
    MaxPasswordAge: Optional[int]
    PasswordReusePrevention: Optional[int]
    HardExpiry: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            MinimumPasswordLength=json_data.get("MinimumPasswordLength"),
            RequireSymbols=json_data.get("RequireSymbols"),
            RequireNumbers=json_data.get("RequireNumbers"),
            RequireUppercaseCharacters=json_data.get("RequireUppercaseCharacters"),
            RequireLowercaseCharacters=json_data.get("RequireLowercaseCharacters"),
            AllowUsersToChangePassword=json_data.get("AllowUsersToChangePassword"),
            MaxPasswordAge=json_data.get("MaxPasswordAge"),
            PasswordReusePrevention=json_data.get("PasswordReusePrevention"),
            HardExpiry=json_data.get("HardExpiry"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel



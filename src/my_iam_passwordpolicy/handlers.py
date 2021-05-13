import logging
from typing import Any, MutableMapping, Optional

from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
    exceptions,
    identifier_utils,
)

from .models import ResourceHandlerRequest, ResourceModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "MY::IAM::PasswordPolicy"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint

def _read_model(session):
    request = ResourceHandlerRequest
    model = request.previousResourceState
    if isinstance(session,SessionProxy):
        iam = session.client("iam")
        try:
           response = iam.get_account_password_policy()
           password_policy = response['PasswordPolicy']
           model.MinimumPasswordLength = password_policy['MinimumPasswordLength']
           model.RequireSymbols = password_policy['RequireSymbols']
           model.RequireNumbers = password_policy['RequireNumbers']
           model.RequireUppercaseCharacters = password_policy['RequireUppercaseCharacters']
           model.RequireLowercaseCharacters = password_policy['RequireLowercaseCharacters']
           model.AllowUsersToChangePassword = password_policy['AllowUsersToChangePassword']
           model.MaxPasswordAge =  password_policy['MaxPasswordAge']   
           model.PasswordReusePrevention = password_policy['PasswordReusePrevention']
           model.HardExpiry = password_policy['HardExpiry']
        except TypeError as e:
            # exceptions module lets CloudFormation know the type of failure that occurred
            raise exceptions.InternalFailure(f"was not expecting type {e}")
            # this can also be done by returning a failed progress event
            # return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"was not expecting type {e}")       
    return model            
   

@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    # TODO: put code here
    if isinstance(session,SessionProxy):
        iam = session.client("iam")
        try:
            kargs = dict(
                MinimumPasswordLength=model.MinimumPasswordLength,
                RequireSymbols=model.RequireSymbols,
                RequireNumbers=model.RequireNumbers,
                RequireUppercaseCharacters=model.RequireUppercaseCharacters,
                RequireLowercaseCharacters=model.RequireLowercaseCharacters,
                AllowUsersToChangePassword=model.AllowUsersToChangePassword,
                MaxPasswordAge=model.MaxPasswordAge,
                PasswordReusePrevention=model.PasswordReusePrevention,
                HardExpiry=model.HardExpiry,
            )

            iam.update_account_password_policy(**{k: v for k,v in kargs.items() if v is not None })
            model.Name = 'PassswordPolicy'
            progress.status = OperationStatus.SUCCESS
        except TypeError as e:
            # exceptions module lets CloudFormation know the type of failure that occurred
            raise exceptions.InternalFailure(f"was not expecting type {e}")
            # this can also be done by returning a failed progress event
            # return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"was not expecting type {e}")        

    return read_handler(session, request, callback_context)


@resource.handler(Action.UPDATE)
def update_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    # TODO: put code here
    if isinstance(session,SessionProxy):
        iam = session.client("iam")
        try:
            kargs = dict(
                MinimumPasswordLength=model.MinimumPasswordLength,
                RequireSymbols=model.RequireSymbols,
                RequireNumbers=model.RequireNumbers,
                RequireUppercaseCharacters=model.RequireUppercaseCharacters,
                RequireLowercaseCharacters=model.RequireLowercaseCharacters,
                AllowUsersToChangePassword=model.AllowUsersToChangePassword,
                MaxPasswordAge=model.MaxPasswordAge,
                PasswordReusePrevention=model.PasswordReusePrevention,
                HardExpiry=model.HardExpiry,
            )

            iam.update_account_password_policy(**{k: v for k,v in kargs.items() if v is not None })
            model.Name = 'PassswordPolicy'
            progress.status = OperationStatus.SUCCESS
        except TypeError as e:
            # exceptions module lets CloudFormation know the type of failure that occurred
            raise exceptions.InternalFailure(f"was not expecting type {e}")
            # this can also be done by returning a failed progress event
            # return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"was not expecting type {e}")   

    return read_handler(session, request, callback_context)


@resource.handler(Action.DELETE)
def delete_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    # TODO: put code here
    if isinstance(session,SessionProxy):
        iam = session.client("iam")
        try:
            iam.get_account_password_policy()
            iam.delete_account_password_policy()
            progress.status = OperationStatus.SUCCESS
        except iam.exceptions.NoSuchEntityException:
            raise exceptions.NotFound(type_name=TYPE_NAME, identifier="PasswordPolicy")
                
    return progress


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    # TODO: put code here
    if isinstance(session,SessionProxy):
        iam = session.client("iam")
        try:
           response = iam.get_account_password_policy()
           password_policy = response['PasswordPolicy']
           model.MinimumPasswordLength = password_policy['MinimumPasswordLength']
           model.RequireSymbols = password_policy['RequireSymbols']
           model.RequireNumbers = password_policy['RequireNumbers']
           model.RequireUppercaseCharacters = password_policy['RequireUppercaseCharacters']
           model.RequireLowercaseCharacters = password_policy['RequireLowercaseCharacters']
           model.AllowUsersToChangePassword = password_policy['AllowUsersToChangePassword']
           model.MaxPasswordAge =  password_policy['MaxPasswordAge']   
           model.PasswordReusePrevention = password_policy['PasswordReusePrevention']
           model.HardExpiry = password_policy['HardExpiry']
           # Setting Status to success will signal to cfn that the operation is complete
           progress.status = OperationStatus.SUCCESS
        except TypeError as e:
            # exceptions module lets CloudFormation know the type of failure that occurred
            raise exceptions.InternalFailure(f"was not expecting type {e}")
            # this can also be done by returning a failed progress event
            # return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"was not expecting type {e}")   

    return progress


@resource.handler(Action.LIST)
def list_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    # TODO: put code here 
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModels=[],
    )

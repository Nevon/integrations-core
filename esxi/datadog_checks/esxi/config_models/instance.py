# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class CollectPerInstanceFilters(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    host: Optional[tuple[str, ...]] = None
    vm: Optional[tuple[str, ...]] = None


class MetricFilters(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    host: Optional[tuple[str, ...]] = None
    vm: Optional[tuple[str, ...]] = None


class MetricPatterns(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[str, ...]] = None


class ResourceFilter(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    patterns: Optional[tuple[str, ...]] = None
    property: Optional[str] = None
    resource: Optional[str] = None
    type: Optional[str] = None


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    collect_per_instance_filters: Optional[CollectPerInstanceFilters] = None
    disable_generic_tags: Optional[bool] = None
    empty_default_hostname: bool
    excluded_host_tags: Optional[tuple[str, ...]] = None
    host: str
    metric_filters: Optional[MetricFilters] = None
    metric_patterns: Optional[MetricPatterns] = None
    min_collection_interval: Optional[float] = None
    password: str
    resource_filters: Optional[tuple[ResourceFilter, ...]] = None
    service: Optional[str] = None
    ssl_cafile: Optional[str] = None
    ssl_capath: Optional[str] = None
    ssl_verify: Optional[bool] = None
    tags: Optional[tuple[str, ...]] = None
    use_configured_hostname: Optional[bool] = None
    use_guest_hostname: Optional[bool] = None
    username: str

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @field_validator('*', mode='before')
    def _validate(cls, value, info):
        field = cls.model_fields[info.field_name]
        field_name = field.alias or info.field_name
        if field_name in info.context['configured_fields']:
            value = getattr(validators, f'instance_{info.field_name}', identity)(value, field=field)
        else:
            value = getattr(defaults, f'instance_{info.field_name}', lambda: value)()

        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_instance', identity)(model))

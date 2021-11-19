# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.base.checks.prometheus import GenericPrometheusCheck
from datadog_checks.base.utils.tracing import traced_class


@traced_class()
class PrometheusCheck(GenericPrometheusCheck):
    pass

# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.base import PDHBaseCheck
from datadog_checks.base.utils.tracing import traced_class

from .metrics import DEFAULT_COUNTERS


@traced_class()
class HypervCheck(PDHBaseCheck):
    def __init__(self, name, init_config, instances=None):
        super(HypervCheck, self).__init__(name, init_config, instances=instances, counter_list=DEFAULT_COUNTERS)

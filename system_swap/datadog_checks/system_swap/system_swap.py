# (C) Datadog, Inc. 2010-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

# 3p
import psutil

from datadog_checks.base import AgentCheck

# project
from datadog_checks.base.utils.tracing import traced_class


@traced_class()
class SystemSwap(AgentCheck):
    def check(self, instance):
        swap_mem = psutil.swap_memory()
        tags = instance.get('tags', [])
        self.rate('system.swap.swapped_in', swap_mem.sin, tags=tags)
        self.rate('system.swap.swapped_out', swap_mem.sout, tags=tags)

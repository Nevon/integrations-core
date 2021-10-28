# Agent Check: Aerospike

## Overview

Get metrics from Aerospike Database in real time to:

- Visualize and monitor Aerospike states.
- Be notified about Aerospike failovers and events.

## Setup

NOTE: The current aerospike integration is only compatible with Aerospike server v4.9 or above, see Aerospike's [Python Client Library Release Notes][1] for more info.
If you use an older Aerospike server version, it is still possible to monitor it with version 7.29.0 or lower of the Datadog Agent.

### Installation

The Aerospike check is included in the Datadog Agent package.
No additional installation is needed on your server.

### Configuration

<!-- xxx tabs xxx -->
<!-- xxx tab "Host" xxx -->

#### Host

##### Metric collection
To configure this check for an Agent running on a host:

1. Edit the `aerospike.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to start collecting your aerospike performance data. See the [sample aerospike.d/conf.yaml][2] for all available configuration options.

2. [Restart the Agent][3].

##### Log collection


1. Collecting logs is disabled by default in the Datadog Agent, you need to enable it in `datadog.yaml`:

   ```yaml
   logs_enabled: true
   ```

2. Add this configuration block to your `aerospike.d/conf.yaml` file to start collecting your Aerospike Logs:

   ```yaml
   logs:
     - type: file
       path: /var/log/aerospike/aerospike.log
       source: aerospike
   ```

    Change the `path` parameter value and configure them for your environment. See the [sample aerospike.d/conf.yaml][2] for all available configuration options.

3. [Restart the Agent][3].

<!-- xxz tab xxx -->
<!-- xxx tab "Containerized" xxx -->


#### Containerized

For containerized environments, see the [Autodiscovery Integration Templates][4] for guidance on applying the parameters below.

##### Metric collection

| Parameter            | Value                                |
| -------------------- | ------------------------------------ |
| `<INTEGRATION_NAME>` | `aerospike`                          |
| `<INIT_CONFIG>`      | blank or `{}`                        |
| `<INSTANCE_CONFIG>`  | `{"host":"%%host%%", "port":"3000"}` |

##### Log collection

_Available for Agent versions >6.0_

Collecting logs is disabled by default in the Datadog Agent. To enable it, see [Kubernetes log collection documentation][5].

| Parameter      | Value                                               |
| -------------- | --------------------------------------------------- |
| `<LOG_CONFIG>` | `{"source": "aerospike", "service": "<SERVICE_NAME>"}` |

<!-- xxz tab xxx -->
<!-- xxz tabs xxx -->

### Validation

[Run the Agent's status subcommand][6] and look for `aerospike` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][7] for a list of metrics provided by this integration.

### Service Checks

**aerospike.can_connect**
**aerospike.cluster_up**

### Events

Aerospike does not include any events.

## Troubleshooting

Need help? Contact [Datadog support][8].

[1]: https://download.aerospike.com/download/client/python/notes.html#5.0.0
[2]: https://github.com/DataDog/integrations-core/blob/master/aerospike/datadog_checks/aerospike/data/conf.yaml.example
[3]: https://docs.datadoghq.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[4]: https://docs.datadoghq.com/agent/kubernetes/integrations/
[5]: https://docs.datadoghq.com/agent/kubernetes/log/
[6]: https://docs.datadoghq.com/agent/guide/agent-commands/#agent-status-and-information
[7]: https://github.com/DataDog/integrations-core/blob/master/aerospike/metadata.csv
[8]: https://docs.datadoghq.com/help/
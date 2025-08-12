---
description: Offensive data enrichment pipeline
title: Nemesis
---

# Nemesis

Offensive data enrichment pipeline

<p align="center">
    <img src="docs/images/nemesis-light.png" alt="Nemesis" style="width: 800px;" />
</p>
<hr />

<p align="center">
<img src="https://img.shields.io/badge/version-2.0.0-blue" alt="version 2.0.0"/>
<a href="https://join.slack.com/t/bloodhoundhq/shared_invite/zt-1tgq6ojd2-ixpx5nz9Wjtbhc3i8AVAWw">
    <img src="https://img.shields.io/badge/Slack-%23nemesis—chat-blueviolet?logo=slack" alt="Slack"/>
</a>
<a href="https://twitter.com/tifkin_">
    <img src="https://img.shields.io/twitter/follow/tifkin_?style=social"
      alt="@tifkin_ on Twitter"/></a>
<a href="https://twitter.com/harmj0y">
    <img src="https://img.shields.io/twitter/follow/harmj0y?style=social"
      alt="@harmj0y on Twitter"/></a>
<a href="https://twitter.com/0xdab0">
    <img src="https://img.shields.io/twitter/follow/0xdab0?style=social"
      alt="@0xdab0 on Twitter"/></a>
<a href="https://github.com/specterops#nemesis">
    <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fspecterops%2F.github%2Fmain%2Fconfig%2Fshield.json&style=flat"
      alt="Sponsored by SpecterOps"/>
</a>
</p>
<hr />

# Overview

Nemesis is an offensive file enrichment pipeline.

Nemesis 2.0 is built on [Docker](https://www.docker.com/) with heavy [Dapr integration](https://dapr.io/), our goal with Nemesis was to create a centralized file processing platform that functions as an "offensive VirusTotal".

_Note: the previous Nemesis 1.0.1 code base has been preserved [as a branch](https://github.com/SpecterOps/Nemesis/tree/nemesis-1.0.1)_

## Setup / Installation
Follow the [quickstart guide](https://github.com/SpecterOps/Nemesis/blob/main/docs/quickstart.md).


## Usage
See the [Nemesis Usage Guide](https://github.com/SpecterOps/Nemesis/blob/main/docs/usage_guide.md).


## Additional Information
Blog Posts:

| Title                                                                                                                                                            | Date         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [*Nemesis 1.0.0*](https://posts.specterops.io/nemesis-1-0-0-8c6b745dc7c5)                                                                                        | Apr 25, 2024 |
| [*Summoning RAGnarok With Your Nemesis*](https://posts.specterops.io/summoning-ragnarok-with-your-nemesis-7c4f0577c93b)                                          | Mar 13, 2024 |
| [*Shadow Wizard Registry Gang: Structured Registry Querying*](https://posts.specterops.io/shadow-wizard-registry-gang-structured-registry-querying-9a2fab62a26f) | Sep 5, 2023  |
| [*Hacking With Your Nemesis*](https://posts.specterops.io/hacking-with-your-nemesis-7861f75fcab4)                                                                | Aug 9, 2023  |
| [*Challenges In Post-Exploitation Workflows*](https://posts.specterops.io/challenges-in-post-exploitation-workflows-2b3469810fe9)                                | Aug 2, 2023  |
| [*On (Structured) Data*](https://posts.specterops.io/on-structured-data-707b7d9876c6)                                                                            | Jul 26, 2023 |


Presentations:

| Title                                                                      | Date         |
|----------------------------------------------------------------------------|--------------|
| x33fcon 2025 (TBD)                                                         | Jun 13, 2025 |
| [*SAINTCON 2023*](https://www.youtube.com/watch?v=0q9u2hDcpIo)             | Oct 24, 2023 |
| [*BSidesAugusta 2023*](https://www.youtube.com/watch?v=Ug9r7lCF_FA)        | Oct 7, 2023  |
| [*44CON 2023*](https://www.youtube.com/watch?v=tjPTLBGI7K8)                | Sep 15, 2023 |
| [*BlackHat Arsenal USA 2023*](https://www.youtube.com/watch?v=Ms3o8n6aS0c) | Sep 15, 2023 |


## Acknowledgments

Nemesis is built on large chunk of other people's work. Throughout the codebase we've provided citations, references, and applicable licenses for anything used or adapted from public sources. If we're forgotten proper credit anywhere, please let us know or submit a pull request!

We also want to acknowledge Evan McBroom, Hope Walker, and Carlo Alcantara from [SpecterOps](https://specterops.io/) for their help with the initial Nemesis concept and amazing feedback throughout the development process. Also thanks to [Matt Ehrnschwender](https://twitter.com/M_alphaaa) for tons of k3s and GitHub workflow help in Nemesis 1.0!

And finally, shout out to OpenAI and Claude for helping with this rewrite.


## Additional Documentation

### Overview

# Overview

The goal of Nemesis is to create an extensible file-processing system for
Advesary Simulation operations which takes files collected from C2 agents and
provides automated analysis and assists with triage.

## Project Structure

- **./docs/** - documentation that's published to the GitHub page
- **./infra/** - infrastructure files (Dapr, Postgres, etc.)
- **./libs/** - common library files and the file_enrichment_modules
- **./projects/** - the main logic files that comprise the various services
- **./tools/** - misc helper scripts

## Design Choices

Many of the decisions made with Nemesis 1.X resulted in an over-engineered system that was less flexible and difficult to expand/maintain. Nemesis 2.0 aims to take lessons learned and simplifies the entire architecture:

- Docker/Docker-Compose is used instead of k8s for speed of development
and general ease of use, especially as we didn't experiment with scaling in the
previous version (we may move back to k8s at some point).
- Dapr is now used to increase reliability and to offload infrastructure plumbing concerns
- Strict protobuf schemas were dropped in favor of a flexibilbe schema
- Overall project code/approaches were greatly simplified
- Dropped Elasticsearch (the largest resource hog) in favor of consolidating with PostgreSQL

### HTTP Endpoint

Easy for people to create consumers without needing to structure their messages
with protobuf.

### RabbitMQ

We still use RabbitMQ as the main queuing system for Nemesis. While
RabbitMQ does not have some of the features of Kafka such as persistent storage
and replay, it is significantly lighter weight and can still scale well.

With Dapr pub/sub integration, this can easily be swapped out.

### Hasura

# Hasura

Nemesis uses Hasura to wrap the PostgreSQL backend to easily build a GraphQL and REST API for the structure Nemesis data model.

Navigating to the "Help" menu reachable in the bottom left of the Nemesis interface and clicking the `/hasura/console/` route link will take you to the Hasura login. Enter the value of the `HASURA_ADMIN_SECRET` ENV variable to login.

## Console

The Hasura console allows you to explore the pre-configured backend data schema, which allows you to explore the schema and query data:

![Hasura's Console](https://github.com/SpecterOps/Nemesis/blob/main/images/hasura-console.png)

***Note:*** There is a [quickstart to Hasura queries here](https://hasura.io/docs/latest/queries/quickstart/).

The "Data" tab on top allows you to query the database in a more traditional manner:

![Hasura Data](https://github.com/SpecterOps/Nemesis/blob/main/images/hasura-data.png)

## Scripting

Hasura allows for _external_ queries and subscriptions to the backend schema, very similar to Mythic:

### Queries

Here is an example of performing a basic query against the Hasura Nemesis endpoint:

```python
from base64 import b64encode
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.websockets import WebsocketsTransport
from pprint import pprint
import ssl

HASURA_ENDPOINT = "https://localhost:7443/hasura/v1/graphql"
BASIC_AUTH_USERNAME = "n"
BASIC_AUTH_PASSWORD = "n"
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

transport = AIOHTTPTransport(
    url=HASURA_ENDPOINT,
    headers={'Authorization': basic_auth(BASIC_AUTH_USERNAME, BASIC_AUTH_PASSWORD)},
    ssl=ssl_context
)

client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql(
    """
query MyQuery {
  files_enriched {
    path
    magic_type
    hashes
    size
  }
}
"""
)

results = client.execute(query)

pprint(results["files_enriched"])
```

### Subscriptions

***TODO***

### Cli

# Nemesis CLI

The Nemesis CLI provides tools for interacting with the Nemesis platform, including file submission and data synchronization with external C2 frameworks.

## Overview

The CLI supports four main operations:

- **File Submission**: Upload files directly to Nemesis for processing
- **Folder Monitoring**: Monitor a folder for new files and submit them to Nemesis for processing
- **Mythic Connector**: Synchronize data between Mythic C2 and Nemesis
- **Outflank Connector**: Ingest data from Outflank Stage1 C2 into Nemesis

## Installation & Setup
You can run the Nemesis CLI via its published docker image or by building/running the Python project locally. In general, the easiest way to use it is with the docker helper scripts found in the `./tools/` folder that are detailed below.

### Docker Method (Recommended)

You can pull and run the latest version of the Nemesis CLI docker image with the following command:
```bash
docker run ghcr.io/specterops/nemesis/cli
```
You can then manually invoke it using `docker run`. For example, the following mounts a folder into the container and submits a file:
```bash
docker run --rm --network host -v /tmp/:/data ghcr.io/specterops/nemesis/cli submit /data -r
```

The helper scripts `./tools/submit.sh`, `./tools/monitor_folder.sh`, and `./tools/mythic_connect.sh` wrap the required docker syntax for ease of use and are highly recommended.

If you want to manually build the docker images, see [the Nemesis CLI project's README](https://github.com/SpecterOps/Nemesis/blob/main/projects/cli/README.md).

### Poetry Method (Local Usage or Development)
To use the Nemesis CLI locally or for development, install at least Python 3.12.8 and [install Poetry](https://python-poetry.org/docs/#installation). Then, run the following:

```bash
cd Nemesis/projects/cli
poetry install
poetry run python -m cli <command>
```

## File Submission

Submit files to Nemesis for processing and enrichment.

The `./tools/submit.sh` script wraps the docker syntax automatically.

### Basic Usage

**./tools/submit.sh (easiest option, preferred) :**
```bash
# Submit a single file
./tools/submit.sh /path/to/file

# Submit multiple files
./tools/submit.sh /path/to/file1 /path/to/file2

# Submit directory
./tools/submit.sh /path/to/directory/

# Submit directory recursively (-r or --recursive)
./tools/submit.sh -r /path/to/directory/

# Submit directory, changing the Nemesis server (default is localhost) and credentials (default is n:n)
./tools/submit.sh /path/to/directory/ \
  --host nemesis.example.com:7443 \
  --username your-username \
  --password your-password

# Submit files customizing various options and use debug logging
./tools/submit.sh submit /path/file1 /path/file2  \
  --host nemesis.example.com:7443 \
  --username your-username \
  --password your-password \
  --project my-project \
  --agent-id my-agent \
  --workers 5 \
  --recursive \
  --debug
```

**Poetry :**
```bash
# Submit a single file w/ Poetry env
cd Nemesis/projects/cli
poetry run python -m cli submit /data/file
```

### Options Reference

**See all ./tools/submit.sh options:**
```bash
% ./tools/submit.sh --help
Usage: python -m cli submit [OPTIONS] PATHS...

  Submit files to Nemesis for processing

Options:
  --debug                Enable debug logging
  -h, --host TEXT        Host and port in format HOST:PORT  [default:
                         0.0.0.0:7443]
  -r, --recursive        Recursively process subdirectories
  -w, --workers INTEGER  Number of worker threads  [default: 10]
  -u, --username TEXT    Basic auth username  [default: n]
  -p, --password TEXT    Basic auth password  [default: n]
  --project TEXT         Project name for metadata  [default: assess-test]
  --agent-id TEXT        Agent ID for metadata  [default:
                         submitunknown_user@docker-desktop]
  -f, --file FILE        Path to single file to submit (alternative to PATHS
                         for backwards compatibility)
  --help                 Show this message and exit.
```

| Option        | Default               | Description               |
| ------------- | --------------------- | ------------------------- |
| `--host`      | `0.0.0.0:7443`        | Nemesis host and port     |
| `--recursive` | `false`               | Process subdirectories    |
| `--workers`   | `10`                  | Number of upload threads  |
| `--username`  | `n`                   | Basic auth username       |
| `--password`  | `n`                   | Basic auth password       |
| `--project`   | `assess-test`         | Project name for metadata |
| `--agent-id`  | `submit<user>@<host>` | Agent ID for metadata     |
| `--debug`     | `false`               | Enable debug logging      |

## Folder Monitoring

Monitor a folder for new files and automatically submit them to Nemesis for processing. This includes both existing files (optional) and any new files added to the folder while monitoring is active.

The `./tools/monitor_folder.sh` script wraps the docker syntax automatically.

### Basic Usage

**./tools/monitor_folder.sh (easiest option, preferred) :**
```bash
# Monitor a directory for new files
./tools/monitor_folder.sh /path/to/directory

# Monitor only for new files (skip existing files)
./tools/monitor_folder.sh /path/to/directory --only-monitor

# Monitor a directory upload files to a Nemesis server
./tools/monitor_folder.sh /path/to/directory \
  --host nemesis.example.com:7443 \
  --username your-username \
  --password your-password \
```

**docker:**
```bash
# Monitor a directory
docker run \
  --rm -ti \
  --network host \
  -v /path/to/directory:/data/directory \
  ghcr.io/specterops/nemesis/cli \
  monitor /data/directory

# Monitor only for new files (skip existing)
docker run \
  --rm -ti \
  --network host \
  -v /path/to/directory:/data/directory \
  ghcr.io/specterops/nemesis/cli \
  monitor /data/directory --only-monitor

# Monitor a directory with advanced configuration
docker run \
  --rm -ti \
  --network host \
  -v /path/to/directory:/data/directory \
  ghcr.io/specterops/nemesis/cli \
  monitor /data/directory \
  --host nemesis.example.com:7443 \
  --username your-username \
  --password your-password \
  --project my-project \
  --agent-id my-agent \
  --workers 5  \
  --debug
```

**Poetry :**
```bash
# Monitor a directory w/ Poetry env
cd Nemesis/projects/cli
poetry install
poetry run python -m cli monitor /path/to/directory
```

### Options Reference

| Option           | Default                | Description                                     |
| ---------------- | ---------------------- | ----------------------------------------------- |
| `--host`         | `0.0.0.0:7443`         | Nemesis host and port                           |
| `--username`     | `n`                    | Basic auth username                             |
| `--password`     | `n`                    | Basic auth password                             |
| `--project`      | `assess-test`          | Project name for metadata                       |
| `--agent-id`     | `monitor<user>@<host>` | Agent ID for metadata                           |
| `--workers`      | `10`                   | Number of upload threads for initial submission |
| `--only-monitor` | `false`                | Skip existing files, only monitor for new ones  |
| `--debug`        | `false`                | Enable debug logging                            |


## Mythic Connector

Synchronize data between Mythic C2 and Nemesis, including callbacks, tasks, and file downloads.

The `./tools/mythic_connect.sh` script wraps the docker syntax automatically.

### Configuration

Create a configuration file (e.g., `settings_mythic.yaml`):

```yaml
mythic:
  url: "https://mythic.local:7443"

  # Password authentication
  credential:
    username: "mythic_user"
    password: "mythic_password"

  # OR Token authentication
  # credential:
  #   token: "mythic_api_token"

nemesis:
  url: "https://nemesis.local:7443/"
  credential:
    username: "nemesis_user"
    password: "nemesis_password"
  expiration_days: 100  # File retention period
  max_file_size: 1000000000  # 1GB limit

db:
  path: "mythic_sync.db"  # Local sync state database

networking:
  timeout_sec: 30
  validate_https_certs: true
```

### Usage

**./tools/mythic_connect.sh (easiest option, preferred) :**
```bash
./tools/mythic_connect.sh /path/to/settings_mythic.yaml
```

**docker :**
```bash
# Run with mounted config file
docker run \
  --rm -ti \
  -v /path/to/settings_mythic.yaml:/config/settings_mythic.yaml \
  ghcr.io/specterops/nemesis/cli \
  connect-mythic -c /config/settings_mythic.yaml

# Show example configuration
docker run --rm ghcr.io/specterops/nemesis/cli connect-mythic --showconfig

# Enable debug logging
docker run --rm -ti \
  -v /path/to/settings_mythic.yaml:/config/settings_mythic.yaml \
  ghcr.io/specterops/nemesis/cli \
  connect-mythic -c /config/settings_mythic.yaml --debug
```

### What Gets Synchronized

- **File Downloads**: Agent-collected files
- **Screenshots**: Visual captures from agents

## Outflank Connector

Ingest data from Outflank Stage1 C2 into Nemesis.

### Configuration

Create a configuration file (e.g., `settings_outflank.yaml`):

```yaml
cache_db_path: "/tmp/nemesis_connectors"
conn_timeout_sec: 5
validate_https_certs: true

nemesis:
  url: "https://nemesis.example.com"
  credential:
    username: "connector_bot"
    password: "connector_password"
  expiration_days: 100
  max_file_size: 1000000000

outflank:
  - url: "https://stage1.example.com"
    credential:
      username: "nemesis_bot"
      password: "outflank_password"

    # Optional: Read from disk instead of API
    # outflank_upload_path: "/opt/stage1/"
```

### Usage

```bash
# Run with mounted config file
docker run \
  --rm -ti \
  -v /path/to/settings_outflank.yaml:/config/settings_outflank.yaml \
  ghcr.io/specterops/nemesis/cli \
  connect-outflank -c /config/settings_outflank.yaml

# Show example configuration
docker run --rm ghcr.io/specterops/nemesis/cli connect-outflank --showconfig

# Enable debug logging
docker run --rm \
  -v /path/to/settings_outflank.yaml:/config/settings_outflank.yaml \
  ghcr.io/specterops/nemesis/cli \
  connect-outflank -c /config/settings_outflank.yaml --debug
```

## Common Docker Patterns

### Volume Mounting

```bash
# Mount single file
-v /host/path/file.txt:/container/path/file.txt

# Mount directory
-v /host/path/directory:/container/path/directory

# Mount config file
-v /host/path/config.yaml:/config/config.yaml
```

### Network Access

Use `--network host` if the CLI needs to access services on the host network:

```bash
docker run --rm --network host \
  -v /path/to/config.yaml:/config/config.yaml \
  ghcr.io/specterops/nemesis/cli \
  connect-mythic -c /config/config.yaml
```

### Environment Variables

Pass environment variables for dynamic configuration:

```bash
docker run --rm \
  -e NEMESIS_HOST=nemesis.example.com \
  -e NEMESIS_USER=myuser \
  ghcr.io/specterops/nemesis/cli \
  submit /data/file --host $NEMESIS_HOST --username $NEMESIS_USER
```

## Troubleshooting

### Common Issues

1. **Connection refused**: Check that Nemesis/Mythic/Outflank services are running and accessible
2. **Permission denied**: Ensure Docker has permission to access mounted files/directories
3. **SSL certificate errors**: Set `validate_https_certs: false` in config for self-signed certificates
4. **Large file uploads**: Adjust `max_file_size` and `--workers` for better performance

### Debug Mode

Enable debug logging for detailed information:

```bash
# For connectors
cli connect-mythic -c config.yaml --debug

# For file submission
cli submit /data/files --debug
```

## Performance Tuning

### File Submission

- Increase `--workers` for parallel uploads (default: 10)
- Use `--recursive` efficiently by targeting specific directories
- Monitor network bandwidth and adjust workers accordingly

### Connectors

- Adjust `timeout_sec` based on network conditions
- Use `outflank_upload_path` for better performance with Outflank



### Quickstart

# Quickstart Guide

Here's a quickstart guide to setting up the Nemesis platform.

### Prerequisites

Ensure your machine meets the following requirements:

- **OS**: Linux (use Debian 12) or macOS
- **Processors**: 4 cores
- **Memory**: 12+ GB RAM
- **Disk Space**: 100 GB
- **Architecture**: x64 or Arm
- **Disk:** 80 GB

- **Docker/Docker-Compose:**
  - Docker version 28.0.0 or higher is recommended. See [Docker's installation instructions](https://docs.docker.com/engine/install/) for instructions on installing Docker. Running the Docker Engine on Linux or on OS X via Docker Desktop is recommended. If using Docker Desktop, ensure that the VM is configured with sufficient RAM/Disk/swap.


### Step 1: Clone the Nemesis Repository
```bash
git clone https://github.com/SpecterOps/Nemesis
cd Nemesis
```

### Step 2: Configuration
Create a `.env` file using the provided [env.example](https://github.com/SpecterOps/Nemesis/blob/main/env.example) as a template:
```bash
cp env.example .env
```
Then configure the values in the `.env` file with a text editor.

This file contains passwords and configuration that Nemesis uses. You should randomize these password values for your deployment!

**NOTE:** `NEMESIS_URL` is used to construct the appropriate absolute hyperlinks for findings and Apprise alerts. It does not affect the hosting of Nemesis itself. If using a hostname, a FQDN is preferred.

**NOTE:** for `APPRISE_URLs` to route user feedback to a specific channel use `?tag=feedback` as shown in the example .env file. Otherwise stock alerts will go to the first URL listed. See the [Alerting](./usage_guide.md#alerting) section of the Usage Guide for more information.

**NOTE:** To use your own SSL certificates, simply replace the `server.crt` and `server.key` files at `./infra/traefik/certs/` before launching Nemesis.


### Step 3: Start Nemesis
To start Nemesis's core services, run the `./tools/nemesis-ctl.sh` script:

```bash
./tools/nemesis-ctl.sh start prod
```

If you'd like to install the monitoring services and/or jupyter notebooks, use the associated optional command line arguments:

```bash
./tools/nemesis-ctl.sh start prod --monitoring --jupyter
```
`nemesis-ctl.sh` effectively is a wrapper for `docker compose` commands and is in charge of pulling and starting the appropriate published Nemesis docker images. In general, we recommend people use `nemesis-ctl.sh` instead of manually invoking `docker compose`. For more complex deployment scenarios, see Nemesis's [Docker Compose documentation](https://github.com/SpecterOps/Nemesis/blob/main/docker_compose.md) to understand what `nemesis-ctl.sh` does underneath.

### Step 4: Access the Web Dashboard

In a web browser, open `https://localhost:7443/` (or the URL Nemesis is hosted on) to access the main Nemesis web interface. Use `n:n` for basic auth unless you specified users. Upon logging in, you will enter your username and project (this is saved in your browser cache and only needed once):

![Nemesis Username and Project](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-username-and-project.png)

If needed, you can change these values by clicking the **Settings** tab on the lower left:

![Nemesis Settings](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-settings.png)

After entering your information, you will then be shown the main Nemesis dashboard with processed file statistics and enrichment workflow information:

![dashboard](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard.png)

### Step 5: Upload File for Analysis

To manually upload files into Nemesis, click on the "File Upload" link in the sidebar. On this page you can upload one or more files into Nemesis:

![file analysis](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-file-upload_success.png)

After uploading the files, click on the "Files" link in the sidebar. Once Nemesis processes the files, they will appear in the table:

![file listing](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-files.png)

Click on the table row to to view the file's details:
![Nemesis File Details](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-file-details.png)

See [Data Ingestion](./usage_guide.md#data-ingestion) for additional ways to ingest data into Nemesis besides manually uploading files through the web interface.

### Step 6: View Other Nemesis Services

Click on the "Help" button on the bottom left to view the additionally exposed Nemesis services. Each route listed is a hyperlink to the service. For logins, refer to the environment variables set.

**NOTE:** The monitoring services (Grafana, Jaeger, and Prometheus) will only be available if you started with them enabled (`--monitoring`).

**NOTE:** The /jupyter/ route will only be available if you started with it enabled (`--jupyter`).

![Nemesis services](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-services.png)

### Step 7: Shutting Nemesis Down

To shutdown Nemesis, use the `nemesis-ctl.sh` script's `stop` or `clean` commands ***with the same arguments you used to start it***. For example, if you started it with monitoring and jupyter enabled, then run the following:
- To stop Nemesis containers:
```bash
./tools/nemesis-ctl.sh stop prod --monitoring --jupyter
```

- To stop Nemesis containers and delete their associated volumes:
```bash
./tools/nemesis-ctl.sh clean prod --monitoring --jupyter
```


### Dapr

# Dapr

Nemesis 2.0 makes heavy use of [Dapr](https://dapr.io/), the Distributed Application Runtime. The Dapr components that Nemesis utilizes are detailed in the following sections. Images in this page were pulled from the appropriate locations from the [Dapr Documentation](https://docs.dapr.io/).

## Pubsub

Nemesis utilizes the [Dapr Publish & subscribe](https://docs.dapr.io/developing-applications/building-blocks/pubsub/) building block for its internal queueing system. Currently, Nemesis utilizes RabbitMQ for the queue, but this can easily be easily swapped for [alternative systems](https://docs.dapr.io/reference/components-reference/supported-pubsub/) like Kafka or Redis Streams by ensuring the provider is stood up in the [docker-compose.yml](https://github.com/SpecterOps/Nemesis/tree/main/docker-compose.yml), modifying the [pubsub.yaml](https://github.com/SpecterOps/Nemesis/tree/main/infra/dapr/components/pubsub.yaml) file with an alternative provider, and ensuring the connection string is passed through via an environment variable as in the current pubsub.yaml example.

![Dapr Pubsub](https://github.com/SpecterOps/Nemesis/blob/main/images/dapr-pubsub-overview-components.png)

## Workflows

[Dapr Workflows](https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-overview/) enable developers to build reliable, long-running business processes as code. They provide a way to orchestrate microservices with built-in state management, error handling, and retry logic for complex distributed applications.

![Dapr Workflow Overview](https://github.com/SpecterOps/Nemesis/blob/main/images/dapr-workflow-overview.png)

Nemesis uses in two specific places/services. First, in the [file_enrichment](https://github.com/SpecterOps/Nemesis/tree/main/projects/file_enrichment/file_enrichment/workflow.py) project, Dapr workflows are used to control the main file enrichment processing logic. The **enrichment_workflow()** function controls the main enrichment workflow, with the **enrichment_module_workflow()** function invoked as a child workflow.

The [document_conversion](https://github.com/SpecterOps/Nemesis/tree/main/projects/document_conversion/document_conversion/main.py) project also implements a Dapr workflow in the **document_conversion_workflow()** function to handle converting documents and extracting text. This is broken out into a separate project as it's a time-consuming task.

## Secrets

Nemesis uses the [Dapr Secrets management](https://docs.dapr.io/developing-applications/building-blocks/secrets/secrets-overview/) building block to protect secrets internally (like Postgres connection strings). Currently the [Local environment variables](https://docs.dapr.io/reference/components-reference/supported-secret-stores/envvar-secret-store/) component is used. These secrets are also refereced within some Dapr files such as [pubsub.yaml](https://github.com/SpecterOps/Nemesis/tree/main/infra/dapr/components/pubsub.yaml).

This reason for using this abstraction is so alternative secret management systems like [Vault or Kubernetes secrets](https://docs.dapr.io/reference/components-reference/supported-secret-stores/) can be used in the future:

![Dapr Secrets](https://github.com/SpecterOps/Nemesis/blob/main/images/dapr-secrets-overview-cloud-stores.png)

An example of retrieving a secret is at the top of the the [housekeeping code](https://github.com/SpecterOps/Nemesis/blob/main/projects/housekeeping/housekeeping/main.py) to retrieve the `POSTGRES_CONNECTION_STRING` string.

## Service Invocation

In a few places in Nemesis, Dapr's [Service Invocation](https://docs.dapr.io/developing-applications/building-blocks/service-invocation/service-invocation-overview/) building block is used to ease the complexity of some API invocations. This building block is specifically used when calling the Gotenberg API and when calling some of the internal file enrichment APIs by the web API.


### Usage Guide

# Nemesis Usage Guide

This page covers usage of Nemesis after the system is properly [setup](https://github.com/SpecterOps/Nemesis/blob/main/quickstart.md).

For a general overview of the Nemesis project structure, see the [overview](https://github.com/SpecterOps/Nemesis/blob/main/overview.md).

- [Nemesis Usage Guide](#nemesis-usage-guide)
  - [Data Ingestion](#data-ingestion)
    - [Nemesis C2 Connector Setup](#nemesis-c2-connector-setup)
  - [Nemesis Dashboard](#nemesis-dashboard)
    - [Files](#files)
      - [File Triage Mode](#file-triage-mode)
      - [File Details](#file-details)
      - [File Tags](#file-tags)
    - [Manual File Upload](#manual-file-upload)
    - [Document Search](#document-search)
    - [Findings](#findings)
    - [Dashboard Settings](#dashboard-settings)
  - [Alerting](#alerting)
    - [User Feedback](#user-feedback)
  - [Submitting Files via the API](#submitting-files-via-the-api)
    - [API Documentation](#api-documentation)

## Data Ingestion

Once Nemesis is running, data first needs to be ingested into the platform. Ingestion into Nemesis can occur in muliple ways, including:

* [Auto-ingesting data from C2 platorms](#nemesis-c2-connector-setup), including Mythic and Outflank C2.
* [Manually uploading files on the "File Upload" page in the Nemesis's Dashboard UI.](#manual-file-upload)
* [Using the CLI tool](https://github.com/SpecterOps/Nemesis/blob/main/./cli.md) to:
    * [submit individual files or entire folders/subfolders](./cli.md#file-submission)
    * [monitor a folder for new files and auto-submit them](./cli.md#folder-monitoring).
* Writing custom tools to interact with [Nemesis's API](#api-documentation).

### Nemesis C2 Connector Setup

Nemesis includes connectors for [Mythic](https://github.com/its-a-feature/Mythic) and Outflank C2 (formerly Stage1). The connectors hook into the C2 platforms and transfer data automatically into Nemesis. The connectors are located in the [CLI](https://github.com/SpecterOps/Nemesis/tree/main/projects/cli/cli/) project.

See the [CLI](https://github.com/SpecterOps/Nemesis/blob/main/./cli.md) documentation for more details on configuration.

## Nemesis Dashboard

The main method for operators/analysts to interact with Nemesis data is through the Nemesis Dashboard. The dashboard can be accessed at `https://NEMESIS_IP/HOST:7443/`. The initial display shows details about the number of processed files and enrichment workflow information:

![Nemesis Dashboard](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard.png)

### Files

One of the common tasks for the dashboard is file triage, accessible through the `Files` page on the left navigation bar:

![Nemesis Dashboard Files View](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-files.png)

As files are processed by Nemesis, they will appear as lines on this page. By default the files will be sorted newest to oldest, but this can be modified by clicking the "Newest First" button at the top which will switch it to showing the oldest first.

Likewise, the "(Findings) All Files" is the default (showing all files), but clicking shows just files with findings. The "Filter by path" text entry can be used to filter by file path/name/extension, and entries can be filtered by agent ID.

When clicking on a file entry, you will be brought to the [File Details](#file-details) page. After viewing a file, the entry will be hidden by default on the "Files" page - click the "Files Unviewed by Me" entry on the top left to view select "Unviewed Files" to show files not viewed by anyone (including you), or "All Files" to view all files regardless of view state:

![Nemesis Dashboard File View State](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-files-view-state.png)

Also, clicking any column will sort by that column's values.

#### File Triage Mode

In the main files view, type `t` to enter file triage mode:

![Nemesis Dashboard File Triage Mode](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-files-triage-mode.png)

As the instructions specify, Use ↑↓ to navigate. Use Shift+↑↓ to select multiple rows. Ctrl/Cmd+A to select all. 'v' to mark as viewed, or ESC to exit. Only the files currently showed by the specified filters you've applied will be marked as viewed. These files will then be hidden from the main triage pane.

#### File Details

Clicking on a file entry in the "Files" view brings you to a file details view:

![Nemesis File Details](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-file-details.png)

On the top left of this view, you'll see basic metadata like the file name, magic/mime types, MD5/SHA1 hashes, etc.

Press **[tab]** to autoscroll (or scroll manually) to get to the "File Content" view. Here, different tabs will display the summaries and transforms for a file. Pressing `p` will cycle between these views:

![Nemesis File Details Content](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-file-details-content.png)

Any plaintext file identified with a specific file type will be rendered with that using the [Monaco](https://github.com/microsoft/monaco-editor) code editorL

![Nemesis File Details Monaco](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-file-details-monaco.png)

If you scroll to the bottom of the page past "File Content" you cans see some basic details about the file enrichment workflow, including any successful and failed enrichments. Mousing over any failed enrichment module nodes will reveal a basic error message.

![Nemesis File Details Enrichments](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-file-enrichment-status.png)

If an enrichment module is failing on your file, we recommend using [the Loki logs in Grafana](./troubleshooting.md#grafana) to help track down what's going on (tip: using the file's `object_id` UUID can help track down specific log lines).

#### File Tags

In the file details view, clicking the "+ Add Tag" button will allow you to create new tags, or add existing defined tags, to the file:

![Nemesis File Details Tagging](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-file-details-tagging.png)

These tags will persist in the display, and can be used to filter files in the main files view:

![Nemesis Files Tag Filtering](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-files-tag-filtering.png)

### Manual File Upload

Files can be manually uploaded through the Nemesis dashboard via the `File Upload` tab on the left navigation bar. The "Project Name" will be auto-completed, and the "Expiration Time" will be auto set for 100 days in the future (this can be changed in the "Settings" button on the bottom left). The "Originating File Path" is optional but recommended. Files can be dragged/dropped into the upload modal, and on successful submission Nemesis will display the following message:

![Nemesis Dashboard File Upload](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-file-upload_success.png)

The file will then be displayed in the [Files](#files) page as soon as it's done processing.

### Document Search

Nemesis indexes the full text of any plaintext file, or the extracted plaintext of any plaintext that can have ASCII/Unicode text extracted. This is stored in the PostgreSQL backend and searchable through this interface. Partial document matches will be shown, while clicking on the file name will take you to the file details page:

![Nemesis Document Search](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-docsearch.png)

Clicking the topright filter icon will bring down filters you can apply for searches:

![Nemesis Document Search Filter](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-docsearch-filter.png)

### Findings

One of the other common tasks for the dashboard is findings triage, accessible through the `Files` page on the left navigation bar:

![Nemesis Findings](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-findings.png)

Clicking on a finding brings up details for the finding:

![Nemesis Finding Details](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-finding-detail.png)

Clicking the hyperlinked file path will take you to the file details page for the file the finding originates from.

You can filter findings by triage state, category, severity, module origin, and triage source (human/automated) at the top of the table.

Like with the `Files` page, type `t` to enter triage mode. This will add a check box to the currently selected file along with displaying keyboard actions you can take:

![Nemesis Finding Triage](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-finding-triage.png)

As the text details, use ↑↓ to navigate findings, → to view finding details details. You can select multiple with Shift + ↑↓, hitting space, or Ctrl+A. Clear selection with ESC. Typing 1, 2, or 3 will set the finding as true positive, false positive, or unknown:

![Nemesis Finding Triage](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-finding-triage2.png)

When combined with the default "Untriaged Only" filter, this allows you to easily and collaboratively triage a large number of findings.

Also, clicking any column will sort by that column's values.

### Dashboard Settings

Navigating to the "Settings" menu reachable in the bottom left of the Nemesis interface will take you to the settings page:

![Nemesis Dashboard Settings](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-settings.png)

Here, you can change your username/project ID, as well as modify the data expiration (in absolute date or number of days), and can clear the Nemesis database and datalake.

Clicking the "Light Mode" or "Dark Mode" menu button in the bottom left will toggle display mods for the application

## Alerting

If Slack alerting is enabled (i.e., if the `APPRISE_URLS` ENV variable is set), alerts on "interesting" files (e.g., parsed credentials, Nosey Parker hits, DPAPI data discovery, etc.) will be pushed to the configuered Slack webhook/channel with **Nemesis** as the bot user. These messages will contain the alert name, alert category, any additional details, a sanitized file path and a link to the [file details](#file-details) and finding details in the dashboard:

![Nemesis Slack Alerting](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-finding-slack-alert.png)

See the [Apprise Wiki](https://github.com/caronc/apprise/wiki) for the string format needed for each alerting service.

### User Feedback

If you want user feedback from the [File Details viewer](#file-details) to be routed for alerting, use an Apprise link like `slack://Nemesis@T...k/#nemesis-feedback?tag=feedback` - this will route user feedback actions to that specified channel, with regular alerts going to any configured channel without the feedback tag.

You can configure multiple Apprise URLs for alerting and user feedback (i.e., alerting to multiple services).

## Submitting Files via the API

You can submit files using Nemesis's `submit` CLI tool:
```bash
./tools/submit.sh
```

Uploading a with curl:
```bash
curl -k -u n:n -F "file=@example.txt" \
        -F 'metadata={"agent_id":"agent123","project":"assess-test","timestamp":"2025-01-29T12:00:00Z","expiration":"2026-02-29T12:00:00Z","path":"/data/files"}' \
        https://nemesis:7443/api/files
```

### API Documentation

Navigating to the "Help" menu reachable in the bottom left of the Nemesis interface will show you the clickable `/api/docs` and `/api/redoc` Swagger and ReDoc API documentation, respectively:

![Swagger API Documentation](https://github.com/SpecterOps/Nemesis/blob/main/images/api-swagger.png)

![ReDoc API Documentation](https://github.com/SpecterOps/Nemesis/blob/main/images/api-redoc.png)

### Odr

# Operational Data Reference

This Operational Data Reference (ODR) is the key a reference for how data should be formated to be accepted and parsed by the Nemesis. The Nemesis 2.0 ODR is significantly simpler than the Nemesis 1.X ODR and consists solely of a [file](#file) entry.

## File
Schema definition for the public `file` message POSTed to the API frontend.

## Message Structure

### Required Fields

| Field        | Type     | Description                                                                    |
| ------------ | -------- | ------------------------------------------------------------------------------ |
| `object_id`  | string   | UUID v4 format identifier for the current object                               |
| `agent_id`   | string   | Identifier for the processing agent                                            |
| `project`    | string   | Project identifier                                                             |
| `timestamp`  | datetime | ISO 8601 formatted timestamp indicating when the file was downloaded           |
| `expiration` | string   | ISO 8601 formatted timestamp indicating when the data should expire in Nemesis |

### Optional Fields

| Field                   | Type     | Description                                                                                                      |
| ----------------------- | -------- | ---------------------------------------------------------------------------------------------------------------- |
| `path`                  | string   | File system path to the relevant resource. Can use either forward (/) or backward (\\) slashes                   |
| `originating_object_id` | string   | UUID v4 format identifier referencing a parent or source object                                                  |
| `nesting_level`         | number   | The level of nesting for the file within an originating container. Used to prevent indefinite container nesting. |
| `creation_time`         | datetime | ISO 8601 formatted timestamp for when the file was created                                                       |
| `access_time`           | datetime | ISO 8601 formatted timestamp for when the file was last accessed                                                 |
| `modification_time`     | datetime | ISO 8601 formatted timestamp for when the file was last modified                                                 |


## Example Message - Derivative File
```json
{
  "agent_id": "339429212",
  "project": "assess-X",
  "timestamp": "2024-08-01T22:51:35",
  "expiration": "2025-08-01T22:51:35",
  "path": "C:\\temp\\file.txt",
  "object_id": "2f0a4f7a-6b97-4869-a8b6-d7df3c9f5124",
  "originating_object_id": "f309b012-d0a1-4639-bd29-77a4dc582576"
}
```

## Example Message - File Extracted from a Container
```json
{
  "agent_id": "339429212",
  "project": "assess-X",
  "timestamp": "2024-08-01T22:51:35",
  "expiration": "2025-08-01T22:51:35",
  "path": "C:\\temp\\file.txt",
  "object_id": "2f0a4f7a-6b97-4869-a8b6-d7df3c9f5124",
  "originating_object_id": "f309b012-d0a1-4639-bd29-77a4dc582576",
  "nesting_level": 1
}
```

## Notes
- All timestamps must be in ISO 8601 format with timezone information
- File paths can use either forward (/) or backward (\\) slashes
- UUIDs should follow the v4 format
- The schema may be extended with additional optional fields in the future
- If `originating_object_id` is present but `nesting_level` is not or is 0, then the file is a derivative file.
- If `originating_object_id` is present and `nesting_level` is present and > 0, then the file was extracted from a container.

### Docker Compose

# Deploying Nemesis with Docker Compose

In general, we recommend that people use the `./tools/nemesis-ctl.sh` script to deploy Nemesis. However, more complex deployment scenarios will require understanding how to deploy Nemesis components manually using Docker Compose. The documentation below details how you can launch Nemesis in a variety

## Use Published Production Docker Images

### Step 1 - Configure environment variables
```bash
cp env.example .env
vim .env
```

### Step 2 - Pull and start the images

The examples below show various ways you can pull and start Nemesis.

**Example 1: Start production images (no monitoring/jupyter)**
```bash
docker compose -f compose.yaml up -d
```

**Example 2: Start production images + monitoring**
```bash
NEMESIS_MONITORING=enabled \
docker compose \
  -f compose.yaml \
  --profile monitoring \
  up -d
```

**Example 3: Start production images + monitoring + jupyter**
```bash
NEMESIS_MONITORING=enabled \
docker compose \
  -f compose.yaml \
  -f compose.prod.build.yaml \
  --profile monitoring \
  --profile jupyter
  up -d
```


## Building and Using Production Images Locally

### Step 1 - Build base images
```bash
docker compose -f compose.base.yaml build
```

### Step 2 - Build & then start production images
**Example 4: Build & then start production images without monitoring/jupyter**
```bash
docker compose \
  -f compose.yaml \
  -f compose.prod.build.yaml \
  up --build -d
```

**Example 5: Build & then start production images with monitoring**
```bash
NEMESIS_MONITORING=enabled \
docker compose \
  -f compose.yaml \
  -f compose.prod.build.yaml \
  --profile monitoring \
  up --build -d
```


## Building and Using Development Images

Development images are not published and must be built locally. If you make any local modifications to project code, you need to build + run the development images.

The easiest method to build + run dev images is to just use the `dev` target instead of `prod` with `./tools/nemesis-ctl.sh` :
```bash
./tools/nemesis-ctl.sh start dev [--monitoring] [--jupyter]
```

### Step 1 - Configure environment variables
```bash
cp env.example .env
vim .env
```

### Step 2 - Build base images
```bash
docker compose -f compose.base.yaml build
```

### Step 3 - Build and start dev images
**Example 6: Build and start dev images without monitoring/jupyter (implicitly merges compose.yaml and compose.override.yaml)**
```bash
docker compose up -d
```

**Example 7: Build and start dev images with monitoring + jupyter**
```bash
NEMESIS_MONITORING=enabled \
docker compose \
  --profile monitoring \
  --profile jupyter \
  up -d
```

### Troubleshooting

# Troubleshooting

Nemesis has a number of services to help with assist with troubleshooting.

**Note** that Grafana + Jaeger tracing are only available if you use the `--monitoring` flag when launching Nemesis!

## Grafana

Navigating to the **Help** menu reachable in the bottom left of the Nemesis interface and clicking the `/grafana/` route link will take you to the Grafana interface. Clicking the **Metrics** Grafana link on the Help page will take you to the general metrics visualization:

![Grafana Metrics](https://github.com/SpecterOps/Nemesis/blob/main/images/grafana-metrics.png)

Clicking the **Logs** Grafana link on the Help page will take you to the general logs Loki idexing in Grafana:

![Grafana Logging](https://github.com/SpecterOps/Nemesis/blob/main/images/grafana-logging.png)

Filtering by a specific service name will allow you to drill down into the logging for that service, which can easily be searched, for example with the `nemesis-file-enrichment` service:

![Grafana Logging](https://github.com/SpecterOps/Nemesis/blob/main/images/grafana-logging-details.png)

Clicking the dashboards link in Grafana will bring you to a few preconfigured dashboards as well:

![Grafana Dashboard](https://github.com/SpecterOps/Nemesis/blob/main/images/grafana-dashboards.png)

## RabbitMQ Dashboard

While the queueing system for Nemesis is swappable with Dapr, Nemesis currently uses RabbitMQ. Navigating to the **Help** menu reachable in the bottom left of the Nemesis interface and clicking the `/rabbitmq/` route link will take you to the RabbitMQ interface. This interface can be used to track message delivery rates/etc.

![RabbitMQ Dashboard](https://github.com/SpecterOps/Nemesis/blob/main/images/rabbitmq.png)

## Jaeger Tracing

Navigating to the **Help** menu reachable in the bottom left of the Nemesis interface and clicking the `/jaeger/` route link will take you to the Jaeger tracing interface. Reaching Jaeger via this link will filter for the `file-enrichment: /TaskHubSidecarService/StartInstance` trace type by default (the Dapr file_enrichment workflow trace):

![Jaeger traces](https://github.com/SpecterOps/Nemesis/blob/main/images/jaeger-traces.png)

Clicking a trace will give you more information on the trace:

![Jaeger trace details](https://github.com/SpecterOps/Nemesis/blob/main/images/jaeger-trace-details.png)

This can help track down locations for slowdown or other failures- for example by filtering across services for `error=true`:

![Jaeger trace error](https://github.com/SpecterOps/Nemesis/blob/main/images/jaeger-trace-error.png)

## Lazydocker

While [Lazydocker](https://github.com/jesseduffield/lazydocker) is not a Nemesis specific project, we highly recommend it for general troubleshooting when using Docker containers:

![Lazydocker](https://github.com/SpecterOps/Nemesis/blob/main/images/lazydocker.png)

### Performance

# Performance Tuning

Nemesis may perform differently depending on the system architecture and resources, specifically RAM and the number of CPUs.

If workflows begin to fail, or you are experiencing major performance issues (as diagnosed by the [Troubleshooting](https://github.com/SpecterOps/Nemesis/blob/main/troubleshooting.md) document) there are a few tunable parameters that can help. Alternatively, if your performance is fine and you want to potentially increase performance, you can increase these values. Most/all of these values involve altering behaviors for the `file-enrichment` service.


### UVICORN_WORKERS

For production (non-dev) deployments, multiple UVICORN_WORKERS are used for the `file-enrichment` service. The default value is 2 and is defined in the `file-enrichment` section in [compose.yaml](https://github.com/SpecterOps/Nemesis/blob/71406afc12f855140ea68aae337076f9b8dc292f/compose.yaml#L217). This value can be set to 1 for troubleshooting, or increased to 4+ for potential performance gains. You can modify this value by defining the `export UVICORN_WORKERS=4` environment variable before launching Nemesis.


### MAX_PARALLEL_WORKFLOWS

The `file-enrichment` container runs a number of file-enrichment workflows in parallel, defaulting to 5. You can modify this value by defining the `export MAX_PARALLEL_WORKFLOWS=3` environment variable before launching Nemesis.


### MAX_PARALLEL_ENRICHMENT_MODULES

For each file enrichment workflow, the `file-enrichment` container runs multiple file enrichment modules in parallel, defaulting to 5. You can modify this value by defining the `export MAX_PARALLEL_ENRICHMENT_MODULES=3` environment variable before launching Nemesis.


### File Enrichment Modules

## Adding File Enrichment Modules

File enrichment modules for the main enrichment workflow are located in [libs/file_enrichment_modules/file_enrichment_modules/](https://github.com/SpecterOps/Nemesis/tree/main/libs/file_enrichment_modules).

To add a new module, create a new folder matching Python's [PEP8 naming conventions](https://peps.python.org/pep-0008/#package-and-module-names):
>Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

Create a main `analyzer.py` file with your enrichment logic. The easiest method for this (and enrichment modules are fairly small) is to find an example module, and use it as a base with a LLM to help draft your code.

If your module needs additional dependencies, you have two options. Before either, first [install Poetry](https://python-poetry.org/).

For the first option, you can `cd` to `projects/file_enrichment` or `libs/file_enrichment_modules/` and run `poetry add X` for the needed library.

Alternatively (and easier) you can create a `pyproject.yaml` in the new module module folder. An example is:

```toml
[tool.poetry]
name = "module"
version = "0.1.0"
description = "Enriches things"
authors = ["harmj0y <will@harmj0y.net>"]
package-mode = false

[tool.poetry.dependencies]
python = "^3.9"
```

Then in this folder, run `poetry add X` to add a new library. The dynamic module loader will install the necessary dependencies in a Poetry env for just that module.

## Tips / Tricks

The `should_process()` function determines if the module should run on a file. You can either check the name or any other component of the base enriched file with `file_enriched = get_file_enriched(object_id)`:

```python
...
def should_process(self, state_key: str) -> bool:
    """Determine if this module should run based on file type."""
    file_enriched = get_file_enriched(state_key)
    # Check if file appears to be a VNC config file
    should_run = (
        file_enriched.file_name.lower().endswith(".ini")
        and "vnc" in file_enriched.file_name.lower()
        and "text" in file_enriched.magic_type.lower()
    )
    logger.debug(f"VncParser should_run: {should_run}, magic_type: {file_enriched.magic_type.lower()}")
    return should_run
...
```

Or you can use a Yara rule (or you could do both!):

```python
...
    # Yara rule to check for DPAPI blob content
    self.yara_rule = yara_x.compile("""
rule has_dpapi_blob
{
    strings:
        $dpapi_header = { 01 00 00 00 D0 8C 9D DF 01 15 D1 11 8C 7A 00 C0 4F C2 97 EB }
        $dpapi_header_b64_1 = "AAAA0Iyd3wEV0RGMegDAT8KX6"
        $dpapi_header_b64_2 = "AQAAANCMnd8BFdERjHoAwE/Cl+"
        $dpapi_header_b64_3 = "EAAADQjJ3fARXREYx6AMBPwpfr"
    condition:
        $dpapi_header or $dpapi_header_b64_1 or $dpapi_header_b64_2 or $dpapi_header_b64_3
}
    """)

def should_process(self, object_id: str) -> bool:
    file_enriched = get_file_enriched(object_id)
    if file_enriched.size > self.size_limit:
        logger.warning(
            f"[dpapi_analyzer] file {file_enriched.path} ({file_enriched.object_id} / {file_enriched.size} bytes) exceeds the size limit of {self.size_limit} bytes, only analyzing the first {self.size_limit} bytes"
        )

    num_bytes = file_enriched.size if file_enriched.size < self.size_limit else self.size_limit
    file_bytes = self.storage.download_bytes(file_enriched.object_id, length=num_bytes)

    should_run = len(self.yara_rule.scan(file_bytes).matching_rules) > 0
    logger.debug(f"[dpapi_analyzer] should_run: {should_run}")
    return should_run
...
```

## On Transforms

File transforms require a `type` (used as a title for display) and an `object_id` to reference the data to display.

Optional metadata is:

| Metadata Field            | Type         | Description                                                            |
| ------------------------- | ------------ | ---------------------------------------------------------------------- |
| file_name                 | string       | Name of the file (i.e., for downloads)                                 |
| display_type_in_dashboard | display_type | How to display in the dashboard                                        |
| display_title             | string       | Title to display for the transform in the dashboard                    |
| default_display           | bool         | `true` to set this transform as the default display                    |
| offer_as_download         | bool         | If set to `true` offered as a download tab, downloading as `file_name` |

Display Types are:

| Value    | Description                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------------- |
| monaco   | Display in a Monaco editor, using the extension from `file_name` to help determine the language type. |
| pdf      | Render as a PDF                                                                                       |
| image    | Render as an image                                                                                    |
| markdown | Render as an image                                                                                    |
| null     | Don't display content                                                                                 |

### Examples

Example of setting a text file as the default display (in file_enrichment_modules/sqlite/analyzer.py):

```python
with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8") as tmp_display_file:
    display = format_sqlite_data(database_data)
    tmp_display_file.write(display)
    tmp_display_file.flush()

    object_id = self.storage.upload_file(tmp_display_file.name)

    displayable_parsed = Transform(
        type="displayable_parsed",
        object_id=f"{object_id}",
        metadata={
            "file_name": f"{file_enriched.file_name}.txt",
            "display_type_in_dashboard": "monaco",
            "default_display": True
        },
    )
enrichment_result.transforms = [displayable_parsed]
```

Example of offering a file for download (in file_enrichment_modules/dotnet/analyzer.py):

```python
decompilation = Transform(
    type = "decompilation",
    object_id = service_results["decompilation"]["object_id"],
    metadata = {
        "file_name" : f"{file_enriched.file_name}.zip",
        "offer_as_download" : True
    }
)
enrichment_result.transforms = [decompilation]
```


### Housekeeping

# Housekeeping

The [housekeeping](https://github.com/SpecterOps/Nemesis/tree/main/projects/housekeeping/) service handles the automated cleanup of expired files and database entries.

This service periodically checks for files and database entries that have passed their expiration date and removes them from both the Minio storage and the database tables. This helps maintain system performance and ensures compliance with data retention policies.

When the serivce runs, entries in the database with an "expiration" datetime value past the current time will be removed, along with their associated files in the Minio datalake.

## Features

- Scheduled daily cleanup of expired data (configurable)
- Handles deletion of files from Minio storage
- Cleans up related database entries
- Supports manual triggering of cleanup jobs
- Maintains proper logging of cleanup activities

## Configuration

The service can be configured using environment variables:

- `CLEANUP_SCHEDULE`: Cron expression for the cleanup schedule (default: `0 0 * * *` - midnight every day)
- `LOG_LEVEL`: Set the logging level (default: `INFO`)

These ENV variables can be adjusted in the [docker-compose.yml](https://github.com/SpecterOps/Nemesis/tree/main/docker-compose.yml) file.

## Endpoints

- `GET /healthz`: Health check endpoint for Docker healthcheck
- `GET /`: Service information
- `POST /trigger-cleanup`: Manually trigger a cleanup job


### Noseyparker Rules

## Adding Nosey Parker Rules

Nemesis uses [Nosey Parker](https://github.com/praetorian-inc/noseyparker) wrapped through [an customized Dapr pub/sub scanner implementation](https://github.com/SpecterOps/Nemesis/tree/main/projects/noseyparker_scanner).

There are a number of custom rules that are specified at [projects/noseyparker_scanner/custom_rules/rules.yaml](https://github.com/SpecterOps/Nemesis/tree/main/projects/noseyparker_scanner/custom_rules/rules.yaml).

```yaml
rules:
  - name: sha256crypt Hash
    id: custom.sha256crypt
    pattern: '(\$5\$(?:rounds=\d+\$)?[\./A-Za-z0-9]{1,16}\$(?:(?:[\./A-Za-z0-9]{43})))'
    references:
      - https://akkadia.org/drepper/SHA-crypt.txt
      - https://hashcat.net/wiki/doku.php?id=example_hashes
    examples:
      - '$5$rounds=5000$GX7BopJZJxPc/KEK$le16UF8I2Anb.rOrn22AUPWvzUETDGefUmAV8AZkGcD'
      - '$5$B7RCoZun804NXFH3$PltCS6kymC/bJTQ21oQOMCLlItYP9uXvEaCV89jl5iB'
      - '$5$JzPB.C/yL0uBMMIK$/2Jr.LeQUg0Sgbm8UhF01d1X643/YHdmRzwlVmt3ut3'
      - '$5$rounds=80000$wnsT7Yr92oJoP28r$cKhJImk5mfuSKV9b3mumNzlbstFUplKtQXXMo4G6Ep5'
      - '$5$rounds=12345$q3hvJE5mn5jKRsW.$BbbYTFiaImz9rTy03GGi.Jf9YY5bmxN0LU3p3uI1iUB'

  - name: sha512crypt Hash
    id: custom.sha512crypt
    pattern: '(\$6\$(?:rounds=\d+\$)?[\./A-Za-z0-9]{1,16}\$(?:(?:[\./A-Za-z0-9]{43})))'
    references:
      - https://akkadia.org/drepper/SHA-crypt.txt
      - https://hashcat.net/wiki/doku.php?id=example_hashes
    examples:
      - '$6$52450745$k5ka2p8bFuSmoVT1tzOyyuaREkkKBcCNqoDKzYiJL9RaE8yMnPgh2XzzF0NDrUhgrcLwg78xs1w5pJiypEdFX/'
      - '$6$Blzt0pLMHZqPNTwR$jR4F0zo6hXipl/0Xs8do1YWRpr47mGcH49l.NCsJ6hH0VQdORfUP1K1HYar1a5XgH1/JFyTGnyrTPmKJBIoLx.'

...
```

If you want to add additional rules, just modify [rules.yaml](https://github.com/SpecterOps/Nemesis/tree/main/projects/noseyparker_scanner/custom_rules/rules.yaml) with the new rule (or add a new rules.yaml) and restart the noseyparker-scanner container.

### Jupyter

# Jupyter Notebooks

Jupyter Lab environment for exploring Nemesis data through interactive notebooks with direct access to Hasura GraphQL and PostgreSQL.

## Overview

The Jupyter service provides a powerful data analysis environment that allows you to:

- Query Nemesis data using Hasura GraphQL
- Perform advanced data analysis and visualization
- Create custom investigations and reports
- Explore file metadata, enrichment results, and security findings

## Access

When Nemesis is running, Jupyter is available at:

**URL**: `https://your-nemesis-host/jupyter/`

![Jupyter](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-jupyter-notebook1.png)

This is also linked to by the Nemesis `Help` menu.

## Authentication

### Environment Variable Password

Use the `JUPYTER_PASSWORD` value in .env (or ENV variable) to log in. If this value is not set, you can discover the randomized value by running `docker compose logs jupyter | grep PASS` .

## Getting Started

### 1. Sample Notebooks

The service comes with pre-configured sample notebooks:

- **`1_getting_started.ipynb`**: Introduction to querying Nemesis data with examples
- **`2_triage_false_positive_findings.ipynb`**: Marking findings with specific criteria as false positives

### 2. Pre-installed Libraries

The Jupyter environment includes:

- **Data Analysis**: pandas, numpy, matplotlib, seaborn, plotly
- **GraphQL Client**: gql[requests] for Hasura queries
- **Database Access**: psycopg2-binary for direct PostgreSQL connections
- **Utilities**: ipywidgets, python-dotenv

### 3. Environment Variables

The following environment variables are automatically configured:

- `HASURA_GRAPHQL_URL`: GraphQL endpoint (`http://hasura:8080/v1/graphql`)
- `HASURA_ADMIN_SECRET`: Admin secret for Hasura access


### Index

![Logo](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dark.png#only-dark)
![Logo](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-light.png#only-light)

<p align="center">
<img src="https://img.shields.io/badge/version-2.0.0-blue" alt="version 2.0.0"/>
<a href="https://join.slack.com/t/bloodhoundhq/shared_invite/zt-1tgq6ojd2-ixpx5nz9Wjtbhc3i8AVAWw">
    <img src="https://img.shields.io/badge/Slack-%23nemesis—chat-blueviolet?logo=slack" alt="Slack"/>
</a>
<a href="https://twitter.com/tifkin_">
    <img src="https://img.shields.io/twitter/follow/tifkin_?style=social"
      alt="@tifkin_ on Twitter"/></a>
<a href="https://twitter.com/harmj0y">
    <img src="https://img.shields.io/twitter/follow/harmj0y?style=social"
      alt="@harmj0y on Twitter"/></a>
<a href="https://twitter.com/0xdab0">
    <img src="https://img.shields.io/twitter/follow/0xdab0?style=social"
      alt="@0xdab0 on Twitter"/></a>
<a href="https://github.com/specterops#nemesis">
    <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fspecterops%2F.github%2Fmain%2Fconfig%2Fshield.json&style=flat"
      alt="Sponsored by SpecterOps"/>
</a>
</p>
<hr />

## Overview

Nemesis is an offensive file enrichment pipeline.

Nemesis 2.0 is built on [Docker](https://www.docker.com/) with heavy [Dapr integration](https://dapr.io/), our goal with Nemesis was to create a centralized file processing platform that functions as an "offensive VirusTotal".

## Additional Information
Blog Posts:

| Title                                                                                                                                                            | Date         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [*Nemesis 1.0.0*](https://posts.specterops.io/nemesis-1-0-0-8c6b745dc7c5)                                                                                        | Apr 25, 2024 |
| [*Summoning RAGnarok With Your Nemesis*](https://posts.specterops.io/summoning-ragnarok-with-your-nemesis-7c4f0577c93b)                                          | Mar 13, 2024 |
| [*Shadow Wizard Registry Gang: Structured Registry Querying*](https://posts.specterops.io/shadow-wizard-registry-gang-structured-registry-querying-9a2fab62a26f) | Sep 5, 2023  |
| [*Hacking With Your Nemesis*](https://posts.specterops.io/hacking-with-your-nemesis-7861f75fcab4)                                                                | Aug 9, 2023  |
| [*Challenges In Post-Exploitation Workflows*](https://posts.specterops.io/challenges-in-post-exploitation-workflows-2b3469810fe9)                                | Aug 2, 2023  |
| [*On (Structured) Data*](https://posts.specterops.io/on-structured-data-707b7d9876c6)                                                                            | Jul 26, 2023 |


Presentations:

| Title                                                                      | Date         |
|----------------------------------------------------------------------------|--------------|
| [*SAINTCON 2023*](https://www.youtube.com/watch?v=0q9u2hDcpIo)             | Oct 24, 2023 |
| [*BSidesAugusta 2023*](https://www.youtube.com/watch?v=Ug9r7lCF_FA)        | Oct 7, 2023  |
| [*44CON 2023*](https://www.youtube.com/watch?v=tjPTLBGI7K8)                | Sep 15, 2023 |
| [*BlackHat Arsenal USA 2023*](https://www.youtube.com/watch?v=Ms3o8n6aS0c) | Sep 15, 2023 |


## Acknowledgments

Nemesis is built on large chunk of other people's work. Throughout the codebase we've provided citations, references, and applicable licenses for anything used or adapted from public sources. If we're forgotten proper credit anywhere, please let us know or submit a pull request!

We also want to acknowledge Evan McBroom, Hope Walker, and Carlo Alcantara from [SpecterOps](https://specterops.io/) for their help with the initial Nemesis concept and amazing feedback throughout the development process. Also thanks to [Matt Ehrnschwender](https://twitter.com/M_alphaaa) for tons of k3s and GitHub workflow help in Nemesis 1.0!

And finally, shout out to OpenAI and Claude for helping with this rewrite.

### Yara

## Yara

Nemesis has the ability to dynamically edit existing, and deploy new, Yara rules which are run against all files (including plaintext extracted from applicable files). These rules are stored in the PostgreSQL backend and [dynamically loaded](https://github.com/SpecterOps/Nemesis/tree/main/libs/file_enrichment_modules/file_enrichment_modules/yara/yara_manager.py) by the Yara file enrichment module uses [yara-x](https://github.com/VirusTotal/yara-x) for performant scanning.

Clicking on "Yara Rules" tab on the left will bring you to the main Yara rules page. In development mode, a single test rule will be present; in production mode a number of existing rules will be loaded:

![Yara Rules](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-yara.png)

### Adding New Rules

Click the "New Rule" button on the top to draft a new Yara rule and click "Create". The rule name will be extracted from the definition:

![Yara Rules New](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-yara-new.png)

![Yara Rules Reload](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-yara-reload.png)

After rule creation, click the (now) green "Reload Yara Engine" button to ensure the Yara backend is reloaded with the new rule states. The rules will be saved in the database and reload if the entire system is brought down and up again.

### Adding New Default Rules

If you want to change the default set of rules _without_ having to add rules on each deployment, add a new yara file to `./libs/file_enrichment_modules/yara_rules/dev/` for development or `./libs/file_enrichment_modules/yara_rules/prod/` for production.

### Editing Existing Rules

To edit an existing rule, click the "Edit Rule" button under actions, modify the rule as wanted, and click "Save":

![Yara Rules Edit](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-yara-edit.png)

Like when adding a new rule, ensure you click the (now) green "Reload Yara Engine" button to ensure the Yara backend is reloaded with the new rule states.

### Rule Alerts

Alerts for any matching rules will be shows in the [Findings](https://github.com/SpecterOps/Nemesis/blob/main/findings.md) tab. This will include the data match as well as the rule details:

![Yara Rules Edit](https://github.com/SpecterOps/Nemesis/blob/main/images/nemesis-dashboard-yara-match.png)
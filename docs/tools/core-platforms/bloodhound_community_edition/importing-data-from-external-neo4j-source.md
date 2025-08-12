---
description: Importing Data From External Neo4J Source documentation
title: Importing Data From External Neo4J Source
---

## Overview

If you have a Neo4J database that you'd like to import into BloodHound to reuse directly, our local dev process (and the Docker Compose example) has an environment variable allowing you to target a folder on disk to use as the `/data` directory for Neo4J. For local dev, the environment variable is named `BH_NEO4J_VOLUME` and the default in the `.env.example` is to use `./local-harnesses/data` as the mount point. This mount point path is preferred as it will be automatically ignored by Git. For the user's example docker compose, this variable is named `NEO4J_VOLUME` and is set to look for `./neo4j/data`.

## Getting a copy of an existing database

### Database running in a docker container

You will want to make sure the database container is stopped before copying the database to ensure nothing is being written at the time. You do not want to remove the container, just put it into a stopped state. If you're running with `docker compose up`, a simple `ctrl+c` is all that's needed.

You can use [`docker cp`](https://docs.docker.com/engine/reference/commandline/cp/) to copy the data directory out of an existing container. Note that you'll need the container id to do so.

If you're using the example `docker compose`, you can instead use `docker compose cp graph-db:/data ./neo4j/data` to copy the current data into the mountable folder location.

For local dev, use `just bh-dev cp graph-db:/data ./local-harnesses/data` instead.

### Database running standalone

You'll need to identify your data directory location first, which varies by operating system/install method. See https://neo4j.com/docs/operations-manual/5/configuration/file-locations/#:~:text=cd%20conf.-,Data,-%5B3%5D for further details.

Once you've identified where your data lives, shut down Neo4J before proceeding. Once the service has cleanly shut down, you'll be free to copy your `data` directory. It might be helpful to `zip` or `tarball` the folder, as it can be quite large depending on your dataset.

## Import data
Copy the folder you've gotten above to `./local-harnesses/data` (local dev) or `./neo4j/data` (example docker compose) in your project directory. Make sure the directory structure is correct (you should see something like `./local-harnesses/data/databases` if everything was done correctly, if you see `.local-harnesses/data/data` you've accidentally nested the data and the import won't work). Once everything is in place, be sure to set your `BH_NEO4J_VOLUME` or `NEO4J_VOLUME` environment variable from above. The easiest way to do this is to copy the value from `.env.example` and paste it into a `.env` file in your project. For local dev, this file isn't tracked, so it will only contain the environment variables you set. Once the environment is set up, you're safe to run `just bh-dev` (local dev) or `docker compose up` (example docker compose) and should see log lines showing that Neo4J is migrating the database for you.

## FAQ
**Q: I've followed the above steps, but Neo4J crashes. What can I do?**
A: While this could be many things, the first troubleshooting step should be to run `just bh-dev down -v` or `docker compose down -v` to remove all previous data. Then starting the containers back up should start fresh (with your filesystem mount untouched).
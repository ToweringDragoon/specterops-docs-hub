---
description: Configuring Database Connections documentation
title: Configuring Database Connections
---

## Environment Variables

Users can alter their database auth credentials for the Docker Compose example with the following environment variables:
* POSTGRES_USER=bloodhound
* POSTGRES_PASSWORD=bloodhoundcommunityedition
* POSTGRES_DB=bloodhound
* NEO4J_USER=neo4j
* NEO4J_SECRET=bloodhoundcommunityedition

These can be altered either through your normal OS / shell mechanisms, or by creating a `.env` file next to your `docker-compose.yml` and setting the variables within it.

## How Docker Compose Uses the Variables

When these variables are set, the first run of your `docker-compose.yml` will use them both for the initial configuration of the databases (setting the username/password/database as requested) and for the application to connect to those databases. After your databases have been configured, they will only affect the running application, as the database containers only take initial credentials when they first create their volume. After that, changes will require you to delete the database volumes or connect to the running database and change the credentials through the normal mechanisms appropriate for each database.
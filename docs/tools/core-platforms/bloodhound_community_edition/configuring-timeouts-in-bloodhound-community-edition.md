---
description: Configuring Timeouts In BloodHound Community Edition documentation
title: Configuring Timeouts In BloodHound Community Edition
---

## Introduction
There are multiple timeouts a user can encounter when working with BloodHound Community Edition, and they can interact in different ways. The defaults are meant to protect your running instance of BloodHound from becoming unstable, but if you need to push the absolute limits, here's a list of known timeouts that may allow you to get results for slow queries.

## Timeout Configurations
### API Request Timeouts
The first type of timeout is the HTTP request timeout. This timeout during a cypher query request defaults to 15 minutes, though query complexity calculations can time box it further (more on that later). It is allowed to be set up to 30 minutes on a query by query basis. To request a higher limit, set the `Prefer: wait=1800` header, where 1800 is the number of seconds you'd like the API to wait before timing out. 1800 seconds (30 minutes) is the maximum it will respect.

### Cypher Query Complexity Limit
The second type of timeout modifier is the cypher query complexity limiter. By default, this system analyzes queries and estimates relative cost modifiers based on the query's relative complexity. This modifier will further limit the timeout to some fraction as a protection mechanism. Disabling this behavior will mean the API will hold the connection open for the full time that's been configured (either the wait time given by the Prefer header or 15 minutes if unset). To disable the complexity limiter, use the environment variable `bhe_disable_cypher_complexity_limit=true`.

### Neo4j Transaction Timeouts
Sometimes the API isn't the limiting factor. If your Neo4j transactions are timing out before the API should be timing out using the above methods to increase it, updating the Neo4j container's environment variables is the best bet. The main environment variable to set in your `docker-compose.yml` in the `graph-db` service definition is `NEO4J_dbms_transaction_timeout=true`. For better clarity, here's the sample `docker-compose.yml` configuration needed:
```yaml
...
services:
...
  graph-db:
    environment:
      - NEO4J_AUTH=${NEO4J_USER:-neo4j}/${NEO4J_SECRET:-bloodhoundcommunityedition}
      - NEO4J_dbms_allow__upgrade=${NEO4J_ALLOW_UPGRADE:-true}
      - NEO4J_dbms_transaction_timeout=true
...
```

If you've tried all the above options together but still can't seem to lift API timeouts as expected, please file a new issue on the repository and include logs showing the timeouts and any errors/additional information around them. Please include the specs you're running bloodhound in and any configuration options you've changed from the defaults.
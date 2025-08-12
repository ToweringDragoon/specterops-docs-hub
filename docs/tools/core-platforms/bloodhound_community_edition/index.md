---
description: BloodHound Community Edition documentation
title: BloodHound Community Edition
---

# Welcome to the BloodHound Community Edition Development Wiki!

## Introduction
BloodHound CE is a security tool that uses graph theory to reveal the hidden and often unintended relationships within an Active Directory or Entra ID (formerly known as Azure AD) environment. Attackers can use BloodHound to easily identify highly complex attack paths that would otherwise be impossible to quickly identify. Defenders can use BloodHound to identify and eliminate those same attack paths. Both blue and red teams can use BloodHound to easily gain a deeper understanding of privilege relationships in an Active Directory or Azure environment.

If you're visiting this wiki as a regular BloodHound user and not a developer, we highly recommend checking out our [official documentation](https://bloodhound.specterops.io/home). These pages hold a wealth of knowledge around setup, usage, and best practices for BloodHound CE and Enterprise, as most information is interchangeable between the two versions.

If the docs still didn't have an answer then feel free to reach out to us or the Community for help. You can check out the [Contact](https://github.com/SpecterOps/BloodHound/wiki/Contact) page for more information.

## Quick Start
Deploy BloodHound CE quickly using [the BHCE QuickStart instructions](https://bloodhound.specterops.io/get-started/quickstart/community-edition-quickstart). 

## Development

Details on setting up the BloodHound CE development environment and contributing code can be found on the [Development page](https://github.com/SpecterOps/BloodHound/wiki/Development).

## Upcoming Upgrade to Postgres Version 16

BloodHound will soon be targeting Postgres 16 for development. This is part of our ongoing effort to ensure better performance and security, grant us access to new features, and to stay ahead of the release support schedule. Postgres 13's last release is scheduled for November 13th, 2025. As of this writing, it is **not required** to update any pre-existing Postgres deployment to use newer versions of BloodHound.

If you have data that you want to keep, follow the steps below on how to back up and restore your data before the upgrade happens. Once the upgrade is done on the repo, any unbacked data will be lost. If you prefer to upgrade your environment using other methods, links to alternative approaches are provided at the end. 

Otherwise, if you have no concern for data loss, no action is required and the upgrade will proceed automatically.

```
# 0. Depending on which version you're running, either 13.2 or 16, you may have to run these commands twice. Where each attempt is (1) going from 16 to 13.2, and then (2) back to 16. If you're still on 13.2, you only need to run these commands once. 

# 1. Stop any running containers, navigate to examples/docker-compose/, and start only the database container
docker compose up app-db

# 2. Change the password encryption from MD5 to SCRAM-SHA-256 format (Postgres 16 defaults to this format)
docker compose exec app-db sh -c "psql -c \"SET password_encryption = 'scram-sha-256'; ALTER ROLE CURRENT_USER PASSWORD '\${BH_POSTGRES_PASSWORD:-bloodhoundcommunityedition}';\""

# 3. Export existing data via a database dump (while the database container is running)
docker compose exec app-db pg_dumpall > dump.sql

# 4. Stop with Ctrl+C and remove the database container
docker compose rm -f app-db

# 5. Remove only the database volume for the Postgres service
docker volume rm docker-compose_postgres-data

# 6. Edit the docker-compose.yml file in examples/docker-compose/docker-compose.yml or whatever directory the file is kept
```
<img width="961" alt="Screenshot 2024-09-30 at 12 20 49 PM" src="https://github.com/user-attachments/assets/763f6824-9605-4818-9f7f-bf4f599eb877">

Or

<img width="957" alt="Screenshot 2024-10-02 at 3 20 13 PM" src="https://github.com/user-attachments/assets/c2815d01-62b8-4297-9a0f-5ed7b8035018">

```
# 7. Start only the database container
docker compose up app-db

# 8. Restore the database from the dump file
docker compose exec -T app-db psql < dump.sql

# 9. Stop the database container with Ctrl+C

# 10. Finally, start all containers
docker compose up
```

### Alternative Upgrade Methods
If you'd prefer to upgrade via alternative methods, check out the following resources:

https://github.com/tianon/docker-postgres-upgrade/tree/master

https://github.com/pgautoupgrade/docker-pgautoupgrade

### Questions or Concerns?
If you have any questions or need assistance with backing up or restoring your data, please feel free to reach out to the team on our official BloodHound community [Slack](https://slack.specterops.io/)!

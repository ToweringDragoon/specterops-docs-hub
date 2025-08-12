---
description: Using Environment Variables For Sensitive Configuration documentation
title: Using Environment Variables For Sensitive Configuration
---

# Configuration with Environment Variables

## How Environment Variables in BloodHound Work

All configuration options available in the `bloodhound.config.json` file format are also available as environment variables.
This allows for easy configuration overrides for any option, as well as allowing for sensitive configuration values to be
passed in without them being stored on disk.

For the following JSON configuration:

```json
{
    "default_admin": {
        "principal_name": "admin",
        "first_name": "BloodHound",
        "last_name": "Admin",
        "email_address": "spam@example.com"
    }
}
```

You can provide each option as an environment variable:

`bhe_default_admin_principal_name=admin`
`bhe_default_admin_first_name=BloodHound`
`bhe_default_admin_last_name=Admin`
`bhe_default_admin_principal_email=spam@example.com`

### Passing Environment Variables Through to Docker Container

In addition to having these environment variables set, you'll also need to pass them to the Docker container.
In the official Docker Compose example, you can do this by modifying the `environment` list in `docker-compose.yml`.
Simply add a line for each environment variable you want to load: `- bhe_default_admin_principal_name=${bhe_default_admin_principal_name}`.
The `${}` syntax is important, as it will allow you to read your environment variables from the session Docker Compose
is running in, using that value for the environment variable in the Docker container.

### BloodHound Environment Variable Rules

-   BloodHound environment variables are case insensitive
-   Prefix is always `bhe_`
-   Environment variables encode the JSON representation as a path
-   Environment variables use an `_` to delimit parts of the path
-   If a component of the path contains an underscore in its name (e.g. `default_admin`), the underscore is not altered
-   While this does make the environment variable a little less human readable (you can't easily distinguish between path
    parts and names with underscores), the parser for environment variables is able to easily identify the tokens and split the
    path correctly, since it knows which tokens are valid.

## List of Potentially Sensitive Environment Variables

The following is a list of environment variables that have been identified as potentially worth using rather than storing
in the JSON config. When deploying BloodHound, ensure you're choosing the right balance of using the configuration file
and using environment variables for your security needs.

-   SAML
    -   `bhe_saml_sp_cert`
    -   `bhe_saml_sp_key`
-   TLS
    -   `bhe_tls_cert_file`
    -   `bhe_tls_key_file`
-   Database
    -   `bhe_database_connection`
    -   `bhe_database_addr`
    -   `bhe_database_username`
    -   `bhe_database_secret`
    -   `bhe_database_database`
-   Neo4J
    -   `bhe_neo4j_connection`
    -   `bhe_neo4j_addr`
    -   `bhe_neo4j_username`
    -   `bhe_neo4j_secret`
    -   `bhe_neo4j_database`
-   Crypto
    -   `bhe_crypto_jwt_signing_key`
-   Default Admin
    -   `bhe_default_admin_principal_name`
    -   `bhe_default_admin_password`
    -   `bhe_default_admin_email_address`
    -   `bhe_default_admin_first_name`
    -   `bhe_default_admin_last_name`
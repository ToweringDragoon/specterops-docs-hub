---
description: Application Database Migrations documentation
title: Application Database Migrations
---

# BloodHound App Database Migration Field Guide

## Introduction

The BloodHound application database was originally built using Gorm auto-migrations. Over time, the need for separate stepwise migrations arose to handle cases that Gorm models could not. Today, Gorm auto-migrations have been removed due to long time pain points and migration errors. In their place, we now implement a base schema that matches the one Gorm auto-migrate created at the time of the transition, and run stepwise migrations on top of it. In the case that a database already exists, we only apply the stepwise migrations that haven't been applied yet, using the semver stored in the database migrations table vs the currenly running API semver to determine which files need to be migrated.

The loss of Gorm's AutoMigrate functionality adds some cognitive overhead. Simply labeling a Gorm model with constraints, changing its fields, or otherwise modifying the schema that should be used with a model will not automatically carry over to the underlying database. To be clear, any destructive operation already wouldn't work, so this cognitive overhead isn't actually new. However, there is a bit more process involved and you will need to dust off your raw SQL skills to write migrations for model changes you make.

### Gorm Models

Our models currently live in `cmd/api/src/model`. The current reality of the app is that models are often multipurpose, meaning you'll find plenty of models that are designed for use as JSON models in the API layer and as Gorm models at the database layer. Any modification to these models must be understood by the engineer making the modifications and the appropriate database schema changes need to be written as a stepwise migration.
### Stepwise Migrations

Our stepwise migrations can be found under `cmd/api/src/database/migration/migrations`. Stepwise migrations are intended to take on the name of the next semver release that they are expected to be a part of. If you are unsure what the previous release semver is, run `just show` after pulling the latest `main` and it will give you the last tagged version. For example, if the current version is `v5.5.0`, and the next release is expected to be a feature release, the stepwise migration should be named `v5.6.0`. If the next release were to be a patch release (like a hotfix), it would be `v5.5.1` instead. Migration names may be changed later if the release they belong to is moved or requires a different version bump than expected, but the current target should be determined when writing the migration. Afterall, others may also be adding migrations to the same release cycle, so sharing that file will be important.

Stepwise migrations should be written as concise, deterministic, and idempotent SQL targeting Postgres. Testing should be done both manually against the database using a database tool like DBeaver or `psql`, as well as through migration (see Testing Migrations for detailed steps).

## Authoring Model Changes

As stated above, models are currently shared between Gorm and other application needs in many cases. Most importantly, many models are used as API response types. As a result, any changes made to a model should be preceded by careful study of where the model is used and what parts of the application are impacted. If the modification could cause a breaking API change, it will need to be reviewed with the BHE team to assess whether it's warranted or if another approach will be necessary.

In the cases where the intended modification of a model is both necessary and the impact is understood and approved, an assessment of database schema impact is required. Some examples include: 

- Adding a field requires a stepwise migration that adds the same field to the database schema, being mindful of naming conventions in Gorm https://gorm.io/docs/conventions.html.
- Removing a field requires a stepwise migration to remove the field from the database as well
- Changing the name of a field will require a corresponding rename operation in the stepwise migration.
- Constraints should no longer be added to the model (as they're only read for AutoMigrate and CreateTable use cases) but instead be explicitly created/modified/deleted with a stepwise migration in all cases.
- New tables will need to include all the metadata fields in addition to the explicit fields. Most models "inherit" (through embedding) fields from a struct that implements a specific type of `id` and embeds the `Basic` struct, which adds the `CreatedAt`, `UpdatedAt`, and `DeletedAt` fields. Always parse all embedded structs in your model and include their fields in your table migration.

Follow best judgement, ensure your migrations are idempotent (can be re-run without causing changes or errors), and test thoroughly from the database layer all the way up to API integration testing and manual API endpoint testing.

## Example Migration

The example migration PR template linked below is based on the migration found in [cmd/api/src/database/migration/test_migrations/v0.1.1.sql](https://github.com/SpecterOps/BloodHound/blob/main/cmd/api/src/database/migration/test_migrations/v0.1.1.sql)

The following is a template to follow for documenting your manual migration testing in your pull request:

### PR Testing Section Template (might make sense as a separate linked document)

#### Testing Steps

1. Run `just bh-dev`
2. Create fresh database on `main`
	1. `git checkout main`
	2. `just bh-dev down -v` (clear existing volumes)
	3. `just bh-dev` (wait for server to start, then proceed)
3. Input example dataset (see below)
4. Test the migration directly
	1. In your database, go to migrations and delete the row with version set to `v999.999.999`
		1. If this is the only row in your database (which is likely), add a new row with the last release tag given from `just show` using `INSERT INTO migrations (major, minor, patch) VALUES (<major>, <minor>, <patch>)` where major/minor/patch are the integers you get from the last release tag.
	2. Stop currently running `bh-dev` (`ctrl+c` or `just bh-dev stop`)
	3. Checkout this branch
	4. `just bh-dev` to start the server and run migrations
	5. If successful, there should be a log that this migration was run, as well as additional entries in the migrations table
5. Validate the data that was expected to be migrated was successfully migrated and that the data that shouldn't be migrated was not touched.
6. Check the schema of the affected table/tables to ensure that it matches the intended new schema post-migration
#### Example Dataset

```
-- Insert data we expect to be migrated
INSERT INTO migration_test (name, foo)
VALUES ('foo', 'foo'), ('foo', 'bar'), ('foo', 'bar')

-- Insert data we expect to be untouched (canary)
INSERT INTO migration_test (name, foo)
VALUES ('bar', 'baz')
```

#### Screenshots

Before Migration:

![Pasted image 20231024125512](https://github.com/SpecterOps/BloodHound/assets/466326/e1343fc1-f9c2-4f87-8b45-f6b687115f2b)
![Pasted image 20231024125542](https://github.com/SpecterOps/BloodHound/assets/466326/15b6dde5-3e34-4e84-ad76-f77ffa803c3b)

After Migration:

![Pasted image 20231024125339](https://github.com/SpecterOps/BloodHound/assets/466326/7b2e4170-dc82-4859-8b80-7e4696397dec)
![Pasted image 20231024125405](https://github.com/SpecterOps/BloodHound/assets/466326/81d40c14-cd0a-42de-ba75-d929f57d3b58)


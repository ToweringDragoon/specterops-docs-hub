---
description: Development documentation
title: Development
---

# Running the Development environment

There are 2 methods for starting up the BloodHound CE development environment: running via Docker Compose or running containers manually. Each of these methods has pre-built `just` commands to easily start and stop the services.

If you are looking to learn more about how the code is structured and generally works please check out the [Code wiki](https://github.com/SpecterOps/BloodHound/wiki/Code).

## Prerequisites

-   A machine or VM with at least 16GB of RAM and at least 8 CPU threads (assuming running VS Code or another full IDE in the same machine, along with other dev tools)
    -   It's possible to get away with less RAM, but more is generally going to make developing easier, especially when working with more than toy graphs
    -   Number of CPU threads doesn't necessarily matter too much, but more threads will make things run a lot better since BloodHound and its tooling works with a decent amount of parallelization
-   [Just](https://github.com/casey/just)
-   [Python 3.10](https://www.python.org/downloads/)
-   [Go 1.23](https://go.dev/dl/)
-   [Node 22](https://nodejs.dev/en/download/)
-   [Yarn 3.6](https://yarnpkg.com/getting-started/install)
-   [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or Docker/Docker Compose compatible runtime)

# Running via Docker Compose

BloodHound CE contains a development Docker Compose setup that focuses on making it easy to validate changes to the application in development mode. The following features are available:

* Running the entire application stack with hot reloading of source files (HMR for TypeScript and Air rebuilds for Go)
* Running pieces of the application stack with hot reloading (ability to run `api-only` to spin up only the API and databases, not the UI)
* Running the application stack with `dlv` debugging enabled (default port is `3456` and the API won't start up until you connect, allowing for debugging of application setup)
* Running a separate bank of databases as targets for project integration tests

## Quick Start

* Run `just init`
* Run `just bh-dev`
* To access the UI, navigate to `http://bloodhound.localhost`. Login with the user `admin` and password that can be found in the log output of the app.

## Building

The BloodHound team maintains a Python tool for building and testing the project called [`beagle`](./packages/python/beagle/README.md).
Building locally requires simply running `just build`. At the end, all the artifacts will be available in `dist`.

## Configuration

If you're getting started for the first time, or want to reset your configuration files, you can use `just init` to get everything setup with defaults. No manual configuration should be required unless you want to change how the system runs in some way.

### Config files

The following is a map of where you can find the configuration files that govern this system:

* `docker-compose.dev.yml`: this is the primary entrypoint for running our containers and all development services are defined here, with environment variables to allow for easy customization locally
* `docker-compose.testing.yml`: this is the entrypoint used to run our testing databases (they autorestart by default, so they're a set and forget configuration)
* `.air.toml`: defines how to run the API with hot reloading enabled using `cosmtrek/air`
* `.air.debug.toml`: defines how to run the API in debugging mode with hot reloading enabled using `cosmtrek/air`
* `tools/docker-compose/`: contains our Dockerfiles used to build the development images and any supporting files they need
* `local-harnesses/`: contains templates for configuration files compatible with this system (as well as local only copies of the actual configuration files you use)

### Environment File

We have a `.env.example` file available that enumerates the environment variables that the docker compose services support. This includes options like service port forwards (in case you have other things running on the default ports), changing the service hostnames, changing which `build.config.json` file you would like to have read when starting up (allows you to have multiple config files and easily switch which is being read on each run), and changing database credentials.

It can be used by copying any values you want to `.env` and modifying as needed. Note that you don't need to keep all the environment variables in your local copy, and can instead allow docker compose to use the defined defaults for anything you don't want to change. The defaults in `.env.example` should generally be kept in sync with the defaults defined in `docker-compose.dev.yml`.

### Build Configuration

BloodHound supports configuring many options through either environment variables or a configuration json file. The template `local-harnesses/build.config.json.template` contains defaults that work out of the box with our docker compose system, with some helpful development options set (not requiring password reset on initial login, setting a static password, etc). The `just init` command will copy this template for you by default, but you can create additional `*.config.json` files if you want to have multiple configurations set up for different scenarios you want to develop against, and change the `BH_CONFIG_FILE` env var in your local `.env` file to point at the config you wish to use at any given time.

### Integration Test Configuration

BloodHound has many integration/E2E tests in its suite. These can either be exercised through your IDE or using `beagle`. However, you'll need to define real databases for these integration tests to run against and pass a configuration as an environment variable. The configuration that gets used by default (when using VS Code or `just`) is `local-harnesses/integration.config.json` which is made from the corresponding template when you run `just init`. Normally you shouldn't need to alter this file, but if you need to pass different API config values, this is the file to change.

The testing databases are defined in `docker-compose.testing.yml` and there's a useful `just` recipe to get them started up.

## Just Command Usage

The best way to interact with our dev environment is using `just`. There are a number of `just` commands tailored to different development needs, including:

* `just init`: ensures that your environment is initialized, including your default `build.config.json` and `integration.config.json` files
* `just bh-dev`: runs services in development mode with hot reloading enabled
    * By default, the application is available at `bloodhound.localhost`
    * By default, Neo4J’s web interface can be accessed at `neo4j.localhost` with the default user:password being neo4j:bloodhoundcommunityedition
    * This recipe allows running other `docker compose` commands, such as `build` and `down`. Use it rather than invoking `docker compose` directly to ensure the right profiles are being selected
* `just bh-debug`: runs services in debug mode with hot reloading enabled
    * Works pretty much exactly like `bh-dev`, except that the API container is run with `dlv` and it will not start the actual API service until you attach a debugger (to ensure it’s easy to debug the startup sequence or other items that might try to race you).
    * BHCE’s debug port is `3456` and there’s a built in configuration for debugging in VS Code under the name `Docker Compose Debug`
    * Hot reloading will cause the debugger to detach, which is an unfortunate limitation. However, the API still won't start back up until you reattach and doing so is usually pretty fast, so it shouldn't interrupt flows too much (you don't want to be changing code while a debugger is active anyway)
* `just bh-testing`: runs the integration testing containers for you
    * Defaults to running `up -d`, so will run in the background
    * This recipe allows running other `docker compose` commands, such as `build` and `down`. Use it rather than invoking `docker compose` directly to ensure the right profiles are being selected

### Clearing volumes

If you need to reset your databases, just use one of the above `just` commands with `down -v`. This will down the containers and remove the backing volumes, giving you a clean slate.

# Testing

The BloodHound project encourages strong automated test coverage so we can move quickly without unknowingly breaking much of the app. We have a few different test environments: Go unit tests, Go integration tests, and React unit tests.

## Running tests

### Unit tests

To run both the Go and UI unit tests, run the following command:

```bash
$ just test
```

By default, test results will be cached after being run. The cache will remain intact until the related files are changed. The following flags can be helpful when running tets.
-   `-a`: Run all tests, even if nothing has changed since the last run
-   `-v`: Run in verbose mode (display output while tests are running)

### Integration tests

The following command will run integration tests in addition to unit tests. Simply make sure that you have your testing
databases running (`just bh-testing`) before running them.

```bash
just test -i
```

To run [cypress](https://www.cypress.io/) UI integration tests:

```bash
$ npx cypress run
```

To open [cypress](https://www.cypress.io/) UI integration testing GUI:

```bash
$ npx cypress open
```

# Debug

For VS Code, there is already a profile created for debugging called Debug with Docker Compose

For debugging in a JetBrains IDE:

-   Open `Run/Debug Configurations` and add a new `Go Remote` config
-   Host: `localhost`
-   Port: `3456`
-   On disconnect: `Leave it running`

# FAQ

**Q: I'm getting an error related to writing the `go.work.sum` file, how do I fix it?**  
A: Run `just build -v` to do a local build of the system. This will update your local `go.work.sum` file for you. Since the container uses the same `go.work.sum` that you have locally, it needs to be up to date. A better solution is in the works, but making the volume not read-only brings a lot of headaches so this needs to be fixed with better tooling outside of Docker.

**Q: My dev databases are broken, how can I rebuild them?**  
A: Run `just bh-dev down -v` to reset all your volumes and then start dev again

**Q: I've made a change to yarn (dependencies, configuration, vite, etc). How do I get those changes in the UI container?**  
A: If you use `just yarn` when doing yarn actions, the default is to also rebuild the UI container for you. If you've made changes without using `just yarn` and would like to just rebuild the containers, you can do `just bh-dev build bh-ui` to rebuild the UI container. You'll need to restart your containers after rebuilding to see the effect.

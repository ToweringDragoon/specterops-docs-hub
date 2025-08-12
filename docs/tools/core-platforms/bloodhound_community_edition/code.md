---
description: Code documentation
title: Code
---

# Project Structure

<!-- Intentionally blank for markdown rendering purposes -->

```

.
├── cmd                                // Artifact source code and their integration tests
|   |                                  // Partitioned By: Utility
│   ├── api
│   ├── ui
|   └── ...
|
├── dist                               // Built artifacts (git ignored)
|
├── dockerfiles                        // Misc. Dockerfiles
|
├── examples                           // Examples for Deploying BloodHound
|
├── packages                           // Libraries/Modules/Packages/Plugins (a.k.a. re-useable do-dads) and their UNIT tests
|   |                                  // Partitioned By: Language/Runtime
│   ├── go
│   |   └── ...
|   |
|   ├── python
│   |   └── beagle
|   |
│   └── javascript
│       └── ...
|
└── tools                              // Misc. tooling (docker compose related files, etc)
```

# Documentation

## API Documentation

We use swagger to show our API documentation alongside our GUI. You can access these docs in your local dev environment
at http://bloodhound.localhost/ui/api-explorer

Please check out our [OpenAPI Spec Guide](https://github.com/SpecterOps/BloodHound/wiki/OpenAPI-Spec-Guide) to learn more about how we author and utilize OpenAPI spec in BloodHound.

# Tests

## Organizing Unit Tests

Our unit tests are organized in the following manner to encourage modular/reusable API design emphasizing consumer
experience. Unit testing requires appropriate use of mocks, stubs, and fakes to separate testing the unit from testing
its dependencies.

### Typescript

For each file, unit testing shall maintain the following pattern:

-   `src/**/<file name>.{ts,tsx}` - The unit(s) being tested
-   `src/**/<file name>.test.{ts,tsx}` - The unit tests

### Golang

For each file in a package, unit testing shall maintain the following pattern:

-   `<package path>/<file name>.go` - The unit(s) being tested
-   `<package path>/<file name>_test.go` - Unit tests for package exports
    -   The package of this file shall be `<package>_test`
-   `<package path>/<file_name>_internal_test.go` - Unit tests for non-exported functions (optional)
    -   The package of this file shall be `<package>`
    -   Reserved for situations where:
        -   functions cannot be exported
        -   control-flow is too difficult or expensive to test with only mocks, etc.

## Integration Tests

### VS Code

VS Code is already configured to run integration tests against the testing database docker containers. Simply run `just init`
to initialize the necessary configurations and be sure the testing databases are running if you haven't started them already
(`just bh-testing`).

You can then use the normal testing options in VS Code to discover tests and run them (Testing charm, test run options inline
in files, etc).

### Beagle

The BloodHound team maintains a Python tool called [`beagle`](./packages/python/beagle/README.md), which is currently found
in `/packages/python/beagle`. Simply run `just show` to see all plans that beagle is capable of running (tests and builds).
You can run `just test -avi` to run all API and UI tests with integration tests enabled. Or you can run `just test -avi <plan_name>`
to run all tests from a specific plan with integration tests enabled.

## Mocks

### Golang

The project uses the [mockgen](https://go.uber.org/mock) mocking framework to generate mocks. In order to maintain
consistency and to keep our mocks in sync with the source code, there are established conventions for how to create and
organize mocks for this project.

-   For each package, there should be a package `<package path>/mocks`
-   For each file in a package that contains an interface(s), there should be a `//go:generate` comment in the following format:
    ```
    //go:generate go run go.uber.org/mock/mockgen -destination=./mocks/filename.go -package=mocks . Comma,Separated,List,Of,Interfaces
    ```
-   For mocking a third party dependency update `cmd/api/src/vendormocks/vendor.go` with a new `//go:generate` comment in the following form:
    ```
    //go:generate go run go.uber.org/mock/mockgen -destination=./{package path}/mock.go -package={package basename} {package} Comma,Separated,List,Of,Interfaces
    ```

By following these conventions, mocks can be kept in sync by running `just go generate ./...`

# Dependencies

## Go

To use 3rd-party tooling written in golang, you must target the `go.tools.mod` file using the `-modfile` flag. For example,
to add a new dev dependency you would execute `go get -modfile go.tools.mod some.com/3rd-party/tool@v1.2.3`.

## How do I use a dev dependency?

To use a dev dependency, it is best to temporarily set the `GOBIN` environment variable to `${PROJECT_ROOT_PATH}/bin` and
even better to wrap the tool in a script of some sort to more easily return the shell environment back to its original state.
This will ensure that everyone is using the same version of the tool without having to vendor it in our VCS.

```bash
#!/usr/bin/env bash

readonly PROJECT_ROOT_PATH="$(dirname $(realpath ${0}))/path/to/project/root"

export GOBIN="$PROJECT_ROOT_PATH/bin"
$GOBIN/myDevTool "$@"
```

## NodeJS

This project uses [Yarn 3](https://yarnpkg.com/) for dependency management.

### To install all project dependencies

```bash
$ yarn
```

### To add/update a specific dependency

```bash
$ yarn add <package_name>@<version>
```

### To add/update a dev dependency

```bash
$ yarn add -D <package_name>@<version>
```

### To view/update outdated modules

```bash
$ yarn upgrade-interactive
```

## How do I use a NodeJS dev dependency?

To use a dev dependency, it is best to use it in the `scripts` section of the `package.json`. Doing so allows
contributors to use the tool without:

-   needing to globally install it
-   accidentally using the incorrect version
-   needing to use the relative path to the new tool (e.g. - `./node_modules/.bin/<dev tool>`).

As an example:

```json
{
    ...
    "scripts": {
        "cool-tools": "cool-tools",
        ...
    }
    ...
}
```

Usage:

```bash
$ yarn cool-tools [tool args/flags]
```

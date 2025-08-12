---
description: OpenAPI Spec Guide documentation
title: OpenAPI Spec Guide
---

# Introduction
The BloodHound team maintains an OpenAPI spec document (currently versioned 3.0.3) that drives several components. The source for this package lives in the `openapi` package at https://github.com/SpecterOps/BloodHound/tree/main/packages/go/openapi. This guide is meant to help understand how our spec source is structured and the general guidelines expected for documentation additions and changes when authoring pull requests.

If you are unfamiliar with OpenAPI Spec, please start by checking out the following resources:
- https://learn.openapis.org/ (fantastic beginner tutorial)
- https://spec.openapis.org/oas/v3.0.3 (the spec version we use)

# Tooling
The following sections outline the required and recommended tooling for development involving changes to the spec source code.

## `just`
This is a required tool for most development tasks within BloodHound. For the purposes of dealing with our spec, the `just gen-spec` command will parse the `openapi.yaml` source code and generate the `openapi.json` file. 

## Redoc
We use Redoc for validating and compiling the spec. The above `just` command, as well as several other places, uses `npx` to pull the `@redocly/cli` locally for usage.

## Editors/Plugins
Some editors have great options for editing our OpenAPI spec. And even if you aren't editing the spec, maybe you're working on a feature or integration and would like to view a rendered version of the API referenece, the tools below can be a huge help.

### JetBrains
JetBrains has built-in support for both editing and previewing OpenAPI specs.

### VSCode
VSCode does not have built-in support for OpenAPI, but can be added easily using a couple of recommended plugins. For editing and validating, our preferred plugin is `redocly.openapi-vs-code`. This will also add a preview option to VSCode, but unfortunately this functionality requires a Redoc account and API key to function correctly, so instead we prefer `zoellner.openapi-preview` for that feature. Once installed, you can open the Command Palette and type `OpenAPI preview`.

## Render HTML Doc
For those who are working on integrations or other features and would like to render the API Doc for easy exploration, here are a few scratch files I keep locally. You only need to save the code into an HTML file and open it in your browser to see the result. Each one uses a different rendering tool (Redoc/Stoplight Elements/Scalar) and they all have pros & cons. Try each one and see what you like best.

### Scalar by scalar.com
```html
<!doctype html>
<html>
<head>
    <title>Scalar API Reference</title>
    <meta charset="utf-8" />
    <meta
        name="viewport"
        content="width=device-width, initial-scale=1" />
</head>
<body>
<script
    id="api-reference"
    data-url="https://raw.githubusercontent.com/SpecterOps/BloodHound/main/packages/go/openapi/doc/openapi.json"></script>
<script src="https://cdn.jsdelivr.net/npm/@scalar/api-reference"></script>
</body>
</html>
```

### Elements by stoplight.io
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Elements API Reference</title>
    <script src="https://unpkg.com/@stoplight/elements/web-components.min.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/@stoplight/elements/styles.min.css">
</head>
<body>
<elements-api
    apiDescriptionUrl="https://raw.githubusercontent.com/SpecterOps/BloodHound/main/packages/go/openapi/doc/openapi.json"
    router="hash"
/>
</body>
</html>
```

### Redocly by redoc.com
```html
<!DOCTYPE html>
<html>
<head>
    <title>Redoc</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">
    <style>
        body { margin: 0; padding: 0; }
    </style>
</head>
<body>
<redoc spec-url='https://raw.githubusercontent.com/SpecterOps/BloodHound/main/packages/go/openapi/doc/openapi.json'></redoc>
<script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"> </script>
</body>
</html>
```

# Development
Our OpenAPI spec package has three main parts:
- The source code (.yaml files)
- The compiled spec (openapi.json)
- The http handler (docs.go)

The compiled spec is generated from the source code and it is the file we serve on the BloodHound API at `api/v2/spec`. This is a single file, and while we could just maintain this directly, it would be much more difficult to navigate and work with. Instead, we have opted to use yaml as our main source language and split the parts of the spec into different files using `$ref`s. When authoring changes the modify the API, it is required that the documentation source is also updated as well to make source our spec always reflects the reality of the API. If you happen to find that something is improperly documented, please [open an issue](https://github.com/SpecterOps/BloodHound/issues).

## Source Layout
In the openapi package's `src` folder, you will find the main `openapi.yaml` file and several other folders. The openapi.yaml file is the main entry point and the other folders are for holding specific related pieces of the overall spec. Looking inside these folders, you may notice there are no further nest subdirectories. The reason for this is that some OpenAPI tools use file names as unique identifiers when piecing the spec together. In larger projects, this can result in some files having identical names in different directories, thus causing errors. To solve this, we use dot-notation to help organize files into an hierarchy. For example, lets look at a handful files in the `schemas` folder:
- api.error-wrapper.yaml
- api.params.query.limit.yaml
- enum.client-type.yaml
- model.asset-group.yaml
- model.components.int64.id.yaml

Using dot-notation, we can organize related schemas, similar to organizing files into folders. In this example, we could imagine an `api` folder that holds schemas that are related to API concerns, such as the generic `error-wrapper` we use for API errors. It could also be further broken up into more specific concerns. `api.params.query.limit.yaml` denotes that it is (most broadly) a general API concern, it is a param(eter) schema, it's more specifically a query parameter, and the name of the parameter is limit. We also use `enum.*` to denote enumeration schemas, and have helper types like `null.*`. Another very populated group is `model.*`, which has specific models as well as model components under `model.component.*`, like timestamps and ID types. This pattern is replicated in the `paths` and `parameters` folder as well.

### Parameters
These files describe the [Parameter Objects](https://spec.openapis.org/oas/v3.0.3#parameter-object). The are generally notated by whether they are a query, path, or header param, with some more specific options for common special named params. Parameters with complex/shared schemas may also have a reference to a `schema` file.

### Schemas
These files describe [Schema Objects](https://spec.openapis.org/oas/v3.0.3#schema-object). As stated in the example above, these schemas may be general API concerns, special non-trivial types, and application models (entities). The most common use case is for defining application models. The models should match the definition described in Go code. In some cases, models can be used for requests and responses. Some people may choose to define a special response schema and special request schema for each entity, but this creates a lot of duplicate definitions and can be solved in a better way. Let's imagine we have the following User model:

```go
type User struct {
    ID int
    UpdatedAt time.Time
    Deleted bool
    Name string
    Password string
    Email string
}
```

This is how the model should be defined in the schema, but there are some fields in this model that are only usable is specific instances. For example, ID, UpdatedAt, and Deleted should not be present or usable for requests because we don't allow the user to update those fields. As for responses, we do want to include those fields, but we don't want to return the Password hash field in responses. Rather than creating a `user.yaml` schema, a `user-request.yaml` schema, and a `user-response.yaml` schema, we can instead add `readOnly` and `writeOnly` flags to those fields. ID, UpdatedAt, and Deleted would be flagged as `readOnly: true`, hiding it from request bodies, and the Password field would be flagged as `writeOnly: true`, hiding it from response bodies. 

There are also cases where a request might be very specially crafted and does not match the model. Because this is a special and unique instance, it should be defined within the `path` file inline, rather than creating a `schema` file for it. The same goes for responses which may return an array of models. Rather than create a specific response `schema` that has a top level array, it is better to describe the response array inline in the `path` file and then ref the model file there.

You may also notice the use of `allOf`. This is a special property of OpenAPI schema that allows you to merge multiple schemas together (aka composition). The most common use for this is for defining a model with an ID and timestamp fields by merging `model.components.int64.id.yaml`, `model.components.timestamps.yaml`, and the specific model properties. This way you don't have to manually redefine the id, created_at, updated_at, and deleted_at fields on every model schema you create.

### Responses
These files describe [Response Objects](https://spec.openapis.org/oas/v3.0.3#response-object). These files have been genericized to cover most situations not related to a 200 response. There are also a few versions of 2xx responses for special cases, such as "no content" or non-JSON responses.

### Paths
These files describe [Path Item Objects](https://spec.openapis.org/oas/v3.0.3#path-item-object). The file naming convention here also follows the dot-notation followed above (instead of subdirectories), but with a slight difference. Each file is named using this convention:
```
paths/{tag-group}.{url.path.with.params}.yaml
```
This may seem strange at first, but there is a reason for it. The main part of the file name is based on the endpoint's URL path, including any URL params that may exist. This makes it easy to identify the path file you are looking for if you know the URL of the endpoint you are working with, and it also helps visually identify errors in path refs in the main openapi.yaml file. Prepended to this is a tag group. OpenAPI spec document renderers have the ability to group different endpoints based on tags. Prepending a tag nickname to each endpoint with similar tags helps to visually identify which path files are in the same group. To help understand this, here is a breakdown of a few path file names:
```yaml
/api/v2/spec:
  tag: API Info (api-info)
  url: spec
  filename: api-info.spec.yaml
/api/v2/version:
  tag: API Info (api-info)
  url: version
  filename: api-info.version.yaml
/api/v2/bloodhound-users/{user_id}:
  tag: BloodHound Users (bh-users)
  url: bloodhound-users/{user_id}
  filename: bh-users.bloodhound-user.id.yaml
/api/v2/bloodhound-users/{user_id}/mfa:
  tag: BloodHound Users (bh-users)
  url: bloodhound-users/{user_id}/mfa
  filename: bh-users.bloodhound-users.id.mfa.yaml
```

When working on a path file, it may have one or more operations based on what HTTP verbs the endpoint supports. For example, an endpoint for `/users` may have a GET operation for retrieving a list of users, and a POST operation for creating a new user. An endpoint for `/users/{id}` might have 3 operations; GET for retrieving the user, PUT for updating the user, and DELETE for removing the user. All of these operations are defined in the same path file. For paths which have a URL parameter and multiple operations, it is best to define the path param at the top of the file, rather than replicating the definition for each operation individually. This is also true for parameters like the Prefer header. Each operation must have a unique `operationId`, a string that roughly describes what the VERB+ENDPOINT does. Think of this like a function name:  GetUser, CreateUser, DeleteUser, etc.

Some common parameters you may see:
```yaml
# For your copy-paste convenience:

# Path level
- $ref: './../parameters/header.prefer.yaml'
- $ref: './../parameters/path.object-id.yaml'

# Operation level
- $ref: './../parameters/query.created-at.yaml'
- $ref: './../parameters/query.updated-at.yaml'
- $ref: './../parameters/query.deleted-at.yaml'
- $ref: './../parameters/query.skip.yaml'
- $ref: './../parameters/query.limit.yaml'
  
# Filter params with predicates
- name: sort_by
  in: query
  description: Sortable columns are [list_columns_here].
  schema:
      $ref: './../schemas/api.params.query.sort-by.yaml'
- name: [string_param_name]
  in: query
  schema:
    $ref: './../schemas/api.params.predicate.filter.string.yaml'
- name: [int_param_name]
  in: query
  schema:
    $ref: './../schemas/api.params.predicate.filter.integer.yaml'
```

When defining responses for an operation, make sure to define all expected responses an endpoint may return. In most cases, this will be one success case, and one or more error cases (different status codes). The way to do this is to look at the handler and check each status code returned for all code paths. Also consider more than just the possible status' that the handlers return. Most endpoints also have auth middleware which can return `401` and `403` before ever making it to the handler, as well as a rate limit middleware that can return a `429`. It is important to capture these cases so the user won't be surprised by unexpected responses.

Most operations should have a custom 2xx success response defined inline (some may use predefined 2xx responses), but most error responses can use generic error response file refs. Some common error responses in many operations:
```yaml
# For your copy-paste convenience:
400:
  $ref: './../responses/bad-request.yaml'
401:
  $ref: './../responses/unauthorized.yaml'
403:
  $ref: './../responses/forbidden.yaml'
404:
  $ref: './../responses/not-found.yaml'
429:
  $ref: './../responses/too-many-requests.yaml'
500:
  $ref: './../responses/internal-server-error.yaml'
```

## Validation & Compilation
Once you have completed your updates to the OpenAPI source, you will need to validate and compile the JSON spec. The reason for this is because editing and maintaining a spec is easiest with multi-file yaml, but most OpenAPI tooling works best when the spec doc is in single file JSON format. While many tools support multi-file or yaml, they tend to have different opinions about how to specifically implement those features and can result in very different results across tools. We have opted to use Redocly for most of our validation and compilation operations. In JetBrains, validation is built in and the editor will let you know if something is incorrect. For VSCode, the Redocly plugin will alert you when it finds issues. Assuming your editor is happy, the next step is to compile the spec. You can use `just gen-spec`, but this will only validate/compile the spec. This is mostly useful for when you want to test that the spec works with the BloodHound API Explorer page (which is something you should do), but when finalizing work for a PR, it is recommended that you run `just prepare-for-codereview`.

# Comments & Concerns
If you find that this documentation is out of date, or you find OpenAPI spec docs that are out of date or don't match the behavior of an endpoint, please create an issue in the repo and let us know!
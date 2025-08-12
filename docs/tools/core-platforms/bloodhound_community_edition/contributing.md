---
description: Contributing documentation
title: Contributing
---

## Getting started

Are you really digging BloodHound Community Edition and looking to give back to the project? Lucky for you there are numerous ways to help! 
Here are some recommendations to help get you started.

* Peruse the [issue tracker](https://github.com/SpecterOps/BloodHound/issues) on GitHub. This can be a great place to get started as it doesn't require much insider knowledge. Here's a few ideas that could help here.
  * Open a bug or feature request
  * Help others
* Enhance documentation
  * Fix errors or inconsistencies
  * Add documents for undocumented capabilities
* Write some code!
  * Fixing a bug that has been reported
  * Add a new feature
  * Enhance an existing feature

## Contributing Code

First, thank you so much for considering a code contribution to BloodHound Community Edition. We're very appreciative of anyone who offers to give back to a tool they find useful. It helps make BloodHound better for everyone.

The following are some general guidelines to follow while writing and submitting your PRs. Following these should make merging the PR faster and easier.

If you need to get you development environment set up you should check out the guide [here](https://github.com/SpecterOps/BloodHound/wiki/Development#running-the-development-environment).

If you're specifically looking to contribute to our documentation, check out our [Documentation Repo](https://github.com/SpecterOps/bloodHound-docs)!

### Before Opening an Issue or Pull Request

If a Pull Request is being planned, please ensure a GitHub issue has been opened first. All Pull Requests must be associated with a GitHub issue (or a Jira ticket for BHE team members), otherwise, it will be closed. The reasons for this are:

- Clear tracking of work related to specific issues
- The bug or feature may already be in progress internally
- Validation is needed to ensure the contribution fits the needs and scope of BHCE
- The engineering team will assist in refining the requirements and setting clear expectations

Once we have reviewed the issue internally, we will reach out to let you know everything is good to go. In some cases we may also provide feedback or suggest changes to the proposal as needed.

If you have any further questions about opening a Pull Request, please reach out to us in our [community slack](https://ghst.ly/BHSlack)!

### Git Configuration and Etiquette

All PR submissions will need to come from a separate branch from `main`. We recommend creating a personal fork of the BloodHound repo and creating the branch from there. This will allow you more control over your local environment.

Also, please ensure that you are branching off of the latest version of `main` from the `SpecterOps/BloodHound` repo. This will ensure everything is built on top of the latest code and also help reduce merge conflicts.

Please be aware, beginning in December 2024 any contribution made to BloodHound or its related projects will require its commits to be signed and verified by GitHub. For information on how to setup a signing key and to sign commits please reference the [GitHub documentation](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification). 

Lastly, we ask that you use brief, but detailed, commit messages when writing your code.

Commit messages should be in conventional commit style as described in the [Conventional Commits Guide RFC](../blob/main/rfc/bh-rfc-2.md).
Please take some time to review the guidelines in order to format your commits accordingly so that the work passes the associated pull request check. 

Adding well formatted and detailed commit messages will help with the review process as it will be easier to
see the reasoning and details included in a particular change. Another habit that will help the PR reviewer is authoring smaller, frequent commits as 
opposed to a giant single commit containing all of your changes.  

### PR Etiquette

#### Reviewers

If you are participating in the review of a PR then you should add yourself to the Reviewers list. It sends appropriate notifications to all reviewers when the PR author requests an additional review after making changes, so be sure to use that button within GitHub when you are ready for an additional look.

It should be noted that the presence of a reviewer on a PR should not dissuade others from also reviewing the PR. The more eyes the better.

If you will no longer be reviewing a PR for some reason, then please try to remember to remove yourself as a Reviewer.

#### Communication
GitHub should be viewed not just as a repository of code, but also as a repository of knowledge. PRs can contain a wealth of information and context on top of the code itself and comments within it. Ensuring that relevant information is captured within can serve as a great resource to our future selves and new engineers when trying to understand why something was implemented a certain way.

* PR descriptions should be sure to include a brief description of the features or fixes being added as well as any relevant context on why important decisions were made.

* Self-posting insight on specific pieces of code can provide valuable insight outside of code comments.

  * [Example](https://github.com/SpecterOps/BloodHound/pull/296#discussion_r1445318622)

* If additional related fixes were thrown into a PR be sure to call those out in the description. Avoid doing unrelated refactors within the same PR as this adds mental overhead. Instead, create a separate PR .

#### Labels
Please use the available labels on your PRs to help easily indicate state outside of the built-in GitHub statuses.

* [api](https://github.com/SpecterOps/BloodHound/labels/api) - This label is to easily identify that a PR contains changes to the backend API code. The goal is to provide an easy way for primarily backend engineers to select PRs to review.

* [blocked](https://github.com/SpecterOps/BloodHound/labels/blocked) - Apply this label if there is some factor preventing the PR from being merged.

* [help wanted](https://github.com/SpecterOps/BloodHound/labels/help%20wanted) - Use this label when you need help from an additional engineer. This could be to answer questions or just to get some extra hands to get the PR ready to go.

* [infrastructure](https://github.com/SpecterOps/BloodHound/labels/infrastructure) - This label is to easily identify that a PR contains changes to the infrastructure code, such as CI/CD or Docker. The goal is to provide an easy way for engineers who have a specialty in this area to select PRs to review.

* [work in progress](https://github.com/SpecterOps/BloodHound/labels/work%20in%20progress) - This label should be added to PRs that are still working through some issues or suggestions. The goal here is to indicate that the PR was initially considered complete, but significant additional work must be done before being ready for re-review.

  * The goal here is to avoid confusion with GitHub’s built-in statuses. After a PR is marked as “Approved” or “Changes Requested” the status will not update on the main /prs page. This can make it difficult to tell if it is looking for further review or if the author is still making changes.

* [user interface](https://github.com/SpecterOps/BloodHound/labels/user%20interface) - This label is to easily identify that a PR contains changes to the frontend UI code. The goal is to provide an easy way for primarily frontend engineers to select PRs to review.

* [tooling](https://github.com/SpecterOps/BloodHound/labels/tooling) - This label is for changesets that add/remove/update developer tooling (Docker Compose files, Beagle, St Bernard, GraphGen, etc).

### Code Style and Formatting

BloodHound CE follows standard Go [styling](https://google.github.io/styleguide/go/) and [formatting](https://go.dev/doc/effective_go) practices. Please ensure that `gofmt` is run against your code before pushing up the PR by running `gofmt -s -w` from the root directory. 

Alternatively, you can [install](https://pkg.go.dev/golang.org/x/tools/cmd/goimports) `goimports` which has some added functionality for tidying up dependencies along with the `gofmt` functionality.

### Testing

The entire BloodHound test suite will run against your PR once it is submitted. This includes Go unit tests, UI unit tests, and integration tests. All tests must pass for the PR to be landed. 

If you see test failures on GitHub and want to troubleshoot them locally you can run them using the instructions [here](https://github.com/SpecterOps/BloodHound/wiki/Development#testing)

Most importantly, please consider adding test coverage around the new feature or bug fix that you are contributing. This will ensure that this new code retains resiliency as the code-base shifts around.

### Logging Handling
There are five levels of logging in our codebase.  Below are each type and when they should be used.

**Debug:** Used for detailed diagnostic information that are only present in non-default configurations. 

**Info:** Used to log general information about the application's normal operations, indicating successful actions that don't require further attention.

**Warn:** Used to indicate potential issues or abnormal behavior that may not immediately cause a problem but could in the future. Warn logs highlight non-app-breaking conditions that may require attention but are not critical.

**Error:** Used when an issue occurs that prevents the application from performing a specific task or function correctly. The application can still continue to run, but something failed.

**Fatal:** Used only in cases where the application had to recover from a bad state or abandon significant work, typically during initialization steps or unrecoverable states. Reserved for critical errors that cause the application to crash or stop working entirely, these logs signal that immediate developer attention is needed.

### Documentation

Documentation that is easy to read and understand is key to ensuring your new feature gets used. There are a number of places where this documentation can be added. We'll leave it up to you to decide where the best location is.

Code comments are the first place to begin documentation. Function-level comments are always appreciated for any new functions that are added, especially library functions. The standard [Go Doc format](https://tip.golang.org/doc/comment) is preferred.
In-line comments are helpful for explaining why non-obvious code paths are used or walking through complex logic in a more human-readable way.

API updates should be documented in our OpenAPI specs located at `packages/go/openapi`. Please follow [OpenAPI v3.0.3](https://spec.openapis.org/oas/v3.0.3.html) specification standards when updating API documentation. More information can be on the [OpenAPI Spec Guide](https://github.com/SpecterOps/BloodHound/wiki/OpenAPI-Spec-Guide.

Lastly, if appropriate your feature may need to be documented on our official documentation page. Please [reach out](https://github.com/SpecterOps/BloodHound/wiki/Contact) to the BloodHound team to discuss further.

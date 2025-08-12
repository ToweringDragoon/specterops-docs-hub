---
description: Installation documentation
title: Installation
---

# Ghostwriter Installation

Ghostwriter is installed using [Docker Compose](https://docs.docker.com/compose/). Install Docker before proceeding.

## Ghostwriter Settings

Copy the examples in `.envs_template` to a new `.envs` within the Ghostwriter directory.

`mkdir .envs && cp .envs_template/.* .envs`

The `.envs` directory contains `.local` and `.production` directories. Each of these directories contains the same two files, `.django` and `.postgres`. These files manage the settings for Docker. Edit the `.django` file to add API keys and manage other options.

### API Configuration

One action Ghostwriter can perform is looking-up domain names and servers in VirusTotal. This uses web requests and a VirusTotal API key. If you do not have one, get a free API key from VirusTotal. Once you have your key, set `VIRUSTOTAL_API_KEY`.

### Slack Configuration

If you desire to use Slack with Ghostwriter, set `SLACK_ENABLE` to `True` and then configure a Slack Incoming WebHook.

You can also specify a username and emoji for the bot. Emojis must be set using Slack syntax like `:sheep:`. The username can be anything you could use for a Slack username. The emoji will appear as the bot's avatar in channels.

The alert target is the message target. You can set this to a blank string, e.g. `''`, but it's useful for targeting users, aliases, or @here/@channel. They must be written as `<!here>`, `<!channel>`, or `<@username>` for them to work as actual notification keywords.

Finally, set the target channel. This might be your `#general` or some other channel. This is the global value that will be used for all messages unless a project-specific channel is supplied. When a new project is created, users have an option to provide a Slack channel to be used for project-related notifications instead of the global channel.

Other notification options may be added in the future. Email and services such as Pushover are being considered. That said, you can add your own notification mediums and tasks in `tasks.py`. See [Background Tasks](https://github.com/GhostManager/Ghostwriter/wiki/Background-Tasks) for more information.

### Company Information

At the bottom of of the settings you will find some values for your company/team. Fill these in to customize reporting. You need to provide at least a company name. Set values to blanks if you do not want to use them (e.g. `COMPANY_TWITTER = ''`).

## Building the Container

Once you have `.envs` setup, check Docker to make sure it is running. Then start the Docker container using your desired configuration (local development or production deployment):

**Local / Development Deployment**

`docker-compose -f local.yml up -d`

**Production Deployment**:

`docker-compose -f production.yml up -d`

### Updating Your Container After a Code Update

If you have already built Ghostwriter before and have made custom changes or pulled down new code, update and rebuild the container using these four commands:

`docker-compose -f local.yml stop; docker-compose -f local.yml rm -f; docker-compose -f local.yml build; docker-compose -f local.yml up -d`

## Next Steps

Move on the the [Database Setup](https://github.com/GhostManager/Ghostwriter/wiki/Database-Setup).
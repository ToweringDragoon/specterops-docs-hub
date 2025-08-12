---
description: Production documentation
title: Production
---

# Moving to Production

Eventually you will want to move Ghostwriter from a development server to a production server. 

Even though Ghostwriter *could* be run in developer mode, it is much better to use HTTPS and take some of the workload off of Django when it comes to hosting files.

## Adjusting Production setting

Start your move to production by opening `.envs\.production\.django`. The `SECRET_KEY` variable is set to `changeme`. Generate a new value and drop in the new key. It is usually something like `cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag`.

The default configuration will host Ghostwriter on *0.0.0.0:80* with HTTP. To enable HTTPS on port 443, or change the listening address or port, open `compose/production/nginx/nginx.conf`. Comment out the HTTP configuration and uncomment the commented lines at the bottom of the file for HTTPS. You can make changes to this configuration file like you would for any nginx configuration.

Production deployments use separate settings from local deployments, so make changes to `.envs/.production/.django` and `.../.postgres` as desired. You can keep separate settings for your local/development and production deployments.

## Deploy to Production

Deploy Ghostwriter in production mode using Docker Compose and the `production.yml` file.

`docker-compose -f production.yml up -d`
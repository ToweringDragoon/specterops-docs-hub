---
description: Scheduled Tasks documentation
title: Scheduled Tasks
---

# Schedule Tasks

Visit the Django Q database from the admin panel to access the Scheduled tasks. You may wish to create a scheduled task to automatically release domains at the end of a project. Shepherd has a task for this, `tasks.release_domains`, which you can schedule whenever you please, like every morning at 01:00.

Any task can be scheduled from this admin panel. Tasks added to `tasks.py` can be referenced with a `tasks.*` prefix on the function name. Then provide arguments and/or kwargs, set a time, and schedule type (e.g. One Time, Daily, Weekly, etc.) and save it.

![scheduled-tasks-domain-release](https://github.com/GhostManager/Ghostwriter/raw/master/DOCS/screenshots/scheduled-tasks-domain-release.png)

## Making Changes to Tasks.py

You can edit `tasks.py` on the fly for debugging and testing. If you make a big change, such as adding a new function or renamng an existing function, you must restart Q cluster before you will be able to use the new function. Function names are imported from `tasks.py` when `python manage.py qcluster` is run.

## Scheduling a Task

Tasks are scheduled in the Django admin panel under Django Q and Scheduled Tasks. Add a new task, give the task a name, and tell it which function to run. Functions must be prefixed with `tasks.` To tell Django Q to pull the functions from `tasks.py`. The final requirement is a schedule. Tasks can be run once or repeatedly (e.g. minutes, hourly, daily, weekly).

You can provide arguments for the functions as needed. Ghostwriter's scheduled tasks do not require arguments, but some have optional arguments. For example, the `scan_servers()` function accepts a `active_only` argument to restrict scanning only to servers that have been checked out for a project.

## Included Tasks

The following information is for Ghostwriter's provided tasks:

### Release Domains

The `tasks.release_domains` function checks if the currently checked out domain names are due to be released. It sends a Slack message if Slack is enabled and the domain's release date is either tomorrow or today. If the release date is today the domain is also released back into the pool.

### Release Servers

The `tasks.release_servers` function checks if the currently checked out servers are due to be released. It sends a Slack message if Slack is enabled and the server's release date is either tomorrow or today. If the release date is today the server is also released back into the pool.

### Check Domains

The `tasks.check_domains` function checks each domain name to update categorization. The function uses the DomainCheck tool. More information is available here:

https://github.com/GhostManager/DomainCheck

### Update DNS

The `tasks.update_dns` function updates Ghostwriter's records of each domain's current DNS records using `dnspython` and constructed DNS queries.

### Archive Projects

The `tasks.archive_projects` function collects a list of projects marked as complete and checks if the project's end date is 90 days (default) in the past. Completed projects older than the specified number of days are archived. This process mostly affects reports attached to the project. Each report is marked as complete (if not already marked as such) and marked as archived. All report types are generated and rolled into a zip file with copies of all of the evidence files. Finally, the evidence files are deleted. The archive files can be browsed and downloaded as needed.

### Scan Servers

The `tasks.scan_servers` function collects a list of static servers catalogued in Ghostwriter, scans them for open ports using `python-nmap`, and records the results (the open port number and protocol). Then the results are compared to previous results. If Slack is enabled, Ghostwriter will send a Slack notification if a new port is found to be open.

This function focuses on the static servers because these servers are assumed to be owned by you and used for command and control (C2). These servers should not have open services exposed to the whole internet, so this is meant to alert you of open ports accessible outside of your management ranges. Transient servers (i.e. virtual private servers, cloud servers) are likely to have open ports for phishing webpages and C2 redirection.

*Important Note:* If you will be using this task the Q cluster needs to be started using as an administrator / root. Administrative privileges are required for the TCP SYN scan.

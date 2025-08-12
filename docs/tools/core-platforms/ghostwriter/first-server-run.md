---
description: First Server Run documentation
title: First Server Run
---

# Start Django

The first time you use Ghostwriter, a super user must  be created to access the admin panel and create new users. This is the administrator of all of Django, so set a strong password and document it in a password vault somewhere.

To create a superuser, run:

`docker-compose -f local.yml run --rm django python manage.py createsuperuser`

Visit *http://SERVER_IP:8000/admin* to view the admin panel and login using the superuser.

If you are deploying using the *production.yml*, the server will be listening on port *0.0.0.0:80*.

## Creating New Users

You may create users using the admin panel or ask users to sign-up using `/accounts/signup`. Filling out a complete profile is recommended. Ghostwriter will make use of full names for displaying user actions and email addresses can be helpful for custom tasks that send email notifications.

**Note**: Django usernames are weirdly case sensitive, so all lowercase is recommended to avoid confusion later.

### Managing Sign-up

The account sign-up can be disabled if you prefer to create accounts manually or just shut it off after a set period of time.

### Password Changes

Once a user has been created, the username and password can be handed off to the intended user. That person may then login and click their avatar icon in the upper-right corner to change their password and upload a custom avatar (if they so desire).

If users are signing-up, then hopefully they know their password. Password resets can be requested using email addresses.

## Next Steps

Use Ghostwriter for some time and see if everything is working properly. If you intend to make modifications to the codebase now is the time to do that.

When you are ready to move from a development server to a production server continue on to [Production](https://github.com/GhostManager/Ghostwriter/wiki/Production).

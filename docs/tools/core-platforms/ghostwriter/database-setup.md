---
description: Database Setup documentation
title: Database Setup
---

# Database Setup

Before Ghostwriter can be used, you must populate the models with the provided Django fixtures. Run this command:

`docker-compose -f local.yml run --rm django /seed_data`

This populates models like the domain status types and project types. This data must be inserted into the models before proceeding. If you try to use Ghostwriter without these values you will find you cannot do very much and will encounter errors.

### Customizing Fixtures

In general, it is best not to edit the fixtures. Ghostwriter expects some values to be as they appear in the fixtures, such as finding severity categories. There are some fixtures you can edit or expand. Each sub-application has a "fixtures" folder with an `initial.json` file where the fixtures live.

In the Reporting fixture file you can add or edit the finding types. The initial values includes Network, Wireless, Mobile, Web, and Physical.

The Rolodex fixture file has multiple types that can be modified. Feel free to add or edit the project types and project roles. Project types represent the types of projects (e.g. red team, penetration test). The project roles apply to humans assigned to projects (e.g. assessment lead).

The Shepherd fixture file contains server providers and server roles that can be edited. Statuses should be left alone.

**Note:** The severity ratings in Ghostwriter are customizable; however, some of the templates expect to find ratings that match the Critical, High, Medium, Low, and Informational ratings in the provided fixture file. If the ratings are changed there are several HTML template files that will also need to be edited.

#### Fixture Layout

If you add a fixture, be careful to increment the `pk` value (the primary key). If you do not, your addition will just overwrite the preceding fixture with the matching `pk`. All fixtures should look something like this:

```json
{
    "model": "ghostwriter.findingtype",
    "pk": 5,
    "fields": {
        "finding_type": "Mobile"
    }
}
```

## Next Steps

Once the fixtures have been loaded successfully, you are ready to move on to your [First Server Run](https://github.com/GhostManager/Ghostwriter/wiki/First-Server-Run).

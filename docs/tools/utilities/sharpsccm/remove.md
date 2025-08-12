---
description: remove documentation
title: remove
---

# Using the "remove" Command Group
This documentation was last updated on 10/26/23 by Chris Thompson (@_Mayyhem). Please refer to the output of the `--help` option for each command for the most up-to-date usage information.

# Description
A group of commands that deletes objects by contacting an SMS Provider via WMI

# Usage
```
SharpSCCM remove [command] [options]

Options:
  -sms, --sms-provider <sms-provider>  The IP address, FQDN, or NetBIOS name of the SMS Provider to connect
                                       to (default: the current management point of the client running
                                       SharpSCCM)
  -sc, --site-code <site-code>         The three character site code (e.g., "PS1") (default: the site code
                                       of the client running SharpSCCM)
  --debug                              Print debug messages for troubleshooting
  --no-banner                          Do not display banner in command output
  -?, -h, --help                       Show help and usage information
```

# Subcommands
```
Commands:
  application <name>  Delete a specified application by contacting a management point via WMI
  collection          Delete a specified collection by contacting a management point via WMI
  collection-member   Remove a device from a collection by by contacting a management point via WMI and adding a collection rule to explicitly exclude it
  collection-rule     Remove a device from a collection rule by contacting a management point via WMI
  deployment <name>   Delete a deployment of a specified application to a specified collection by contacting a management point via WMI
  device <guid>       Remove a device from SCCM by contacting a management point via WMI
```

---

# remove application
### Description
Delete a specified application by contacting an SMS Provider via WMI

### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator
  - Application Author
  - Operations Administrator

### Usage
```
SharpSCCM remove application <name> [options]

Arguments:
  <name>  The LocalizedDisplayName of the application to delete

Options:
  -sms, --sms-provider <sms-provider>  The IP address, FQDN, or NetBIOS name of the SMS Provider to connect
                                       to (default: the current management point of the client running
                                       SharpSCCM)
  -sc, --site-code <site-code>         The three character site code (e.g., "PS1") (default: the site code
                                       of the client running SharpSCCM)
  --debug                              Print debug messages for troubleshooting
  --no-banner                          Do not display banner in command output
  -?, -h, --help                       Show help and usage information
```
### Examples
Remove the application named `app01`:
```
.\SharpSCCM.exe remove application app01

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Found the app01 application
[+] Deleted the app01 application
[+] Querying for applications named app01
[+] No remaining applications named app01 were found
[+] Completed execution in 00:00:02.4554925
```

---

# remove collection
### Description
Delete a specified collection by contacting an SMS Provider via WMI
    
### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator
  - Infrastructure Administrator
  - Operations Administrator
  - Security Administrator

### Usage
```
SharpSCCM remove collection [options]

Options:
  -i, --collection-id <collection-id>      The CollectionID of the collection to remove (e.g., "PS100020"
  -n, --collection-name <collection-name>  The name of the collection to remove
  -sms, --sms-provider <sms-provider>      The IP address, FQDN, or NetBIOS name of the SMS Provider to
                                           connect to (default: the current management point of the client
                                           running SharpSCCM)
  -sc, --site-code <site-code>             The three character site code (e.g., "PS1") (default: the site
                                           code of the client running SharpSCCM)
  --debug                                  Print debug messages for troubleshooting
  --no-banner                              Do not display banner in command output
  -?, -h, --help                           Show help and usage information
```
### Examples
Remove the collection with CollectionID `PS10005D`:
```
.\SharpSCCM.exe remove collection -i PS10005D

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Deleted the devicecollection collection (PS10005D)
[+] Querying for the devicecollection collection (PS10005D)
[+] Found 0 collections matching the specified CollectionID
[+] No remaining collections named devicecollection with CollectionID PS10005D were found
[+] Completed execution in 00:00:00.7964524
```

---

# remove collection-member
### Description
Remove a device from a collection by by contacting an SMS Provider via WMI and adding a collection rule to explicitly exclude it    

### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator
  - Infrastructure Administrator
  - Operations Administrator
  - Security Administrator

### Usage
```
SharpSCCM remove collection-member [options]

Options:
  -d, --device <device>                    The name of the device to exclude from the specified collection
  -i, --collection-id <collection-id>      The CollectionID of the collection to exclude the resource from
                                           (e.g., "PS100020"
  -n, --collection-name <collection-name>  The name of the collection to exclude the specified device or
                                           user from
  -t, --collection-type <device|user>      The type of the collection ("device" or "user")
  -u, --user <user>                        The UniqueUserName of the user to exclude from the specified
                                           collection, including escaped backslashes (e.g.,
                                           "APERTURE\\cave.johnson")
  -r, --resource-id <resource-id>          The unique ResourceID of the device or user to exclude from the
                                           specified collection
  -w, --wait-time <wait-time>              The time (in seconds) to wait for the excluded collection to
                                           populate before displaying updated collection members (default:
                                           15 seconds)
  -sms, --sms-provider <sms-provider>      The IP address, FQDN, or NetBIOS name of the SMS Provider to
                                           connect to (default: the current management point of the client
                                           running SharpSCCM)
  -sc, --site-code <site-code>             The three character site code (e.g., "PS1") (default: the site
                                           code of the client running SharpSCCM)
  --debug                                  Print debug messages for troubleshooting
  --no-banner                              Do not display banner in command output
  -?, -h, --help                           Show help and usage information
```
### Examples
Remove the `CAVE-JOHNSON-PC` device from the `devicecollection` collection by adding a collection rule to explicitly exclude it:
```
.\SharpSCCM.exe remove collection-member -d CAVE-JOHNSON-PC -n devicecollection

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Found the devicecollection collection (PS10005D)
[+] Found a device named CAVE-JOHNSON-PC in the collection
[+] Found resource named CAVE-JOHNSON-PC with ResourceID 16777274
[+] Creating new device collection: device_f4641149-3062-427a-9e35-b59c20dd2a19
[+] Successfully created collection
[+] Found resource named CAVE-JOHNSON-PC with ResourceID 16777274
[+] Added CAVE-JOHNSON-PC 16777274 to device_f4641149-3062-427a-9e35-b59c20dd2a19
[+] Waiting for new collection member to become available...
[+] New collection member is not available yet... trying again in 5 seconds
[+] Successfully added CAVE-JOHNSON-PC 16777274 to device_f4641149-3062-427a-9e35-b59c20dd2a19
[+] Added rule to exclude resource from devicecollection
[+] Waiting 15s for collection to populate
[+] Found the devicecollection collection (PS10005D)
[+] Executing WQL query: SELECT * FROM SMS_FullCollectionMembership WHERE CollectionID='PS10005D'
[+] No instances of SMS_FullCollectionMembership meeting the specified criteria were found, or you do not have permission to query them
[+] Found 0 members in devicecollection (PS10005D)
[+] Completed execution in 00:00:28.7425216
```

---

# remove collection-rule
### Description
Remove a device from a collection rule by contacting an SMS Provider via WMI (currently supports Query type rules only)
    
### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator
  - Infrastructure Administrator
  - Operations Administrator
  - Security Administrator

### Usage
```
SharpSCCM remove collection-rule [options]

Options:
  -i, --collection-id <collection-id> (REQUIRED)  The CollectionID of the collection to remove the resource
                                                  from (e.g., "PS100020")
  -q, --query-id <query-id> (REQUIRED)            The QueryID of the rule to remove from the specified
                                                  collection
  -sms, --sms-provider <sms-provider>             The IP address, FQDN, or NetBIOS name of the SMS Provider
                                                  to connect to (default: the current management point of
                                                  the client running SharpSCCM)
  -sc, --site-code <site-code>                    The three character site code (e.g., "PS1") (default: the
                                                  site code of the client running SharpSCCM)
  --debug                                         Print debug messages for troubleshooting
  --no-banner                                     Do not display banner in command output
  -?, -h, --help                                  Show help and usage information
```
### Examples
Remove the rule with a `QueryID` value of `2` from the `PS10004C` collection:
```
.\SharpSCCM.exe remove collection-rule -i PS10004C -q 2

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Found matching rule for CollectionID PS10004C
-----------------------------------
CollectionRule
-----------------------------------
QueryExpression: select SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,SMS_R_SYSTEM.SMSUniqueIdentifier,SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM.Client from SMS_R_System where SMS_R_System.MDMDeviceCategoryID = "613E03DB-8D34-4C66-AB13-D142E2C714C2"
QueryID: 2
RuleName: mycat
-----------------------------------
[+] Successfully removed collection rule
[+] Completed execution in 00:00:01.1073859
```

---

# remove deployment
### Description
Delete a deployment of a specified application to a specified collection by contacting an SMS Provider via WMI
    
### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator
  - Application Deployment Manager
  - Operations Administrator

### Usage
```
SharpSCCM remove deployment <name> [options]

Arguments:
  <name>  The exact AssignmentName of the deployment

Options:
  -sms, --sms-provider <sms-provider>  The IP address, FQDN, or NetBIOS name of the SMS Provider to connect
                                       to (default: the current management point of the client running
                                       SharpSCCM)
  -sc, --site-code <site-code>         The three character site code (e.g., "PS1") (default: the site code
                                       of the client running SharpSCCM)
  --debug                              Print debug messages for troubleshooting
  --no-banner                          Do not display banner in command output
  -?, -h, --help                       Show help and usage information
```
### Examples
Remove the deployment with an `AssignmentName` equal to `app01_PS10004C_Install`:
```
.\SharpSCCM.exe remove deployment app01_PS10004C_Install

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Found the app01_PS10004C_Install deployment
[+] Deleted the app01_PS10004C_Install deployment
[+] Querying for deployments of app01_PS10004C_Install
[+] No remaining deployments named app01_PS10004C_Install were found
[+] Completed execution in 00:00:00.8722912
```

---

# remove device
### Description
Remove a device from SCCM by contacting an SMS Provider via WMI
    
### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator
  - Infrastructure Administrator
  - Operations Administrator

### Usage
```
SharpSCCM remove device <guid> [options]

Arguments:
  <guid>  The GUID of the device to remove (e.g., "GUID:AB424B0D-F582-4020-AA26-71D32EA07683"

Options:
  -sms, --sms-provider <sms-provider>  The IP address, FQDN, or NetBIOS name of the SMS Provider to connect
                                       to (default: the current management point of the client running
                                       SharpSCCM)
  -sc, --site-code <site-code>         The three character site code (e.g., "PS1") (default: the site code
                                       of the client running SharpSCCM)
  --debug                              Print debug messages for troubleshooting
  --no-banner                          Do not display banner in command output
  -?, -h, --help                       Show help and usage information
```
### Examples
Remove the device with SMS ID `GUID:001B2EE1-AE95-4146-AE7B-5928F1E4F396`:
```
.\SharpSCCM.exe remove device GUID:001B2EE1-AE95-4146-AE7B-5928F1E4F396

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Deleted device with SMSUniqueIdentifier GUID:001B2EE1-AE95-4146-AE7B-5928F1E4F396
[+] Completed execution in 00:00:01.2899596
```
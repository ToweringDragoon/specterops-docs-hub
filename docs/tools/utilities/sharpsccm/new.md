---
description: new documentation
title: new
---

# Using the "new" Command Group

This documentation was last updated on 10/26/23 by Chris Thompson (@_Mayyhem). Please refer to the output of the `--help` option for each command for the most up-to-date usage information.

### Description
A group of commands that create new objects by contacting an SMS Provider via WMI

### Usage
```
  SharpSCCM new [command] [options]

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

### Subcommands
```
  application        Create an application by contacting an SMS Provider via WMI
  collection         Create a collection of devices or users by contacting an SMS Provider via WMI
  collection-member  Add a device to a collection by contacting and SMS Provider via WMI
  deployment         Create an assignment to deploy an application to a collection by contacting an SMS Provider via WMI 
  device             Create a new device record and obtain a reusable certificate for subsequent requests (experimental)
```

---

# new application

### Description
Create an application by contacting an SMS Provider via WMI

### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator
  - Application Author
  - Operations Administrator

### Usage
```
  SharpSCCM new application [options]

Options:
  -n, --name <name> (REQUIRED)         The name of the new application
  -p, --path <path> (REQUIRED)         The local or UNC path of the binary/script the application will
                                       execute (e.g., "C:\Windows\System32\calc.exe",
                                       "\\site-server.domain.com\Sources$\my.exe
  -r, --run-as-user                    Execute the application in the context of the logged on user
                                       (default: SYSTEM)
  -s, --show                           Show the application in the Configuration Manager console (default:
                                       hidden)
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
Create a new hidden application with the name `app01` that launches `calc.exe`:
```
.\SharpSCCM.exe new application -n app01 -p calc.exe

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Creating new application: app01
[+] Application path: calc.exe
[+] Updated application to hide it from the Configuration Manager console
[+] Updated application to run as SYSTEM
[+] Successfully created application
[+] Completed execution in 00:00:22.8538193
```
---

# new collection
### Description
Create a collection of devices or users by contacting an SMS Provider via WMI

### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator
  - Infrastructure Administrator
  - Operations Administrator
  - Security Administrator

### Usage
```
SharpSCCM new collection [options]

Options:
  -n, --collection-name <collection-name> (REQUIRED)  The name of the new collection
  -t, --collection-type <device|user> (REQUIRED)      The type of collection to create ("device" or "user")
  -sms, --sms-provider <sms-provider>                 The IP address, FQDN, or NetBIOS name of the SMS
                                                      Provider to connect to (default: the current
                                                      management point of the client running SharpSCCM)
  -sc, --site-code <site-code>                        The three character site code (e.g., "PS1") (default:
                                                      the site code of the client running SharpSCCM)
  --debug                                             Print debug messages for troubleshooting
  --no-banner                                         Do not display banner in command output
  -?, -h, --help                                      Show help and usage information
```
### Examples
Create a new device collection named "devicecollection":
```
.\SharpSCCM.exe new collection -n devicecollection -t device

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Creating new device collection: devicecollection
[+] Successfully created collection
[+] Completed execution in 00:00:02.6569059
```

---

# new collection-member
### Description
Add a device to a collection by contacting and SMS Provider via WMI
 
### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator
  - Infrastructure Administrator
  - Operations Administrator
  - Security Administrator

### Usage
```
SharpSCCM new collection-member [options]

Options:
  -d, --device <device>                    The name of the device to add to the specified collection
  -i, --collection-id <collection-id>      The CollectionID of the collection to add the specified device or
                                           user to
  -n, --collection-name <collection-name>  The name of the collection to add the specified device or user to
  -r, --resource-id <resource-id>          The unique ResourceID of the device or user to add to the
                                           specified collection
  -t, --collection-type <device|user>      The type of the collection ("device" or "user")
  -u, --user <user>                        The UniqueUserName of the user to add to the specified
                                           collection, including escaped backslashes (e.g.,
                                           "APERTURE\\cave.johnson")
  -w, --wait-time <wait-time>              The time (in seconds) to wait for the collection to populate
                                           before displaying new collection members (default: 15 seconds)
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
Add the `CAVE-JOHNSON-PC` device to the `devicecollection` device collection:
```
.\SharpSCCM.exe new collection-member -d CAVE-JOHNSON-PC -n devicecollection

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Found resource named CAVE-JOHNSON-PC with ResourceID 16777274
[+] Added CAVE-JOHNSON-PC 16777274 to devicecollection
[+] Waiting for new collection member to become available...
[+] New collection member is not available yet... trying again in 5 seconds
[+] New collection member is not available yet... trying again in 5 seconds
[+] Successfully added CAVE-JOHNSON-PC 16777274 to devicecollection
[+] Completed execution in 00:00:17.0243932
```

---

# new deployment

### Description
Create an assignment to deploy an application to a collection by contacting an SMS Provider via WMI

### Requirements
Permitted security roles:
  - Full Administrator
  - Application Administrator
  - Application Deployment Manager
  - Operations Administrator

### Usage
```
SharpSCCM new deployment [options]

Options:
  -a, --application-name <application-name> (REQUIRED)  The name of the application to deploy
  -c, --collection-name <collection-name>               The name of the collection to deploy the application
                                                        to
  -i, --collection-id <collection-id>                   The CollectionID of the collection to add the
                                                        specified device or user to
  -sms, --sms-provider <sms-provider>                   The IP address, FQDN, or NetBIOS name of the SMS
                                                        Provider to connect to (default: the current
                                                        management point of the client running SharpSCCM)
  -sc, --site-code <site-code>                          The three character site code (e.g., "PS1")
                                                        (default: the site code of the client running
                                                        SharpSCCM)
  --debug                                               Print debug messages for troubleshooting
  --no-banner                                           Do not display banner in command output
  -?, -h, --help                                        Show help and usage information
```

### Examples
Create a new deployment of the `app01` application to the `DEVICES` collection:
```
.\SharpSCCM.exe new deployment -a app01 -c DEVICES

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Connecting to \\ATLAS.APERTURE.SCI\root\SMS\site_PS1
[+] Creating new deployment of app01 to DEVICES (PS10004C)
[+] Found the app01 application
[+] Successfully created deployment of app01 to DEVICES (PS10004C)
[+] New deployment name: app01_PS10004C_Install
[+] Completed execution in 00:00:06.0505442
```

---

# new device
### Description
Create a new device record and obtain a reusable certificate for subsequent requests (experimental)

### Requirements
PKI certificates are not required for client authentication (default)

### Usage
```
SharpSCCM new device [options]

Options:
  -n, --name <name> (REQUIRED)         The NetBIOS name, IP address, or IP address and port (e.g.,
                                       "192.168.1.1@8080") of the new device
  -p, --password <password>            The password for the specified computer account (required to get
                                       secrets)
  -u, --username <username>            The name of the computer account to register the new device record
                                       with, including the trailing "$" (required to get secrets)
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
Using known computer account credentials, create a new device record named "NEWDEVICE" and a corresponding reusable self-signed certificate that allows secret policy retrieval:
```
.\SharpSCCM.exe new device -n NEWDEVICE -u chell$ -p password

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |

[+] Querying the local WMI repository for the current management point and site code
[+] Connecting to \\127.0.0.1\root\CCM
[+] Current management point: ATLAS.APERTURE.SCI
[+] Site code: PS1
[+] Created "ConfigMgr Client Messaging" certificate in memory for device registration and signing/encrypting subsequent messages
[+] Reusable Base64-encoded certificate:

    308209D20201033082098E06092A864886F70D010701A082097F0482097B308209773082059006092A864886F70D010701A08205810482057D3082057930820575060B2A864886F70D010C0A0102A08204EE308204EA301C060A2A864886F70D010C0103300E0408C58F4E4BFA652A7A020207D0048204C8673FCCC994DCD004646DDEE9E4C0E24760DDC44BE41F458A7EF8DD0A76EC6C628EBFE3BC426925DB28139D63A147028AECB5538E876995802CCBD8E4FDAC98361EBD5328C4DDBE226278919865CF95C472E8D1CF674E079B19DE9D4DE7DD202ED5E02DF71413130BCA8095EC2C84FA89AF7FECC8001D42E11D4151D152F0213E65C0151EA0C42A2C8C263E9FA8D73C883C3F8CE8D5811B5D514D104C152A5CDF8217EF3580D4866FDEA68DE2E62A9675B13D8DB0163BB8992D4DE2A1FE28BC0C210DF2B2A27715212A06CA6B17672CFB44A7295AC2282FA40798469D078FF5ED4A976E46EB0AD653DC56E84A17026E64680A4C816549E2FA8CBEF8FF509CCA5A23BCFABD466FC38A4F48248920247CB350725E120D18E107DF9591068DCE4473578F29EA8F9BE1FA62CE4032259D76F001B7F00286BDD454CBE010B15737957D110B1EC24966B2060C0DA6A7E1F186101F7262BD13C8166E777612A37156CD904397C980AAC31BE1DAA8C53B44DFA7C06B3ADC15DA005A624F278A32EB5FDF5CCB360700D9C2B4F857E4B84435EC8585616C5DB3B1C0648E6B2DE3FB0714369FABD6F059D1A5765CF997CA67D37FD07FE3F9FB29443A89FD6245676820B89ACB274AB177337734A38186CA2A1283C46EEA88573C946507DA7B0CAEB4F1F264FF7676C1AD6C96E736FD9097032586FE8CB41A9E7E43F005CFD7C13CE773C9584CC11C3138F045707D43946F92B720EA7D94EF86700FF07D8CC433F671EFCCF1050B521572B177F395A98CC4AB2C257C8B54560C4E8203FF7DA5927165CB1930B3E833D32C594375E13E09AA1E403F5C954AB4A98C1A3C0DF69AE1EED8C7CEC343B655452B5875C2E47185A3A5BAB2D68ED722073A734293B413BAF2B9F5122505E44AEBE6E639C0729A4B122E5E564279EAC5AAECFECC75FCC74DA7E5F56BB1E04A2FAD439DF652EB44EECE052E45C6E10C3A94A8039B9692E16D8FE3570BF5F312BED3E684056990C165D193918E0F5BBCAACABF92FA00AA596CB513EBB649CEF98DEFCC062C2F518451C64C430A0CEC3DFC72BC30BBA2BA15A246C4D99234477DBE48EBB29E11131D4AFB43F25D043478982A8EF547F737E3DB3A41EEFEAAC7F3AB9A1AFEBEDB484EA94ADAA6AFFF0FBC3DEC1F5D8BF246A19B3A20C06F7928F9B894647170D26A33C6F2681E1E5D39D7563A6478216C872B9AEFBC96A6B6A28B07807E83C94F280A2834A98F0ADE78BCE6DF2B3EAD598FAC8C5302EACDF1D32948AEBD6138BBDD51769B88252BCD84BB647A13A49B6F0D6791E43163B1E964BA3B1D03727721816FE4160A5AA3FA80F13378ED43C3446E3D07CA5CA170B593DA883D282942530EAA3BAFEEFB62A80E9E7229FB11D12979DFB9989F023F9BF09397771BEE301D7ECAA9CAE1509BCE67B788A68F27DBE1EEDA9AF86F31BA6C4EB3CF809608910675AAC9D0755B013866CBD65D4A14C13C3903603DCF5A0EAA828BA0EFD8B673DC5E359E670F51DBA470CD161AAB2B316B2CE6AC51624494BE65BF8205D5F61A7019A3779B995B30DD3EA0852068CA9EB126C0A3A28F2F104E46F5EC85EA4095651E4792F3A48E427045E1C9AC4D76F9374F61A6FEEDAB775EE34E1AD66BD0EE4AFE53A62F9E51A20A3047B66F56FE7BA2811C76108B8D94B7A2139568575AF714F617A33F91E9C8E13535A78AED48ACCB8DCFF6B040EBF676F6E3B3372C7518ACF63174301306092A864886F70D0109153106040401000000305D06092B060104018237110131501E4E004D006900630072006F0073006F0066007400200053006F0066007400770061007200650020004B00650079002000530074006F0072006100670065002000500072006F00760069006400650072308203DF06092A864886F70D010706A08203D0308203CC020100308203C506092A864886F70D010701301C060A2A864886F70D010C0103300E0408C8CFC47C94919738020207D08082039836EE5E2A3CF4A2F8D23548FB647ADEA6634D671E18AC1DA7831146DB8C2E0A1A507534E4611162E432DBDDFBAA974E3BF07F2A2EB80099EC7DF5965DB8F119E32823532696581819FD5690CB4D984CFD633AC2E596E928C8922A958D131D7B29B85EB2F1ECDF21D2ABDD9EBD4A4854B594BF80B82CAAA565A950D32B5A8ACE0CB1CC08E998BA9BDB2AA09BC1628983278557FBC471CCE5C16C347B3463FE2855A4AD9E9D745F2BF3E84D4F3E5E8E7A413356F2568119DB671B85A2FB4B1F2063481549D88CEFDE65A3A128A7FFC24D0B4C70FEFB5E6301802927786E1EAD8B0EA065911B2C1259E79A2AD67A9EBCF0471B9341C03D72EE51EF1165215F90B88D66214EEE1CDF3EC351CB977F349B2F43A16A14A28E36798B0DF50A15FBEA11B5F56EF59A7BA0E166193A5093AA6CC3FDD8F602F6C24EF62D57DAABCC717A358C54331D70855C6742FF6839B444A9EEC92ABAFDC405BAEAA937C86CD3053C74A6016CA6BF1A69487962515146CEBD3B3FEB8B645B6D5FA08BBBE8D8A0F87E60692BB1E24A93841BD1317B0FE0F210EEFEAD31538CD7C16682669658280DE34CFCE024C6E9CD4CA46C6C3AFE26BB3A013495335C2BF89E2B168AB157301D84B7043889E854762DE8DE5E924111D03A0C0014E147D0E81F00D3053F6E542D091A6995EFF25124581E7D4D0B9BF6E79B906D5E31230028A1F599EDE49EA7D15E86F8D557BFA19B887D88944529602CF9B636F0E56FBBEEB9816BA24C1A4A828F58292140CEC482AA175718E323758BF53456FEED6B73A704C29F575A34240ABF71C989D089EED37992F22E1C9869B577F34430D1A5C949C6BEC017520CEE0458665AC49947CAF03569BFECFAA408722A386B77FC96D08D5690D3019A3BCDF9022BAE3534805289C5FDD0205E4E7D3F5EA041E8F88EA298410F81C251CE126555A3014D704CD11E286CF6886755CA4CF7F6566AAACE9A98903AA79FA241A0DA05858BE1F625D5FF97EB1CA321EB772A597CAEDE113A06275CDF5E2AD9D5BD9DF1F7291C0C91BDE1AA66A69D8BBA03B5BACDAF645B3758433EF78FE26E97463B4B7602DD5607954A2BA01F23B66CCBF9ACFDB8726A9CA5B07A9185F725060E3971F72849618549908086E9E3DE36E7AB6BAC3D3094C5DA1EE0577FB23A857C079EBD8E02ACACC3AB69F1B527E87497C5424D43DEA8177F641AE9D2A8E5A96C4463A6D785B6051A133C85725DB3D9A39119E8FBFDED49C6720049AFAF2290935136DB63A15A6B86530D0DF2E862A14A62B6B689E44CF5FE5884F4E8303B301F300706052B0E03021A0414C8ADF93AAE03E264AADFA1A1E6258494EF0D1F1D0414B7CC1DB30BD0F333260687A9E67D1E2CDAE4F8F1020207D0

[+] Discovering local properties for client registration request
[+] Modifying client registration request properties:
      FQDN: NEWDEVICE
      NetBIOS name: NEWDEVICE
      Authenticating as: chell$
      Site code: PS1
[+] Sending HTTP registration request to ATLAS.APERTURE.SCI:80
[+] Received unique SMS client GUID for new device:

    GUID:001B2EE1-AE95-4146-AE7B-5928F1E4F396

[+] Completed execution in 00:00:06.2773716
```
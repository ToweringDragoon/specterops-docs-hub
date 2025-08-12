---
description: SharpSCCM documentation
title: SharpSCCM
---

# Introduction
SharpSCCM is a post-exploitation tool designed to leverage Microsoft Endpoint Configuration Manager (a.k.a. ConfigMgr, formerly SCCM) for credential gathering and lateral movement without requiring access to the SCCM administration console GUI. 

# Features
- User location and lateral movement [functions ported from PowerSCCM](https://enigma0x3.net/2016/02/29/offensive-operations-with-powersccm/)
- [Requesting NTLM authentication from SCCM clients](https://posts.specterops.io/relaying-ntlm-authentication-from-sccm-clients-7dccb8f92867) for lateral movement
- [Credential gathering (Network Access Accounts)](https://posts.specterops.io/the-phantom-credentials-of-sccm-why-the-naa-wont-die-332ac7aa1ab9) by Duane Michael [@subat0mik](https://twitter.com/subat0mik)
- [Requesting and Unobfuscating NAAs](https://blog.xpnsec.com/unobfuscating-network-access-accounts/) by Adam Chester [@\_xpn\_](https://twitter.com/_xpn_)
- Functionality to abuse newly discovered attack primitives for [coercing NTLM authentication from SCCM servers](https://posts.specterops.io/coercing-ntlm-authentication-from-sccm-e6e23ea8260a) in sites where automatic site-wide client push installation is enabled, which can allow [takeover of SCCM](https://posts.specterops.io/sccm-site-takeover-via-automatic-client-push-installation-f567ec80d5b1)
- CMPivot query execution via the AdminService API

This tool can be used to demonstrate the impact of configuring SCCM without the [recommended security settings](https://docs.microsoft.com/en-us/mem/configmgr/core/clients/deploy/plan/security-and-privacy-for-clients).

SharpSCCM works from any Windows machine running the SCCM client software and leverages Windows Management Instrumentation (WMI) and the ConfigMgr Client Messaging SDK to communicate with SCCM management points.

# Defensive Recommendations
### ConfigMgr
- Install hotfix KB15599094 and disable NTLM for client push installation (prevents coercion via client push)
- Use Enhanced HTTP and disable network access accounts
- Disable automatic site-wide client push installation, use software update-based installation instead
- Set a strong PXE boot password (prevents cracking to obtain OSD creds)
- Disable "F8-Debugging" (uncheck the "Enable command support" option) in production PXE boot networks
- Require PKI certificates for client authentication (prevents rogue device registration)
- [Enable multi-factor authentication for SMS Provider calls](https://learn.microsoft.com/en-us/troubleshoot/mem/configmgr/setup-migrate-backup-recovery/enable-mfa-for-sms-provider-calls)
- Don't use over-privileged credentials (e.g., Domain Admins) for NAA/client push/domain join/task sequences/collection variables
- Don't enable WebClient on site systems (prevents coercion via HTTP)
- Don't manage tier zero assets (e.g., domain controllers) with ConfigMgr or treat ConfigMgr as tier zero
- Access the ConfigMgr console using accounts in the same tier as the devices in the site

### Domain/Server
- Require SMB signing on all site systems (prevents relay to SMB)
- Require LDAP signing or channel binding on domain controllers (prevents relay to LDAP)
- Require Extended Protection for Authentication (EPA) on AD CS servers (prevents relay to HTTP)
- Disable network access accounts in AD after ConfigMgr transition to Enhanced HTTP
- Disable SeMachineAccountPrivilege/MachineAccountQuota for non-admin users to prevent them from adding computers to the domain
- Remove Extended Rights assignment from users who do not require this permission (prevents GetLAPSPassword for created accounts)
- Move from legacy LAPS to Windows LAPS in Azure with password encryption enabled

### Database
- Require Extended Protection for Authentication (EPA) on the site database (prevents relay to MSSQL)
- Don't link other databases to your site database, especially with DBA privileges
- Set strong passwords for DBA accounts

### Firewall/Network
- Block all unnecessary connections to site systems, especially SMB and MSSQL (reduces coercion via SMB and relay to SMB/MSSQL)
- Only support PXE boot on VLANs restricted to authorized administrators

### Security
- Monitor for suspicious activity on site systems and using site accounts
  * Site system computer accounts authenticating from an IP address that isn't their static IP
  * Client push installation accounts authenticating from anywhere other than the primary site server
  * Canary network access accounts and client push installation accounts authenticating anywhere
  * Legitimate network access accounts authenticating to anywhere other than a distribution point
  * Unusual application deployments in the site's Audit Status Messages

More ideas for detection opportunities can be found in the Detection Guidance section of this post: https://posts.specterops.io/coercing-ntlm-authentication-from-sccm-e6e23ea8260a. Please reach out or submit an update if you have any other practical detection ideas that have minimal impact on user experience, performance, additional overhead, etc.

# Development
Microsoft's [Windows and Office 365 deployment lab kit](https://docs.microsoft.com/en-us/microsoft-365/enterprise/modern-desktop-deployment-and-management-lab?view=o365-worldwide) can deploy a fully operational SCCM lab in Hyper-V in less than an hour. You only need the following systems to begin testing SharpSCCM functionality:
- CM1: Configuration Manager Primary Site Server, Management Point, and Site Database Server
- GW1: Configuration Manager Client
- DC1: Domain Controller

You could also consider deploying a lab in Azure using a [template](https://learn.microsoft.com/en-us/samples/azure/azure-quickstart-templates/sccm-technicalpreview/), [AutomatedLab](https://automatedlab.org/en/latest/), or [Snaplabs](https://twitter.com/an0n_r0/status/1687230842601451522).

For debugging, I share a directory in GW1 that is accessible from my host running Visual Studio, execute the Visual Studio Remote Debugger on GW1, configure a post-build job to copy the solution files to the share on GW1, and configure Visual Studio to remote debug on GW1. 

# My Research
- [Coercing NTLM Authentication from SCCM](https://medium.com/specter-ops-posts/coercing-ntlm-authentication-from-sccm-e6e23ea8260a)
- [Relaying NTLM Authentication from SCCM Clients](https://medium.com/specter-ops-posts/relaying-ntlm-authentication-from-sccm-clients-7dccb8f92867)
- [SCCM Site Takeover via Automatic Client Push Installation](https://medium.com/specter-ops-posts/sccm-site-takeover-via-automatic-client-push-installation-f567ec80d5b1)
- [SCCM Hierarchy Takeover](https://posts.specterops.io/sccm-hierarchy-takeover-41929c61e087)
- [Hierarchy Takeover without SOCKS](https://twitter.com/_Mayyhem/status/1700602445603209236)

Research is ongoing to add SharpSCCM features to:
- execute SharpSCCM actions in environments that require PKI certificates

# My Videos/Talks
- [Black Hat USA Arsenal 2022: SharpSCCM](https://www.youtube.com/watch?v=19F_Io1Tykg)
- [Black Hat USA Arsenal 2023: SharpSCCM - Abusing Microsoft's C2 Framework](https://www.youtube.com/watch?v=uyI5rgR0D-s)
- [Black Hat USA SpecterOps Booth 2023: SharpSCCM - Abusing Microsoft's C2 Framework](https://www.youtube.com/watch?v=Q8mEMFKscnk)

# Offensive SCCM Resources by Other Awesome People
- [Active Directory Spotlight: Attacking The Microsoft Configuration Manager (SCCM/MECM), by Carsten Sandker (@0xcsandker)](https://www.securesystems.de/blog/active-directory-spotlight-attacking-the-microsoft-configuration-manager/)
- [An Inside Look: How to Distribute Credentials Securely in SCCM, by Christopher Panayi](https://www.mwrcybersec.com/an-inside-look-how-to-distribute-credentials-securely-in-sccm)
- [CISA Red Team Report Featuring SCCM, by CISA](https://www.cisa.gov/sites/default/files/2023-03/aa23-059a-cisa_red_team_shares_key_findings_to_improve_monitoring_and_hardening_of_networks_1.pdf)
- [Client Push Installation Abuse, by Matt Nelson (@enigma0x3)](https://twitter.com/enigma0x3/status/962095579068354561?lang=ar-x-fm)
- [CMLoot, by Tomas Rzepka (@1njected)](https://github.com/1njected/CMLoot)
- [cmloot, by Andreas Vikerup and Dan Rosenqvist](https://www.shelltrail.com/research/cmloot/)
- [CMPivot SharpSCCM Support, by Diego Lomellini (@DiLomSec1)](https://github.com/Mayyhem/SharpSCCM/pull/27)
- [Deobfuscator Implementation in Python by @SkelSec](https://github.com/xpn/sccmwtf/pull/3)
- [Exploring SCCM by Unobfuscating Network Access Accounts, by Adam Chester (@_xpn_)](https://blog.xpnsec.com/unobfuscating-network-access-accounts/)
- [Get Secrets via PXE Media Certificates SharpSCCM PR, by Carsten Sandker (@0xcsandker)](https://github.com/Mayyhem/SharpSCCM/pull/28)
- [Grow Your Own SCCM Lab, by @HTTP418](https://http418infosec.com/grow-your-own-sccm-lab)
- [impacket SCCM Relay, by Matt Creel (@Tw1sm)](https://github.com/Tw1sm/impacket/tree/feature/sccm-relay)
- [Looting Microsoft Configuration Manager, by Tomas Rzepka (@1njected)](https://labs.withsecure.com/publications/looting-microsoft-configuration-manager)
- [Mimikatz misc::sccm, by Benjamin Delpy (@gentilkiwi)](https://twitter.com/gentilkiwi/status/1392204021461569537?lang=en)
- [Mimikatz dpapi::sccm, by Benjamin Delpy (@gentilkiwi)](https://twitter.com/gentilkiwi/status/1392594113745362946?lang=en)
- [MalSCCM, by Phil Keeble (@The_Keeb)](https://github.com/nettitude/MalSCCM)
- [Offensive Operations with PowerSCCM, by Matt Nelson (@enigma0x3)](https://enigma0x3.net/2016/02/29/offensive-operations-with-powersccm/)
- [Offensive SCCM Summary, by @HTTP418](https://http418infosec.com/offensive-sccm-summary)
- [Owning One to Rule Them All, by Dave Kennedy (@HackingDave) and Dave DeSimone](https://vimeo.com/47978442)
- [PowerSCCM, by Matt Nelson (@enigma0x3), Will Schroeder (@harmj0y), Jared Atkinson (@jaredcatkinson), and Matt Graeber (@mattifestation)](https://github.com/PowerShellMafia/PowerSCCM)
- [Pulling Passwords Out of Configuration Manager, by Christopher Panayi](https://www.youtube.com/watch?v=Ly9goAud0gs)
- [Push, by Vulnlab](https://www.vulnlab.com/machines)
- [Push Comes to Shove: Exploring SCCM Attack Paths, by Brandon Colley (@TechBrandon)](https://www.youtube.com/watch?v=qLBJJPUGk9U)
- [Push Comes to Shove Part 1, by Brandon Colley (@TechBrandon)](https://www.hub.trimarcsecurity.com/post/push-comes-to-shove-exploring-the-attack-surface-of-sccm-client-push-accounts)
- [Push Comes to Shove Part 2, by Brandon Colley (@TechBrandon)](https://www.hub.trimarcsecurity.com/post/push-comes-to-shove-bypassing-kerberos-authentication-of-sccm-client-push-accounts)
- [PXEThief, by Christopher Panayi](https://github.com/MWR-CyberSec/PXEThief)
- [pxethiefy, by Carsten Sandker (@0xcsandker)](https://github.com/sse-secure-systems/Active-Directory-Spotlights/tree/master/SCCM-MECM/pxethiefy)
- [Red Team Ops SCCM Module, by Zero Point Security (@zeropointsecltd)](https://twitter.com/zeropointsecltd/status/1707385897979654508)
- [SCCM Credential Recovery for Network Access Accounts, by Evan McBroom (@mcbroom_evan)](https://gist.github.com/EvanMcBroom/525d84b86f99c7a4eeb4e3495cffcbf0)
- [SCCM Decrypt POC, by Adam Chester (@_xpn_)](https://gist.github.com/xpn/5f497d2725a041922c427c3aaa3b37d1)
- [SCCM w/ Garrett Foster (@garrfoster), by Brandon Colley (@TechBrandon) at Trimarc Happy Hour](https://www.youtube.com/watch?v=I5YTH0kQlr8)
- [SCCM Exploitation: The First Cred is the Deepest II, by Gabriel Prud'homme (@vendetce)](https://www.youtube.com/watch?v=W9PC9erm_pI)
- [SCCM/MECM Hacker Recipes, by Charlie Bromberg (@_nwodtuhs)](https://www.thehacker.recipes/a-d/movement/sccm-mecm)
- [sccmhunter, by Garrett Foster (@garrfoster)](https://github.com/garrettfoster13/sccmhunter)
- [sccmwtf, by Adam Chester (@_xpn_)](https://github.com/xpn/sccmwtf)
- [SharpDPAPI SCCM Credential Gathering Support, by Duane Michael (@subat0mik)](https://github.com/GhostPack/SharpDPAPI/blob/81e1fcdd44e04cf84ca0085cf5db2be4f7421903/SharpDPAPI/Commands/SCCM.cs#L208-L244)
- [Site Takeover via SCCM's AdminService API, by Garrett Foster (@garrfoster)](https://posts.specterops.io/site-takeover-via-sccms-adminservice-api-d932e22b2bf)
- [Snaplabs SCCM Lab Template, by @an0n_r0](https://twitter.com/an0n_r0/status/1687230842601451522)
- [SQLRecon SCCM Module, by Sanjiv Kawa (@sanjivkawa)](https://github.com/skahwah/SQLRecon)
- [Targeted Workstation Compromise with SCCM, by Matt Nelson (@enigma0x3)](https://enigma0x3.net/2015/10/27/targeted-workstation-compromise-with-sccm/)
- [The Phantom Credentials of SCCM: Why the NAA Won't Die, by Duane Michael (@subat0mik)](https://posts.specterops.io/the-phantom-credentials-of-sccm-why-the-naa-wont-die-332ac7aa1ab9)
- [We Have C2 at Home: Leveraging Microsoft's C2 Framework, by Garrett Foster (@garrfoster)](https://www.youtube.com/watch?v=w-9GMz7vD0o&t=6435s)

# Supporters
The time I'm able to spend researching, developing, and improving SharpSCCM would not be possible without [SpecterOps's](https://www.specterops.io/) sponsorship of the project as part of their commitment to transparency and support for open-source development. I'm immensely grateful for their guidance and support.

# Contributions
The following people have contributed to this project:
- Duane Michael ([@subat0mik](https://twitter.com/subat0mik))
- Evan McBroom ([@EvanMcBroom](https://twitter.com/mcbroom_evan))
- Diego Lomellini ([@DiLomSec1](https://twitter.com/DiLomSec1))
- Carsten Sandker ([@0xcsandker](https://twitter.com/0xcsandker))

Some features were built based on the work of the following people:
- Matt Nelson ([@enigma0x3](https://twitter.com/enigma0x3))
- Will Schroeder ([@harmj0y](https://twitter.com/harmj0y))
- Benjamin Delpy ([@gentilkiwi](https://twitter.com/gentilkiwi))
- Adam Chester ([@_xpn_](https://twitter.com/_xpn_))
- Garrett Foster ([@garrfoster](https://twitter.com/garrfoster))
- [guervild](https://github.com/guervild)

Special thanks to others who submitted PRs/fixes:
- John Lambert ([@JohnLaTwC](https://twitter.com/JohnLaTwC))

If you're interested in collaborating, please hit me up on Twitter ([@_Mayyhem](https://twitter.com/_Mayyhem)) or the [BloodHoundGang Slack](http://ghst.ly/BHSlack)!




---
description: Command Line Usage documentation
title: Command Line Usage
---

# Syntax
`SharpSCCM.exe [command] [options]`

All commands and subcommands have a help page that is automatically generated using the System.CommandLine library. Help pages can be accessed by entering any SharpSCCM command followed by `-h`, `--help`, `/h`, `/?`, or `-?`. Required positional arguments are shown within angle brackets and options are shown within square brackets. SharpSCCM supports command line tab completion with dotnet-suggest, but does not have it enabled by default to prevent writing of files to ~/AppData/Local/Temp/. For more information, see https://github.com/dotnet/command-line-api/blob/main/docs/Features-overview.md.

# Subcommands
```
  exec    Execute a command, binary, or script on a client or request NTLM authentication from a client
  get     A group of commands that fetch objects from SMS Providers via WMI, management points via HTTP(S), or domain controllers via LDAP
  invoke  A group of commands that execute actions on an SMS Provider
  local   A group of commands to interact with the local workstation/server
  new     A group of commands that create new objects by contacting an SMS Provider via WMI
  remove  A group of commands that deletes objects by contacting an SMS Provider via WMI
```

# Required Arguments
The `server` and `sitecode` arguments are no longer required. By default, SharpSCCM will use the current management point of the client device it is executed from. However, much of the functionality relies on the SMS Provider role, which may be hosted separately from management points. This role is installed on the primary site server by default. You can use the `SharpSCCM get site-info` to identify potential site servers.

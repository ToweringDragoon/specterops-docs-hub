---
description: deob documentation
title: deob
---

# Using the "deob" Command

This documentation was last updated on 4/15/24 by Chris Thompson (@_Mayyhem). Please refer to the output of the `--help` option for each command for the most up-to-date usage information.

### Description
Deobfuscate a policy secret hex string offline
    
### Requirements
None

### Usage
```
SharpSCCM deob <secret-string> [options]

Arguments:
  <secret-string>  The policy secret hex string to deobfuscate

Options:
  --debug         Print debug messages for troubleshooting
  --no-banner     Do not display banner in command output
  -?, -h, --help  Show help and usage information
```
### Examples
Deobfuscate a secret string:
```
.\SharpSCCM.exe deob 891300000611B0FBE3E5E7BFFC6026279DD585431385F4148760679BF6DF183AB8C3D553401D69452BABE97E140000003A00000040000000036600000000000000DA417D3BF7F38E6DFFAEEF520778F829D93946F9ED61FB91502C3F2D718E996CF3E910C58548E699FCEDDCA215FB4B801CB53A29C7000EBDF0DE020464BBEA0000

  _______ _     _ _______  ______  _____  _______ _______ _______ _______
  |______ |_____| |_____| |_____/ |_____] |______ |       |       |  |  |
  ______| |     | |     | |    \_ |       ______| |______ |______ |  |  |    @_Mayyhem

[+] Deobfuscated secret: aperture.local\NETWORKACCESS
[+] Completed execution in 00:00:00.1439718
```
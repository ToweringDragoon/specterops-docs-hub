---
description: Build Instructions documentation
title: Build Instructions
---

# Building in Visual Studio
1. Clone the git repository.
`git clone https://github.com/Mayyhem/SharpSCCM.git`
2. Open SharpSCCM.sln in Visual Studio.
3. Select Target (e.g., Release > x64)
4. Build Solution (Ctrl + Shift + B)

A version of the SharpSCCM assembly that contains all of its dependencies will be merged and placed in the $(TargetDir) directory (e.g., .\SharpSCCM\bin\x64\Release\SharpSCCM.exe).

If Visual Studio displays red underlines under the code, try building anyway and they should go away.
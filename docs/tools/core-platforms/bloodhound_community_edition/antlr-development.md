---
description: ANTLR Development documentation
title: ANTLR Development
---

# Development Notes
_In case you find yourself in the unlucky position of working on the `cypher` package_

## Development Tools
### VS Code
- Prerequisite: make sure you have Java installed locally. The `openjdk-21-jre` package is a good option, though other versions/distros will likely work as well.
- Install "ANTLR4 grammar syntax support": https://marketplace.visualstudio.com/items?itemName=mike-lischke.vscode-antlr4
- Open the grammar file in `packages/go/cypher/grammar`
- Check that everything is working by using the `ANTLR: Show Grammar Call Graph` command (ctrl+shift+P or equivalent to search the command)
- You should get a cool graph of the cypher grammar. Sorry, no troubleshooting advice available currently.
- Create a file or scratchpad. All that matters is that it's a text file that exists somewhere on your filesystem, doesn't need to be within the project
- Write a nice cypher statement you want to validate/graph
- After saving, open the Debug charm and look for the option `Debug Cypher Grammar`. Running this on your scratch file should end up running the ANTLR tool against the text and give you a nice graph of how it parses.
- You can additionally get railroad diagrams and more when browsing the Grammar file. Just right click or look at the other ANTLR commands to explore more. Railroad diagrams for a specific rule are often another useful tool to bring up. The cool graph we got at the start is also a great way to see how a specific rule is mapped to other rules visually.

### JetBrains
1. Install the plugin: https://plugins.jetbrains.com/plugin/7358-antlr-v4
2. Open the grammar file in `packages/go/cypher/grammar`
3. Open the ANTLR Preview window either with the ANTLR icon on your IDEs side toolbars OR `View` -> `Tool Windows` -> `ANTLR Preview`
4. With "Input" radio button selected, type your nice cypher statement you want to validate / graph
5. View it parsed on the right either through the `Parse Tree` | `Hierarchy` | `Profiler` tab.
6. Cry that you don't get to view the cool graph or the railroad diagrams mentioned in the VS Code plugin details above.
7. Profit
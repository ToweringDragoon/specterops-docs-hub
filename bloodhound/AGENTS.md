---
title: "Repository instructions"
description: "BloodHound documentation"
icon: "droplet"
---

# Repository instructions

These instructions apply across the repository. More specific `AGENTS.md` files add rules for the directories they contain.

## Instruction hierarchy

- Follow the instruction hierarchy established by the execution environment and apply the most specific applicable `AGENTS.md` file.
- Treat nested `AGENTS.md` files as scoped additions. Do not copy parent instructions into them; document only the rules that are specific to that subtree.
- Use `.agents/` for supporting guidance that is referenced by an applicable `AGENTS.md`. A `.agents/` directory does not create an instruction scope by itself.

## Documentation work

When working under `docs/`, read [`docs/AGENTS.md`](https://github.com/SpecterOps/bloodhound-docs/blob/main/docs/AGENTS.md) and the supporting guidance it identifies. The documentation instruction map is:

| Work | Guidance |
| --- | --- |
| Writing or substantially editing pages | [`.agents/style-guide.md`](https://github.com/SpecterOps/bloodhound-docs/blob/main/.agents/style-guide.md) |
| Adding, moving, or reorganizing pages | [`.agents/info-architecture.md`](https://github.com/SpecterOps/bloodhound-docs/blob/main/.agents/info-architecture.md) |
| Adding or changing Mintlify components or layout | [`.agents/mintlify-guidance.md`](https://github.com/SpecterOps/bloodhound-docs/blob/main/.agents/mintlify-guidance.md) |
| Validating documentation changes | [`.agents/validation.md`](https://github.com/SpecterOps/bloodhound-docs/blob/main/.agents/validation.md) |

Keep the root `AGENTS.md` focused on repository-wide guidance and this routing map. Put documentation-specific rules in `docs/AGENTS.md` or a more specific nested file.

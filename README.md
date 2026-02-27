# MITRE ATT&CK Semantic Navigator

Map natural-language attack scenarios to MITRE ATT&CK techniques using semantic embeddings.
This project demonstrates how vector embeddings and semantic search can help security teams quickly translate incident descriptions into relevant MITRE ATT&CK techniques.

---

## Why this project?

Security analysts often describe incidents in plain language:
> “Attacker stole credentials and moved laterally across machines”

But MITRE ATT&CK uses structured techniques.
This tool bridges the gap using AI.

---

## Features

- Parses the official MITRE ATT&CK dataset (STIX)
- Generates sentence embeddings for all techniques
- Performs semantic similarity search
- Returns most relevant techniques for a scenario
- Embedding caching for fast startup

---

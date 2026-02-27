# MITRE ATT&CK Semantic Navigator

A small project that maps plain-English attack scenarios to MITRE ATT&CK techniques using embeddings and semantic search.

The idea is simple: you describe what happened during an incident, and the tool suggests the most relevant ATT&CK techniques.

---

## Why I built this

In real incidents, things are described like this:

> “Attacker stole credentials and moved laterally across machines”

But MITRE ATT&CK is structured and technique-driven.

I wanted to see how far I could get using embeddings to bridge that gap and make the mapping feel more natural.

---

## What it does

- Parses the official MITRE ATT&CK dataset  
- Creates embeddings for all techniques  
- Uses semantic similarity to match scenarios → techniques  
- Returns the most relevant techniques for consideration  
- Caches embeddings so the tool starts fast after the first run

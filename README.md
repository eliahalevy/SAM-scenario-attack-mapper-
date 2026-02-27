# MITRE ATT&CK Semantic Navigator

Describe an attack scenario and instantly get the top 3 likely MITRE ATT&CK techniques.
This small project maps plain-English incident descriptions to MITRE ATT&CK techniques using embeddings and semantic search, helping bridge the gap between real incident language and the structured ATT&CK framework.

---

## Why I built this project

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

---


## Example

Input

Attacker steals credentials and moves laterally across machines


Output

T1003 – OS Credential Dumping
- Tactics: credential-access
- Similarity: 0.6895
- MITRE Link: https://attack.mitre.org/techniques/T1003/

T1570 – Lateral Tool Transfer
- Tactics: lateral-movement
- Similarity: 0.6889
- MITRE Link: https://attack.mitre.org/techniques/T1570/

T1563.002 – RDP Hijacking
- Tactics: lateral-movement
- Similarity: 0.6829
- MITRE Link: https://attack.mitre.org/techniques/T1563/002/






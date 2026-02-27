import json
import pandas as pd

INPUT_FILE = "data/enterprise-attack.json"
OUTPUT_FILE = "data/mitre_techniques.csv"


def extract_techniques():
    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    techniques = []

    for obj in data["objects"]:
        # We only want ATT&CK techniques
        if obj.get("type") == "attack-pattern":

            # Some objects are deprecated → skip them
            if obj.get("revoked") or obj.get("x_mitre_deprecated"):
                continue

            technique_id = None
            for ref in obj.get("external_references", []):
                if ref.get("source_name") == "mitre-attack":
                    technique_id = ref.get("external_id")

            if not technique_id:
                continue

            name = obj.get("name", "")
            description = obj.get("description", "")

            tactics = obj.get("kill_chain_phases", [])
            tactic_names = [t["phase_name"] for t in tactics]

            techniques.append({
                "technique_id": technique_id,
                "name": name,
                "description": description,
                "tactics": ", ".join(tactic_names)
            })

    df = pd.DataFrame(techniques)
    df = df.sort_values("technique_id")

    print("Techniques extracted:", len(df))
    df.to_csv(OUTPUT_FILE, index=False)
    print("Saved to", OUTPUT_FILE)


if __name__ == "__main__":
    extract_techniques()
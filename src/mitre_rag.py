import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import os

def cosine_similarity_numpy(query_vec, matrix):
    """
    Fast cosine similarity using dot product.
    Assumes vectors are normalized.
    """
    return np.dot(matrix, query_vec.T).squeeze()

DATA_FILE = "data/mitre_techniques.csv"
MODEL_NAME = "BAAI/bge-base-en-v1.5"
CACHE_FILE = "data/mitre_embeddings.npy"


print("Loading MITRE dataset...")
df = pd.read_csv(DATA_FILE)

print("Loading embedding model...")
model = SentenceTransformer(MODEL_NAME)

texts = df["name"] + ". " + df["description"]

if os.path.exists(CACHE_FILE):
    print("Loading cached embeddings...")
    embeddings = np.load(CACHE_FILE)
else:
    print("Generating embeddings for techniques...")
    embeddings = model.encode(texts.tolist(), show_progress_bar=True)
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    np.save(CACHE_FILE, embeddings)
    print("Embeddings cached.")

print("Embeddings ready.\n")


def retrieve_techniques(query, top_k=5):
    query_embedding = model.encode([query])
    query_embedding = query_embedding / np.linalg.norm(query_embedding)
    scores = cosine_similarity_numpy(query_embedding, embeddings)

    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for idx in top_indices:
        results.append({
            "technique_id": df.iloc[idx]["technique_id"],
            "name": df.iloc[idx]["name"],
            "tactics": df.iloc[idx]["tactics"],
            "score": float(scores[idx])
        })

    return results


if __name__ == "__main__":

    print("=" * 60)
    print("MITRE ATT&CK Semantic Navigator")
    print("=" * 60)

    scenario = input("\nDescribe attack scenario:\n> ")

    results = retrieve_techniques(scenario, top_k=5)

    print("\nTop Matching Techniques:\n")

    for r in results:
        print(f"{r['technique_id']} - {r['name']}")
        print(f"Tactics: {r['tactics']}")
        print(f"Similarity: {r['score']:.4f}")
        print("-" * 40)
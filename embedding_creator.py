# In embedding_creator.py
from sentence_transformers import SentenceTransformer
import multiprocessing

class EmbeddingCreator:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def create_embedding(self, chunk):
        return self.model.encode(chunk)

    def create_all_embeddings(self, chunks):
        if not chunks:
            return []
        # Use start_method 'spawn' for compatibility
        multiprocessing.set_start_method('spawn', force=True)
        with multiprocessing.Pool(processes=2) as pool:  # Limit to 2 processes
            embeddings = pool.map(self.create_embedding, chunks)
        return embeddings

if __name__ == "__main__":
    embedder = EmbeddingCreator()
    test_chunks = ["Artificial intelligence is impactful.", "AI changes the world."]
    embeddings = embedder.create_all_embeddings(test_chunks)
    print(f"Created {len(embeddings)} embeddings")
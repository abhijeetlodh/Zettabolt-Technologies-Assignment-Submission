import threading
import numpy as np

class DocumentRetriever:
    def __init__(self, query):
        self.query = query
        self.query_embedding = None

    def create_query_embedding(self, embedding_creator):
        self.query_embedding = embedding_creator.create_embedding(self.query)

    def compute_similarity(self, chunk_embedding):
        if self.query_embedding is None or chunk_embedding is None:
            return 0.0
        return np.dot(self.query_embedding, chunk_embedding) / (np.linalg.norm(self.query_embedding) * np.linalg.norm(chunk_embedding))

    def retrieve_top_k(self, chunk_embeddings, k=3):
        if not chunk_embeddings:
            return []
        similarities = []
        lock = threading.Lock()

        def compute_similarity_thread(chunk_id):
            similarity = self.compute_similarity(chunk_embeddings[chunk_id])
            with lock:
                similarities.append((chunk_id, similarity))

        threads = []
        for i in range(len(chunk_embeddings)):
            thread = threading.Thread(target=compute_similarity_thread, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        similarities.sort(key=lambda x: x[1], reverse=True)
        top_k_indices = [x[0] for x in similarities[:k]]
        return top_k_indices

if __name__ == "__main__":
    from embedding_creator import EmbeddingCreator
    embedder = EmbeddingCreator()
    query = "What is the impact of AI?"
    retriever = DocumentRetriever(query)
    retriever.create_query_embedding(embedder)
    test_embeddings = embedder.create_all_embeddings(["AI is great", "AI impacts society"])
    top_indices = retriever.retrieve_top_k(test_embeddings)
    print(f"Top indices: {top_indices}")
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from wikipedia_scraper import WikipediaScraper
from embedding_creator import EmbeddingCreator
from document_retriever import DocumentRetriever
from text_processor import TextProcessor
import asyncio

def main():
    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    query = "What is the impact of AI?"

    print("Starting data extraction...")
    # Step 1: Extract and clean data
    scraper = WikipediaScraper()
    chunks = scraper.get_chunks(url)
    if not chunks:
        print("No chunks extracted. Exiting.")
        return
    print(f"Extracted {len(chunks)} chunks successfully.")

    print("Starting embedding creation...")
    # Step 2: Create embeddings
    embedding_creator = EmbeddingCreator()
    chunk_embeddings = embedding_creator.create_all_embeddings(chunks)
    if not chunk_embeddings:
        print("No embeddings created. Exiting.")
        return
    print(f"Created {len(chunk_embeddings)} embeddings successfully.")

    print("Starting document retrieval...")
    # Step 3: Retrieve top chunks
    retriever = DocumentRetriever(query)
    retriever.create_query_embedding(embedding_creator)
    top_k_indices = retriever.retrieve_top_k(chunk_embeddings)
    if not top_k_indices:
        print("No top chunks retrieved. Exiting.")
        return
    top_k_chunks = [chunks[i] for i in top_k_indices]
    print(f"Retrieved {len(top_k_chunks)} top chunks successfully.")

    print("Starting text processing...")
    # Step 4: Process top chunks
    processor = TextProcessor()
    processed_chunks = asyncio.run(processor.process_top_chunks(top_k_chunks))
    print(f"Processed {len(processed_chunks)} chunks successfully.")

    # Step 5: Output results
    output = []
    for i, chunk in enumerate(processed_chunks):
        chunk_output = f"Chunk {i+1}:\n{chunk}\n"
        print(chunk_output)
        output.append(chunk_output)

    # Save to log file
    with open("output.log", "w") as f:
        f.write("\n".join(output))
    print("Output written to output.log.")

if __name__ == "__main__":
    main()
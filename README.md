# README

## Setup Instructions:

1. **Run SageMaker Studio**:  
   You need to initialize the SageMaker environment before proceeding.

2. **Terminal Command to Run**:  
   ```bash
   ./run.sh
   
Overview of the Approach:
Multi-threading: Used for parallelizing tasks like retrieving documents or processing data.
Async Programming: Utilized to ensure non-blocking, efficient execution of tasks like text preprocessing.
Multiprocessing: Leveraged to create embeddings in parallel, speeding up the process by handling multiple chunks simultaneously.
Embeddings: The embeddings are created for chunks of text (e.g., from Wikipedia) using SentenceTransformer. No LLM API was used, only locally hosted models.
Generative AI Tools:
The script includes generative AI techniques for embedding creation and document retrieval, emphasizing customization and personal understanding of how these tools are applied, without relying on any LLM API.
Workflow:
Run the following commands in your terminal:

First, run:

bash
Copy
./run.sh
Then, run the main Python script:

bash
Copy
python main.py
Process Overview:

Instantiate Wikipedia_Scraper: Scrapes text chunks from a Wikipedia page.
Use Embedding_Creator: Generates embeddings for all the scraped chunks using multiprocessing to speed up the process.
Use Document_Retriever: Retrieves the top 3 relevant chunks based on the generated embeddings using multi-threading.
Use Text_Processor: Preprocesses the top chunks asynchronously.
Results: Finally, it logs the results in output.log.# Zettabolt-Technologies-Assignment-Submission

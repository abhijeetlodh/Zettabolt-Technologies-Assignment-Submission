import asyncio

class TextProcessor:
    async def preprocess_chunk(self, chunk):
        await asyncio.sleep(0.1)  # Simulate async work
        return chunk.lower()

    async def process_top_chunks(self, chunks):
        if not chunks:
            return []
        tasks = [self.preprocess_chunk(chunk) for chunk in chunks]
        processed_chunks = await asyncio.gather(*tasks)
        return processed_chunks

if __name__ == "__main__":
    processor = TextProcessor()
    test_chunks = ["AI is Great", "IMPACTS of AI"]
    processed = asyncio.run(processor.process_top_chunks(test_chunks))
    print(f"Processed chunks: {processed}")
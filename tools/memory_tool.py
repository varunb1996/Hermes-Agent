import chromadb

client = chromadb.PersistentClient(
    path="memory"
)

collection = client.get_or_create_collection(
    name="hermes_memory"
)


def save_memory(text):

    collection.add(
        documents=[text],
        ids=[str(hash(text))]
    )


def retrieve_memory(query):

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    return results["documents"]
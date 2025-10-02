from dotenv import load_dotenv
import os
from src.helper import load_pdf_file, filter_to_minimal_docs, text_split, download_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec 
from langchain_pinecone import PineconeVectorStore

# Load environment variables
load_dotenv()
print("✅ Environment variables loaded")

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
print("🔑 API keys set")

# Load PDF files
print("📄 Loading PDF files from 'data/' folder...")
extracted_data = load_pdf_file(data='data/')
print(f"✅ Loaded {len(extracted_data)} documents from PDF files")

# Filter documents
print("🔍 Filtering documents to minimal form...")
filter_data = filter_to_minimal_docs(extracted_data)
print(f"✅ Filtered documents count: {len(filter_data)}")

# Split text into chunks
print("✂️ Splitting text into chunks...")
text_chunks = text_split(filter_data)
print(f"✅ Created {len(text_chunks)} text chunks")

# Download embeddings
print("⚙️ Generating embeddings...")
embeddings = download_embeddings()
print(f"✅ Embeddings loaded: {embeddings is not None}")

# Initialize Pinecone
pinecone_api_key = PINECONE_API_KEY
print("🌐 Connecting to Pinecone...")
pc = Pinecone(api_key=pinecone_api_key)
print("✅ Connected to Pinecone")

# Set index name
index_name = "medical-chatbot"

# Create index if not exists
print(f"📂 Checking if Pinecone index '{index_name}' exists...")
if not pc.has_index(index_name):
    print(f"⚡ Index '{index_name}' not found. Creating new index...")
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    print(f"✅ Index '{index_name}' created")
else:
    print(f"✅ Index '{index_name}' already exists")

# Load the index
index = pc.Index(index_name)
print(f"📌 Pinecone index '{index_name}' loaded successfully")

# Create vector store
print("📦 Uploading documents to Pinecone Vector Store...")
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings, 
)
print("✅ Documents uploaded successfully to Pinecone")

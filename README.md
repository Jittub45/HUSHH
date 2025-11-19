

---

# Assessment Recommender System

LIVE WEBSITE: https://shl-recommender-url.onrender.com/

Intelligent assessment recommendation system that maps job descriptions to the most relevant SHL assessments using workflow orchestration, hybrid retrieval, and intelligent reranking.

## Quick Start

Clone repository and set up environment.

```bash
git clone <repository-url>
cd shl-recommender

python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Configure environment variables.

```bash
cp .env.example .env
```

Add Gemini API key in .env.

Run Streamlit UI.

```bash
python run_ui.py
```

Run FastAPI server.

```bash
python run_api.py
```

## Architecture

Query flows through five stages: extraction, hybrid retrieval, balance computation, reranking, and post-processing.

Pipeline stages include
Query enhancement with Gemini
Semantic and BM25 hybrid retrieval
Automatic knowledge personality ratio detection
Reranking with Gemini Flash
Final filtering and deduplication

## Features

LangGraph powered workflow with retries and confidence checks
FAISS semantic search with BM25 augmentation
Specificity and domain based scoring
Intelligent reranking with role and skill reasoning
Adaptive test type balance (technical vs behavioral)
Soft duration scoring to avoid empty outputs

## Project Structure

```
shl-recommender
src
api.py
ui_app.py
query_enhancer.py
retreiver.py
gemini_reranker.py
test_type_balancer.py
improvements.py

outputs
embeddings_gemini_001.npy
faiss_gemini_001.index
bm25_index.pkl
assessments_processed.csv

configs
recommender_config.json
```

## API

Base URL
http colon slash slash localhost colon eight thousand

Health
GET slash health

Recommend
POST slash recommend

Example request

```json
{
  "query": "Java developer with SQL skills",
  "top_k": 10
}
```

Stats
GET slash stats

## Streamlit UI

Job description input panel
Prebuilt templates
Real time results
CSV export
Custom K P ratio slider
Debug mode

## Configuration

Add Gemini API key inside .env
Modify retriever weights and domain boosts in retreiver.py
Update role templates and skill expansion logic in query_enhancer.py

## Performance

Coverage covers five hundred plus assessments
Response time around thirty seconds with reranking
High accuracy for technical and communication based roles
Soft scoring avoids zero results

## Troubleshooting

Activate virtual environment
Reinstall dependencies
Ensure API is running before UI
Verify .env key
Check existence of outputs folder

## Stack

Python
FastAPI
Streamlit
FAISS
BM25
Google Gemini embeddings
LangGraph

## Author

Jitendra Kumar</br>
GitHub: Jittub45</br>
LinkedIn: kumarjitendra1

---


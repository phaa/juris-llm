# Juris-LLM: Legal Question-Answering System with RAG

Generative AI project focused on **legal documents**, such as the Brazillian Federal Constitution of 1988, utilizing a RAG (Retrieval-Augmented Generation) architecture, a local or cloud-based LLM, observability with Prometheus and Grafana, in addition to MLOps with CI/CD, DVC, and MLflow.

## Project Features

- **Smart ingestion and chunking** of legal PDFs
- **Semantic vectorization** with SentenceTransformers
- **Vector storage** with ChromaDB
- **Semantic search** and retrieval with LangChain
- **Response generation** with local LLaMA model (vLLM) or Gemini (Vertex AI)
- **RESTful API** with FastAPI
- **Automated testing** with Pytest and TestClient
- **Monitoring** with Prometheus and Grafana
- **CI/CD** with GitHub Actions and Google Cloud Run
- **MLOps** with DVC + MLflow (in progress)

## Technologies and Tools

| Category | Technologies |
|---|---|
| Vectorization | `sentence-transformers`, `ChromaDB`, `LangChain` |
| LLMs | `vLLM` + `Hugging Face` + `Transformers` or `Vertex AI` (Gemini) |
| Backend API | `FastAPI`, `Pydantic`, `Uvicorn` |
| Containerization | `Docker`, `Docker Compose`, `NVIDIA CUDA Base Image` |
| Testing | `Pytest`, `TestClient`, mocks |
| Observability | `prometheus_client`, `Prometheus`, `Grafana` |
| CI/CD | `GitHub Actions`, `Cloud Run`, `Artifact Registry`, `GCP` |
| MLOps | `DVC`, `MLflow` (coming soon) |

## Folder Structure

```
juris-llm/
│
├── app/                      # Código principal da aplicação FastAPI
│   ├── main.py               # Ponto de entrada da API
│   ├── rag.py                # Lógica do RAG (query + geração)
│   ├── chroma_loader.py      # Carregamento da coleção vetorial
│   ├── models.py             # Modelos Pydantic (Entrada/Saída)
│
├── data/                     # Dados PDF / processados
│
├── scripts/                  # Scripts para chunking e vetorização
│   └── ingest.py
│
├── infra/                    # Infraestrutura (Docker, Prometheus, etc.)
│   ├── Dockerfile.api
│   ├── prometheus.yml
│
├── tests/                    # Testes automatizados
│
├── .github/workflows/        # CI/CD com GitHub Actions
│
├── .env                      # Variáveis de ambiente
├── requirements.txt
└── README.md
```

## Local Installation (with Docker)

```bash
# Clone the repository
git clone [https://github.com/seu-usuario/juris-llm.git](https://github.com/seu-usuario/juris-llm.git)
cd juris-llm

# Create your .env file
cp .env.example .env

# Bring up the services
docker-compose up --build
```

## Testing

```bash
# In the terminal (with activated environment)
pytest
```

## Monitoring

- Access Prometheus at http://localhost:9090
- Access Grafana at http://localhost:3000
  - User: admin
  - Pass: admin
  - Add Prometheus as a data source and create dashboards

## Deploy with CI/CD (Cloud Run)
CI/CD pipeline integrated with GitHub Actions:
- Authenticates with a service account key
- Builds the Docker image
- Pushes to Google Artifact Registry
- Deploys to Cloud Run with defined variables

## LLM Usage

### Local Model
- Using vLLM with CUDA support
- Serves an HTTP endpoint separate from the API

### Model via Vertex AI
- Gemini (preview): gemini-2.5-flash-preview-05-20
- Integration via SDK: google-genai

## Future Extensions
- Web Interface with Streamlit or Next.js
- Database storage (e.g., PostgreSQL + pgvector)
- Caching with Redis
- Authentication with OAuth2
- LLM Fine-tuning

## Author

Pedro Henrique Azevedo  
[LinkedIn](https://www.linkedin.com/in/pedro-henrique-azevedo/) • [GitHub](https://github.com/phazevedo)

## License

This project is licensed under the **MIT License**.

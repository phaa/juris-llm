# Juris-LLM: Sistema de Perguntas e Respostas Jurídico com RAG

Projeto de IA generativa com foco em **documentos jurídicos**, como a Constituição Federal de 1988, utilizando uma arquitetura RAG (Retrieval-Augmented Generation), LLM local ou na nuvem, observabilidade com Prometheus e Grafana, além de MLOps com CI/CD, DVC e MLflow.

## 🚀 Funcionalidades

- ✅ **Ingestão e chunking** inteligente de PDFs jurídicos  
- ✅ **Vetorização semântica** com SentenceTransformers  
- ✅ **Armazenamento vetorial** com ChromaDB  
- ✅ **Busca semântica** e recuperação com LangChain  
- ✅ **Geração de respostas** com modelo LLaMA local (vLLM) ou Gemini (Vertex AI)  
- ✅ **API RESTful** com FastAPI  
- ✅ **Testes automatizados** com Pytest e TestClient  
- ✅ **Monitoramento** com Prometheus e Grafana  
- ✅ **CI/CD** com GitHub Actions e Google Cloud Run  
- ✅ **MLOps** com DVC + MLflow (em progresso)  

## 🛠️ Tecnologias e Ferramentas

| Categoria             | Tecnologias                                                       |
|-----------------------|--------------------------------------------------------------------|
| 🔍 Vetorização         | `sentence-transformers`, `ChromaDB`, `LangChain`                  |
| 🧠 LLMs                | `vLLM` + `Hugging Face` + `Transformers` ou `Vertex AI` (Gemini)  |
| 🧰 Backend API         | `FastAPI`, `Pydantic`, `Uvicorn`                                  |
| 📦 Containerização     | `Docker`, `Docker Compose`, `NVIDIA CUDA Base Image`              |
| 🔬 Testes              | `Pytest`, `TestClient`, mocks                                     |
| 📊 Observabilidade     | `prometheus_client`, `Prometheus`, `Grafana`                      |
| 🔁 CI/CD               | `GitHub Actions`, `Cloud Run`, `Artifact Registry`, `GCP`         |
| 🧪 MLOps               | `DVC`, `MLflow` (em breve)                                        |

## 📂 Estrutura de Pastas

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

## 📦 Instalação Local (com Docker)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/juris-llm.git
cd juris-llm

# Crie seu arquivo .env
cp .env.example .env

# Suba os serviços
docker-compose up --build
```

## 🧪 Testes

```bash
# No terminal (com ambiente ativado)
pytest
```

## 📈 Monitoramento

- Acesse o Prometheus em `http://localhost:9090`
- Acesse o Grafana em `http://localhost:3000`
  - User: `admin`
  - Pass: `admin`
  - Adicione Prometheus como data source e crie dashboards

## ☁️ Deploy com CI/CD (Cloud Run)

Pipeline de CI/CD integrado com GitHub Actions:

- Autentica com chave de service account
- Faz build da imagem Docker
- Faz push para o Google Artifact Registry
- Faz deploy na Cloud Run com variáveis definidas

## 🤖 Uso de LLMs

### Modelo Local

- Usando vLLM com suporte a CUDA
- Serve um endpoint HTTP separado da API

### Modelo via Vertex AI

- Gemini (preview): `gemini-2.5-flash-preview-05-20`
- Integração via SDK: `google-genai`

## 📚 Futuras Extensões

- Interface Web com Streamlit ou Next.js
- Armazenamento em banco de dados (ex: PostgreSQL + pgvector)
- Cache com Redis
- Autenticação com OAuth2
- Fine-tuning de LLM

## 👨‍💻 Autor

Pedro Henrique Azevedo  
[LinkedIn](https://www.linkedin.com/in/pedro-henrique-azevedo/) • [GitHub](https://github.com/phazevedo)

## 📝 Licença

Este projeto está licenciado sob os termos da **MIT License**.
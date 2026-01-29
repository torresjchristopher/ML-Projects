# ML-Projects

A consolidated repository of machine learning projects covering various technologies, architectures, and use cases. Each project is self-contained with complete documentation, tests, and deployment configurations.

## 📚 Projects Overview

### 1. **nlp-fine-tuning-api** 🤖
Fine-tune Transformer models (DistilBERT/BERT) for text classification and deploy as production-ready APIs.
- **Tech Stack**: Python, Transformers, FastAPI, MLflow, Docker
- **Use Case**: Text classification, NLP model deployment
- **Key Features**: Experiment tracking, containerization, CI/CD

### 2. **ml-pipeline** 📊
End-to-end machine learning pipeline with MLOps for tabular data.
- **Tech Stack**: Python, Scikit-learn, MLflow, Pandas, Docker
- **Use Case**: Scalable ML workflows, model training, hyperparameter tuning
- **Key Features**: Data preprocessing, model training, evaluation, reproducibility

### 3. **fastapi-ml-deployment** ⚡
ML model deployment and serving using FastAPI framework.
- **Tech Stack**: FastAPI, Scikit-learn/XGBoost, Docker, Python
- **Use Case**: Model serving, REST API creation
- **Key Features**: Async endpoints, request validation, Docker deployment

### 4. **ruby-ml-sinatra** 💎
Ruby Sinatra web application with integrated ML backend.
- **Tech Stack**: Ruby, Sinatra, Python backend, Flask/FastAPI, TextBlob/Transformers
- **Use Case**: Web app with NLP features
- **Key Features**: Cross-language integration, HTTP communication, ERB/HAML templates

### 5. **rust-data-preprocessing** 🦀
Real-time data preprocessing engine built in Rust.
- **Tech Stack**: Rust, Polars, Serde, CSV, Kafka (or simulated data), Python bridge
- **Use Case**: High-performance data processing
- **Key Features**: Real-time processing, gRPC/FFI integration, Python interoperability

### 6. **retail-sales-forecaster** 📈
Time series forecasting for retail sales predictions.
- **Tech Stack**: Python, Prophet, ARIMA, XGBoost, Pandas, Matplotlib, Scikit-learn
- **Use Case**: Sales prediction, forecasting
- **Key Features**: Multiple forecasting models, visualization, evaluation metrics

### 7. **resume-matcher** 📄
Resume matching system using transformers and semantic similarity.
- **Tech Stack**: Python, spaCy, Transformers, Sentence-Transformers, FAISS/Annoy, Streamlit
- **Use Case**: Resume screening, job matching
- **Key Features**: Semantic search, similarity ranking, web UI

### 8. **sql-python-rdms** 🗄️
Relational Database Management System with Python interface.
- **Tech Stack**: Docker, Python, MySQL, SQL, Mermaid, GraphViz
- **Use Case**: Database design, SQL operations, CRUD applications
- **Key Features**: Data modeling, query optimization, visualization

## 📁 Repository Structure

Each project follows a consistent structure:

```
project-name/
├── README.md                 # Project-specific documentation
├── requirements.txt          # Python dependencies
├── setup.py / pyproject.toml # Project configuration
├── src/                      # Source code
├── tests/                    # Test suite
├── docker/                   # Docker configuration
├── scripts/                  # Utility and setup scripts
└── [language-specific files] # Rust.toml, Gemfile, etc.
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ (for most projects)
- Docker & Docker Compose
- Git

### Clone and Navigate
```bash
git clone https://github.com/torresjchristopher/ML-Projects.git
cd ML-Projects
cd [project-name]
```

### Installation
Each project has its own setup instructions in its README:

```bash
# Example for most Python projects
pip install -r requirements.txt

# For projects with Docker
docker build -t project-name .
docker run -it project-name
```

## 🛠️ Technologies

| Category | Technologies |
|----------|--------------|
| **Languages** | Python, Rust, Ruby, SQL |
| **ML/AI** | Transformers, Scikit-learn, XGBoost, ARIMA, Prophet, spaCy |
| **Web Frameworks** | FastAPI, Sinatra, Flask |
| **Data** | Pandas, Polars, NumPy, Matplotlib, Seaborn |
| **DevOps** | Docker, MLflow, GitHub Actions |
| **Databases** | MySQL, SQLite, Postgres |
| **Tools** | Kafka, FAISS, Streamlit, Jupyter |

## 📖 Documentation

Each project contains:
- **README.md** - Project overview and quick start
- **Documentation/** - Detailed guides (if applicable)
- **Examples/** - Usage examples and notebooks (if applicable)

## 🧪 Testing

Run tests for individual projects:
```bash
cd [project-name]
pytest tests/
# or per-project instructions in README
```

## 🐳 Docker Support

Most projects include Dockerfile and docker-compose.yml:
```bash
cd [project-name]
docker-compose up
```

## 🤝 Contributing

Each project maintains its own contribution guidelines. See individual project READMEs for details.

## 📝 License

Each project may have its own license. Check the individual project LICENSE files.

## ✨ Key Highlights

✅ **Production-Ready**: Code follows best practices and deployment standards  
✅ **Complete**: Each project includes training, testing, and deployment code  
✅ **Documented**: Comprehensive READMEs and inline documentation  
✅ **Tested**: Unit tests and integration tests included  
✅ **Modern Stack**: Uses latest versions of ML and web frameworks  
✅ **MLOps**: Experiment tracking, containerization, CI/CD ready  

## 📚 Learning Resources

These projects demonstrate:
- How to train and deploy ML models in production
- Best practices for reproducible ML pipelines
- Full-stack development with Python and other languages
- DevOps and containerization for ML applications
- Real-world data processing and ML workflows

---

**Last Updated**: January 2025  
**Maintained By**: torresjchristopher

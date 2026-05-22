# NexusIntel

> **Enterprise-Grade Cyber Investigation & Intelligence Platform**

![NexusIntel Banner](./screenshots/banner.png)

[![GitHub Stars](https://img.shields.io/github/stars/xdrew87/nexusintel?style=flat-square&logo=github&color=0FF441)](https://github.com/xdrew87/nexusintel)
[![License: MIT](https://img.shields.io/badge/License-MIT-0FF441?style=flat-square)](./LICENSE)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-0FF441?style=flat-square&logo=python)](https://www.python.org/)
[![React 18+](https://img.shields.io/badge/React-18%2B-0FF441?style=flat-square&logo=react)](https://react.dev/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0FF441?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)

---

## 🎯 What is NexusIntel?

NexusIntel is a **modular, analyst-centric cyber investigation platform** designed for security researchers, SOC analysts, OSINT investigators, and red/blue teams. It correlates infrastructure, maps relationships, builds investigation graphs, and enriches intelligence in a **production-grade environment**.

### Not Just Another Tool
- ❌ Not a simple dashboard
- ❌ Not another generic OSINT scanner
- ❌ Not another SIEM clone

### What It Actually Is
- ✅ An investigation workspace with persistent case management
- ✅ A cyber intelligence correlation engine
- ✅ A relationship & infrastructure mapping system
- ✅ An analyst-focused investigation pivot platform
- ✅ Enterprise-grade with commercial UI/UX

---

## ✨ Key Features

### 🔍 Investigation Workspace
Create and manage investigations with persistent sessions, evidence organization, notes, tags, and pivot tracking.

### 📊 Intelligence Enrichment
Enrich indicators (IPs, domains, URLs, emails, usernames, hashes, ASNs) with:
- DNS resolution & reverse DNS
- WHOIS & ASN data
- TLS certificates
- Subdomain discovery
- Geolocation data
- Technology fingerprinting

### 🌐 Graph Engine
Interactive relationship visualization featuring:
- **Node types:** Domains, IPs, ASNs, certificates, emails, users, hashes, technologies
- **Edge types:** hosted_on, resolves_to, owns, related_to, uses, shares_certificate, shares_asn
- **Capabilities:** Zoom, drag, filter, cluster, export, animated transitions

### 📁 Case Evidence System
Upload and organize evidence:
- Screenshots, JSON, logs, text, CSV files
- Automatic SHA256 hashing
- Metadata preservation
- Timestamp tracking

### 🔗 Threat Intelligence Integrations
Optional API integrations for:
- AbuseIPDB
- Shodan
- Censys
- VirusTotal
- OTX (AlienVault)
- GreyNoise

### 📈 Campaign Clustering
Detect infrastructure relationships via:
- Shared ASN detection
- Certificate correlation
- Hosting provider analysis
- Favicon hash matching

### 📋 Report Generation
Export investigations as:
- Markdown reports
- JSON structures
- Styled HTML documents
- Investigation summaries

### 🔎 Global Search
Search across:
- Indicators
- Cases
- Evidence
- Notes
- Relationships

### ⏱️ Timeline View
Visual investigation timeline showing:
- Analyst pivots
- Evidence uploads
- Enrichment results
- Actions taken

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Async web framework
- **SQLAlchemy** - ORM
- **Pydantic** - Data validation
- **AsyncIO** - Async operations
- **httpx** - Async HTTP client
- **SQLite/PostgreSQL** - Databases

### Frontend
- **React 18** - UI framework
- **Vite** - Build tool
- **TailwindCSS** - Styling
- **Framer Motion** - Animations
- **Cytoscape.js** - Graph visualization
- **React Flow** - Alternative graph library
- **Monaco Editor** - Code editor
- **Zustand** - State management

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Orchestration
- **GitHub Actions** - CI/CD

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Node.js 18+
- Docker & Docker Compose (optional)

### Local Installation

**1. Clone the repository:**
```bash
git clone https://github.com/xdrew87/nexusintel.git
cd nexusintel
```

**2. Backend setup:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python3 -m uvicorn api.main:app --reload
```

Backend runs on `http://localhost:8000`

**3. Frontend setup (new terminal):**
```bash
cd frontend
npm install
npm run dev
```

Frontend runs on `http://localhost:5173`

**4. Access NexusIntel:**
Open `http://localhost:5173` in your browser

### Docker Deployment

```bash
docker-compose up -d
```

This starts:
- Backend (port 8000)
- Frontend (port 5173)
- SQLite database

Visit `http://localhost:5173`

---

## 📖 API Documentation

API docs available at `http://localhost:8000/docs` (Swagger UI)

### Core Endpoints

#### Investigations
```
GET    /api/v1/investigations          - List investigations
POST   /api/v1/investigations          - Create investigation
GET    /api/v1/investigations/{id}     - Get investigation
PUT    /api/v1/investigations/{id}     - Update investigation
DELETE /api/v1/investigations/{id}     - Delete investigation
```

#### Indicators
```
POST   /api/v1/indicators/enrich       - Enrich indicator
GET    /api/v1/indicators/{id}         - Get indicator details
```

#### Graph
```
GET    /api/v1/graph/{investigation_id} - Get graph data
POST   /api/v1/graph/pivot              - Pivot from indicator
```

#### Evidence
```
POST   /api/v1/evidence/upload         - Upload evidence
GET    /api/v1/evidence/{id}           - Get evidence
```

#### Search
```
GET    /api/v1/search?query=...        - Global search
```

---

## 🏗️ Architecture

```
NexusIntel/
├── backend/
│   ├── api/              # REST API routes
│   ├── models/           # SQLAlchemy models
│   ├── services/         # Business logic
│   ├── enrichers/        # Enrichment modules
│   ├── graph/            # Graph engine
│   ├── database/         # DB setup
│   ├── utils/            # Utilities
│   └── main.py          # Entry point
├── frontend/
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── pages/        # Page routes
│   │   ├── hooks/        # Custom hooks
│   │   ├── stores/       # Zustand state
│   │   └── utils/        # Utilities
│   └── public/           # Static assets
├── docs/                 # Documentation
├── docker/              # Docker configs
└── scripts/             # Utility scripts
```

---

## 🔐 Security

NexusIntel implements:
- ✅ Strict input validation
- ✅ Secure file handling with path traversal protection
- ✅ Rate limiting
- ✅ API sanitization
- ✅ Safe async workers
- ✅ CSP headers
- ✅ Secure session handling
- ✅ Environment-based configuration (no hardcoded secrets)

**Never:**
- Exposed API keys
- Hardcoded secrets
- Unrestricted uploads
- Unvalidated user input

See [SECURITY.md](./SECURITY.md) for details.

---

## 🔄 Configuration

Copy `.env.example` to `.env` and configure:

```env
# Database
DATABASE_URL=sqlite:///./nexusintel.db
# DATABASE_URL=postgresql://user:pass@localhost/nexusintel  # PostgreSQL support

# API Keys (optional - leave blank to skip integrations)
SHODAN_API_KEY=
ABUSEIPDB_API_KEY=
VIRUSTOTAL_API_KEY=
CENSYS_API_KEY=
GREYNOISE_API_KEY=

# Features
ENABLE_ENRICHMENT=true
ENABLE_GRAPH_ENGINE=true
ENABLE_AUTONOMOUS_PIVOTING=false

# Server
DEBUG=false
LOG_LEVEL=INFO
```

---

## 🧪 Testing

```bash
cd backend
pytest tests/ -v
pytest tests/ --cov=api  # With coverage
```

```bash
cd frontend
npm test
npm run test:e2e
```

---

## 📚 Documentation

- [Architecture Guide](./docs/ARCHITECTURE.md)
- [API Reference](./docs/API.md)
- [Development Guide](./CONTRIBUTING.md)
- [Security Policy](./SECURITY.md)

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

**Areas for contribution:**
- New enrichment modules
- UI/UX improvements
- Integration modules
- Documentation
- Bug fixes

---

## 📋 Roadmap

### v1.0 (Current)
- ✅ Investigation workspace
- ✅ Intelligence enrichment
- ✅ Graph visualization
- ✅ Evidence management
- ✅ Basic report generation

### v1.1 (Planned)
- 🔄 Campaign clustering automation
- 🔄 Autonomous pivoting engine
- 🔄 Infrastructure heatmaps
- 🔄 Multi-user collaboration

### v1.2 (Future)
- 📋 Investigation sharing & collaboration
- 📋 Advanced visualization options
- 📋 Custom enrichment modules
- 📋 Cloud deployment templates

---

## ⚖️ License

This project is licensed under the **MIT License** - see [LICENSE](./LICENSE) for details.

### ⚠️ Disclaimer

NexusIntel is provided for **authorized security research and testing only**. Unauthorized access, data collection, or use against systems you don't own or have permission to test is illegal. Users are solely responsible for ensuring lawful use.

---

## 👤 Author

**xdrew87** - Cybersecurity Researcher & OSINT Specialist

- GitHub: [@xdrew87](https://github.com/xdrew87)
- Focus: Enterprise security, OSINT, infrastructure investigation

---

## 📞 Support & Contact

- **Issues:** GitHub Issues for bugs and features
- **Discussions:** GitHub Discussions for questions
- **Documentation:** See `/docs` folder

---

## 🙏 Acknowledgments

Inspired by:
- Palantir Gotham
- Maltego
- Elastic Security
- Recorded Future
- Microsoft Sentinel

---

**Built with ❤️ for the security research community**

# ⚡ OmniResearch AI — Autonomous Multi-Agent Deep Research & Intelligence Engine

[![CI](https://github.com/your-username/omni-research-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/omni-research-agent/actions)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
[![Agent Architecture](https://img.shields.io/badge/Agentic-ReAct%20%2B%20Critic%20Loop-orange.svg)](#system-architecture)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Submission for Agentic AI Hackathon 2026**  
> An autonomous multi-agent deep research engine that plans investigations, executes grounded web queries, subjects findings to an adversarial peer-review critic, and synthesizes publication-grade executive whitepapers with live telemetry streaming.

---

## 🌟 Overview & Why This Stands Out

Traditional chatbots process queries in a single, monolithic, ungrounded step—leading to hallucinations, superficial answers, and zero verification.

**OmniResearch AI** implements true **Agentic AI design patterns**:
1. **Hierarchical Task Decomposition**: Deconstructs high-level research objectives into a directed acyclic graph (DAG) of investigative sub-tasks.
2. **Autonomous Tool Calling**: Leverages real-time search and web scraping tools with domain-level credibility scoring.
3. **Adversarial Self-Correction Loop**: An independent **Critic Agent** audits gathered claims, evaluates source consensus, identifies blind spots, and triggers remediation loops if data is insufficient.
4. **Live Observability Stream**: Emits real-time Server-Sent Events (SSE) detailing agent thoughts, tool dispatches, critique verdicts, and milestone completions.
5. **Zero-Friction Evaluator Mode**: Features a high-fidelity **Mock Engine** that allows hackathon evaluators to test the complete multi-agent pipeline immediately without configuring an API key.

---

## 🏗️ System Architecture

```mermaid
graph TD
    User([User Research Topic]) --> UI[Web Dashboard / CLI]
    UI --> API[FastAPI Orchestration Hub]
    
    subgraph MultiAgentEngine [OmniResearch Autonomous Core]
        API --> Orchestrator[📋 Agent 01: Lead Planner]
        Orchestrator -->|Dynamic Task DAG| Researcher[🔍 Agent 02: Web Explorer]
        
        subgraph ToolExecution [Tool Layer]
            Researcher -->|Tool Call| SearchTool[Search Engine (DuckDuckGo / Tavily)]
            Researcher -->|Tool Call| ScraperTool[Web Scraper & Content Distiller]
            SearchTool -->|Citations & Snippets| Researcher
            ScraperTool -->|Extracted Text| Researcher
        end
        
        Researcher -->|Aggregated Evidence| Critic[⚖️ Agent 03: Fact-Checker Critic]
        
        Critic -->|Gap Analysis / Rejection| Orchestrator
        Critic -->|Approved Factual Evidence| Synthesizer[✍️ Agent 04: Report Synthesizer]
        
        Synthesizer -->|Structured Executive Whitepaper| API
    end
    
    API -->|Live SSE Telemetry Stream| UI
    API --> Export[Markdown / PDF / JSON Export]
```

---

## 🤖 The 4 Autonomous Agents

| Agent | Role | Capabilities & Responsibilities |
| :--- | :--- | :--- |
| **📋 Lead Planner** *(Orchestrator)* | Strategy & Decomposition | Analyzes research intent, breaks topics into structured sub-tasks with targeted search strategies, and refines tasks upon receiving Critic feedback. |
| **🔍 Web Explorer** *(Researcher)* | Information Retrieval | Dispatches autonomous queries to search engines and web scrapers, distills raw HTML, extracts snippets, and assigns credibility ratings. |
| **⚖️ Fact-Checker** *(Critic)* | Verification & Reflection | Audits gathered claims against source citations, calculates verification scores, identifies coverage gaps, and triggers follow-up research. |
| **✍️ Report Synthesizer** *(Writer)* | Synthesis & Publication | Compiles multi-module evidence into structured Markdown reports featuring executive summaries, comparative benchmark tables, Mermaid diagrams, and bibliographies. |

---

## 🚀 Quick Start (Under 60 Seconds)

### 1. Clone & Install
```bash
git clone https://github.com/your-username/omni-research-agent.git
cd omni-research-agent

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Interactive Web Dashboard
```bash
python main.py
```
👉 Open your browser at **`http://127.0.0.1:8000`**!

> [!TIP]
> **Zero API Key Needed for Demos**: By default, OmniResearch AI runs with the built-in high-fidelity **Mock Engine**, allowing hackathon judges to evaluate the UI, telemetry streaming, agent loops, and markdown generation instantly.

---

### 3. Run via Terminal CLI
```bash
python main.py --cli --topic "Post-Quantum Cryptography and Migration Strategies"
```

---

## ⚙️ Pluggable LLM Providers

OmniResearch AI is provider-agnostic. Switch models easily via environment variables:

```bash
cp .env.example .env
```

Edit `.env` to configure your preferred backend:

### Google Gemini (Recommended)
```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-1.5-flash
```

### OpenAI
```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

### Groq (Ultra-Fast)
```env
LLM_PROVIDER=groq
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

### Local Ollama (100% Offline & Private)
```env
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3
```

---

## 🧪 Testing & Verification

Run the automated test suite with pytest:

```bash
pytest -v tests/
```

All agent planning routines, tool invocations, critic evaluations, and end-to-end multi-agent pipelines are covered by automated unit tests.

---

## 📁 Project Structure

```
omni-research-agent/
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI matrix testing
├── src/
│   ├── agents/
│   │   ├── base.py              # Base agent & event emitter
│   │   ├── orchestrator.py      # Lead Planner agent
│   │   ├── researcher.py        # Web Explorer agent
│   │   ├── critic.py            # Fact-Checker critic agent
│   │   └── synthesizer.py       # Report Synthesizer agent
│   ├── api/
│   │   └── server.py            # FastAPI & SSE live streaming
│   ├── llm/
│   │   └── provider.py          # Unified LLM provider adapter
│   ├── models/
│   │   └── schema.py            # Pydantic data contracts
│   ├── tools/
│   │   ├── scraper.py           # Content extraction & cleaning
│   │   └── search.py            # Search engine & citations
│   ├── ui/
│   │   └── static/
│   │       ├── app.js           # Live telemetry & Mermaid renderer
│   │       ├── index.html       # Modern Glassmorphic dashboard
│   │       └── style.css        # Custom animations & theme
│   ├── cli.py                   # Rich terminal runner
│   └── pipeline.py              # Multi-agent orchestrator coordinator
├── tests/
│   └── test_agents.py           # Pytest test suite
├── .env.example                 # Configuration template
├── .gitignore                   # Git hygiene
├── main.py                      # Single-command launcher
├── pyproject.toml               # Python package configuration
├── requirements.txt             # Clean, lightweight dependencies
└── README.md                    # Project documentation
```

---

## 🎯 Evaluator Rubric Alignment

| Hackathon Criterion | How OmniResearch AI Delivers |
| :--- | :--- |
| **Agentic Autonomy** | Implements autonomous DAG task decomposition, asynchronous tool calling, and self-directed execution without hardcoded linear scripts. |
| **Iterative Reflection** | Features an explicit **Critic Agent** that peer-reviews findings, scores factual grounding, and triggers self-correction loops. |
| **Observability** | Real-time SSE telemetry stream exposes agent thoughts, tool payloads, and status transitions visually in the web dashboard. |
| **Code Quality & Reliability** | Strongly typed Pydantic models, modular architecture, comprehensive pytest suite, and GitHub Actions CI. |
| **Evaluator Experience** | Works out-of-the-box in zero-config demo mode with a single command: `python main.py`. |

---

## 📄 License
Released under the [MIT License](LICENSE).

# ⚡ High-Throughput FinTech Analytics Ledger Engine

An enterprise-grade financial ingestion engine designed to process, optimize, and store massive transaction event streams (simulating 8 Crore / 80 Million records) under strict memory boundaries.

---

## 🚨 The Problem Statement
Traditional data analytic pipelines crumble when forced to process multi-million record event streams simultaneously. Standard extraction methods pull entire raw datasets directly into application memory, triggering catastrophic Out-of-Memory (OOM) system failures. 

Furthermore, naive data processing engines suffer from severe latency bottlenecks caused by Python's slow internal row-by-row looping structures. When these unoptimized data layers dump raw, unindexed flat tables straight into storage, relational warehouses choke during business-critical analytical reporting queries.

## 🎯 Project Achievements & Deliverables
*   **Zero Memory Crashes (OOM Prevention):** The ingestion tier uses strict data streaming block gates, keeping the server RAM footprint completely flat whether processing 10,000 rows or 80,000,000 rows.
*   **50% Computational Storage Reductions:** By executing strict downcasting rules on primitive numeric allocations, the database engine halves the active memory consumption required to process transaction lines.
*   **Sub-Second Analytical Query Latency:** Decomposing flat ledger tables into an optimized relational Star Schema with customized B-Tree Indexes removes structural storage bottlenecks, unlocking real-time performance on complex data joins.
*   **100% Data Lineage Auditing (Zero Record Loss):** Integrated data observability checkpoints run automated post-load reconciliation metrics, verifying that every single memory event safely commits to physical disk blocks with no dropouts.

---

## 📁 Repository Directory Structure

```text
high-throughput-ledger/
│
├── config/
│   └── database_settings.yaml     # Connection configurations and chunk-size limits
│
├── src/
│   ├── __init__.py
│   ├── schema_provisioner.py      # SQL DDL schemas for Fact and Dimension tables
│   ├── ingestion_engine.py        # Stream processing generators & batch-chunking logic
│   ├── transformation_core.py     # NumPy type-downcasting & matrix vector processing
│   └── observability_audit.py     # Post-load verification checkpoints & reconciliation
│
├── orchestration/
│   └── ledger_pipeline_dag.py     # Apache Airflow orchestration workflow parameters
│
├── tests/
│   └── test_pipeline_lineage.py   # Automated schema, type, and data integrity unit tests
│
├── README.md                      # Problem statement, architecture maps, and metrics
└── requirements.txt               # System package dependencies (pandas, numpy, sqlalchemy)

⚙️ Core Data Pipeline Architecture
The end-to-end data processing workflow moves sequentially through 4 highly optimized execution steps:

[ Raw Stream Generator ]
             │
             ▼
 1. INGESTION (src/ingestion_engine.py)
    └─ Memory-safe Python Generator streams data row-by-row
    └─ Groups rows into fixed micro-batches of 100,000 records
             │
             ▼
 2. TRANSFORMATION (src/transformation_core.py)
    └─ Converts raw arrays into vectorized Pandas Matrix
    └─ Forces 64-bit to 32-bit Type-Downcasting (int32, float32)
             │
             ▼
 3. STORAGE LAYER (src/schema_provisioner.py)
    └─ Writes optimized blocks into localized Star Schema DB
    └─ Applies B-Tree indexing on primary join keys
             │
             ▼
 4. OBSERVABILITY AUDIT (src/observability_audit.py)
    └─ Reconciles (Staged Memory Row Count == Saved Database Row Count)
    └─ Raises immediate failure warnings if data loss occurs
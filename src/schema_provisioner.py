import sqlite3
import os

def initialize_warehouse(db_path):
    """
    Creates the optimized Star Schema tables and applies B-Tree indexing
    to handle high-volume transaction analysis locally.
    """
    print(f"Connecting to database target: {db_path}...")
    
    # Establish a local database connection file on your hard drive
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. Build the Dimension Metadata Layer (Stores Account Info)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dim_accounts (
        account_id INTEGER PRIMARY KEY,
        account_tier TEXT NOT NULL,
        risk_score REAL NOT NULL CHECK(risk_score >= 0.0 AND risk_score <= 1.0)
    );
    """)
    
    # 2. Build the High-Volume Core Fact Layer (Stores Every Transaction Event)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fact_ledger_transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        transaction_type TEXT NOT NULL CHECK(transaction_type IN ('DEBIT', 'CREDIT')),
        execution_timestamp TEXT NOT NULL,
        FOREIGN KEY (account_id) REFERENCES dim_accounts(account_id)
    );
    """)
    
    # 3. Apply the Performance-Engineering B-Tree Index Group
    print("Applying compound B-Tree indices for sub-second lookup performance...")
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_ledger_account_time 
    ON fact_ledger_transactions (account_id, execution_timestamp);
    """)
    
    conn.commit()
    conn.close()
    print("🚀 Relational warehouse schema successfully initialized and indexed on disk!")

if __name__ == "__main__":
    # Test execution path using our default database target path
    TARGET_DB = "storage_warehouse.db"
    initialize_warehouse(TARGET_DB)
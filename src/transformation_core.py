import pandas as pd
import numpy as np

def optimize_and_transform_chunk(raw_chunk):
    """
    Transforms a raw block of record dicts into a structured DataFrame,
    forcing downcasting on numerical columns to minimize system RAM usage.
    """
    # 1. Load the structured block into a temporary working matrix
    df = pd.DataFrame(raw_chunk)
    
    if df.empty:
        return df, 0.0, 0.0, 0.0

    # Record the memory usage prior to optimization checks
    initial_memory = df.memory_usage(deep=True).sum() / 1024
    
    # 2. Execute Downcasting Strategy (Force 64-bit to 32-bit types)
    if 'account_id' in df.columns:
        df['account_id'] = df['account_id'].astype(np.int32)
        
    if 'amount' in df.columns:
        df['amount'] = df['amount'].astype(np.float32)
        
    # 3. Standardize text strings into optimized categoricals or clean formats
    if 'transaction_type' in df.columns:
        df['transaction_type'] = df['transaction_type'].astype('category')

    # Record the memory usage post-optimization
    optimized_memory = df.memory_usage(deep=True).sum() / 1024
    savings = initial_memory - optimized_memory

    return df, initial_memory, optimized_memory, savings

if __name__ == "__main__":
    print("Testing memory downcasting core...")
    
    # Create a dense sample array to simulate incoming data rows
    mock_data = [
        {"account_id": 4999, "amount": 1500.75, "transaction_type": "DEBIT", "execution_timestamp": "2026-06-24 10:00:00"}
        for _ in range(50000)
    ]
    
    # Execute the transformation matrix test
    df_optimized, before_kb, after_kb, saved_kb = optimize_and_transform_chunk(mock_data)
    
    print(f"  Matrix Scaling Audit Report:")
    print(f"   - RAM Footprint Before: {before_kb:.2f} KB")
    print(f"   - RAM Footprint After:  {after_kb:.2f} KB")
    print(f"   - Total Clean System Savings: {saved_kb:.2f} KB")
    print("\nTransformation data typing layer is fully optimized!")
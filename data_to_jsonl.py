import json
import duckdb

def stream_parquet_to_jsonl(parquet_file, jsonl_file):
    con = duckdb.connect(database=':memory:')  # load in-memory
    query = f"SELECT * FROM '{parquet_file}'"
    
    with open(jsonl_file, 'w') as f:
        result = con.execute(query)
        column_names = [desc[0] for desc in result.description]  
        for row in result.fetchall():
            json_row = json.dumps(dict(zip(column_names, row)))
            f.write(f"{json_row}\n")
    con.close()  
    print("Conversion completed successfully!")

if __name__ == "__main__":
    import time
    import psutil
    
    parquet_file = 'train-00000-of-00005.parquet'
    jsonl_file = 'train-00000-of-00005.jsonl'

    mb_divisor = 1024 ** 2 # MB of memory
    
    start_time = time.perf_counter()
    start_memory = psutil.Process().memory_info().rss / mb_divisor
    
    stream_parquet_to_jsonl(parquet_file, jsonl_file)
    
    end_time = time.perf_counter()
    end_memory = psutil.Process().memory_info().rss / mb_divisor
    
    execution_time = end_time - start_time
    memory_used = end_memory - start_memory
    
    print(f"Conversion completed in {execution_time:.3f} seconds.")
    print(f"Memory usage: {memory_used:.2f} MB")

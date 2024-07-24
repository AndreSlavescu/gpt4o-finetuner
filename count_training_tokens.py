import duckdb
import tiktoken

def count_tokens_in_jsonl(jsonl_file):
    tokenizer = tiktoken.get_encoding("cl100k_base")
    
    con = duckdb.connect(database=':memory:')
    con.execute(f"CREATE TABLE data AS SELECT * FROM read_json_auto('{jsonl_file}')")
    rows = con.execute("SELECT problem, solution FROM data").fetchall()
    
    total_tokens = 0
    for problem, solution in rows:
        total_tokens += len(tokenizer.encode(problem)) + len(tokenizer.encode(solution))
    
    con.close()
    return total_tokens

if __name__ == "__main__":
    import time
    import psutil
    
    jsonl_file = 'train-00000-of-00005.jsonl'
    
    mb_divisor = 1024 ** 2  # MB of memory
    
    start_time = time.perf_counter()
    start_memory = psutil.Process().memory_info().rss / mb_divisor
    
    token_count = count_tokens_in_jsonl(jsonl_file)
    
    end_time = time.perf_counter()
    end_memory = psutil.Process().memory_info().rss / mb_divisor
    
    execution_time = end_time - start_time
    memory_used = end_memory - start_memory
    
    print(f"Total number of tokens in the training data: {token_count}")
    print(f"Execution time: {execution_time:.3f} seconds")
    print(f"Memory usage: {memory_used:.2f} MB")

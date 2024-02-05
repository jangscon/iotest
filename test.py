import time

def write_large_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def read_large_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def measure_io_throughput(file_path):
    # 대량의 데이터 생성 (예: 100MB 데이터)
    large_data = "A" * (100 * 1024 * 1024)

    # 파일 쓰기 성능 측정
    start_write_time = time.time()
    write_large_file(file_path, large_data)
    end_write_time = time.time()
    write_elapsed_time = end_write_time - start_write_time
    write_throughput = len(large_data) / write_elapsed_time / (1024 * 1024)  # MB/s
    print(f"쓰기 성능: {write_throughput:.2f} MB/s")

    # 파일 읽기 성능 측정
    start_read_time = time.time()
    read_data = read_large_file(file_path)
    end_read_time = time.time()
    read_elapsed_time = end_read_time - start_read_time
    read_throughput = len(read_data) / read_elapsed_time / (1024 * 1024)  # MB/s
    print(f"읽기 성능: {read_throughput:.2f} MB/s")

# 성능 측정 실행
measure_io_throughput("uploads/test_file.txt")

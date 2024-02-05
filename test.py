import time
import os

def write_large_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def read_large_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def measure_io_throughput(file_size, webdav_file_path,local_file_path, iter_num):
    # 대량의 데이터 생성 (예: 100MB 데이터)
    large_data = "A" * file_size
    total_throughputs = [0,0,0,0]
    for i in range(iter_num) : 

        # 파일 쓰기 성능 측정
        start_write_time = time.time()
        write_large_file(webdav_file_path, large_data)
        end_write_time = time.time()
        write_elapsed_time = end_write_time - start_write_time
        write_throughput = len(large_data) / write_elapsed_time / (1024 * 1024)  # MB/s
        print(f"webdav 쓰기 성능: {write_throughput:.2f} MB/s")
        total_throughputs[0] += write_throughput

        # 파일 읽기 성능 측정
        start_read_time = time.time()
        read_data = read_large_file(webdav_file_path)
        end_read_time = time.time()
        read_elapsed_time = end_read_time - start_read_time
        read_throughput = len(read_data) / read_elapsed_time / (1024 * 1024)  # MB/s
        print(f"webdav 읽기 성능: {read_throughput:.2f} MB/s")
        total_throughputs[1] += read_throughput

        os.remove(webdav_file_path)

            # 파일 쓰기 성능 측정
        start_write_time = time.time()
        write_large_file(local_file_path, large_data)
        end_write_time = time.time()
        write_elapsed_time = end_write_time - start_write_time
        write_throughput = len(large_data) / write_elapsed_time / (1024 * 1024)  # MB/s
        print(f"local 쓰기 성능: {write_throughput:.2f} MB/s")
        total_throughputs[2] += write_throughput

        # 파일 읽기 성능 측정
        start_read_time = time.time()
        read_data = read_large_file(local_file_path)
        end_read_time = time.time()
        read_elapsed_time = end_read_time - start_read_time
        read_throughput = len(read_data) / read_elapsed_time / (1024 * 1024)  # MB/s
        print(f"local 읽기 성능: {read_throughput:.2f} MB/s")
        total_throughputs[3] += read_throughput

        os.remove(local_file_path)
    
    print("===================================")
    print(f"webdav 쓰기 성능: {(total_throughputs[0]/iter_num):.2f} MB/s")
    print(f"webdav 읽기 성능: {(total_throughputs[1]/iter_num):.2f} MB/s")
    print(f"local 쓰기 성능: {(total_throughputs[2]/iter_num):.2f} MB/s")
    print(f"local 읽기 성능: {(total_throughputs[3]/iter_num):.2f} MB/s")
    print("===================================")

# 성능 측정 실행
measure_io_throughput((100 * 1024 * 1024),"uploads/test_file.txt","test_file.txt",3)

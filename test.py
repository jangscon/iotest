import time
import os
import sys

def write_large_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def read_large_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def convert_to_readable(size_bytes):
    """
    바이트 단위로 된 파일 크기를 "GB" 또는 "MB"와 같은 읽기 쉬운 형식으로 변환합니다.
    """
    size_gb = size_bytes / (1024 ** 3)
    if size_gb >= 1:
        return f"{size_gb:.2f}GB"
    
    size_mb = size_bytes / (1024 ** 2)
    return f"{size_mb:.2f}MB"



def measure_io_throughput(file_size, webdav_file_path,local_file_path, log_file_path, iter_num):
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
        total_throughputs[0] += write_throughput

        # 파일 읽기 성능 측정
        start_read_time = time.time()
        read_data = read_large_file(webdav_file_path)
        end_read_time = time.time()
        read_elapsed_time = end_read_time - start_read_time
        read_throughput = len(read_data) / read_elapsed_time / (1024 * 1024)  # MB/s
        total_throughputs[1] += read_throughput

        os.remove(webdav_file_path)

            # 파일 쓰기 성능 측정
        start_write_time = time.time()
        write_large_file(local_file_path, large_data)
        end_write_time = time.time()
        write_elapsed_time = end_write_time - start_write_time
        write_throughput = len(large_data) / write_elapsed_time / (1024 * 1024)  # MB/s
        total_throughputs[2] += write_throughput

        # 파일 읽기 성능 측정
        start_read_time = time.time()
        read_data = read_large_file(local_file_path)
        end_read_time = time.time()
        read_elapsed_time = end_read_time - start_read_time
        read_throughput = len(read_data) / read_elapsed_time / (1024 * 1024)  # MB/s
        total_throughputs[3] += read_throughput

        os.remove(local_file_path)
    
    print(f"{(total_throughputs[0]/iter_num):.2f} {(total_throughputs[1]/iter_num):.2f} {(total_throughputs[2]/iter_num):.2f} {(total_throughputs[3]/iter_num):.2f}")
    
    with open(log_file_path, 'a') as file:
        file.write("===================================")
        file.write(f"{convert_to_readable(file_size)} x {iter_num}")
        file.write(f"{(total_throughputs[0]/iter_num):.2f} {(total_throughputs[1]/iter_num):.2f} {(total_throughputs[2]/iter_num):.2f} {(total_throughputs[3]/iter_num):.2f}")
        file.write("===================================\n")

# 성능 측정 실행

def convert_to_bytes(file_size):
    size_unit = file_size[-2:].upper()
    size_value = int(file_size[:-2])

    if size_unit == "GB":
        return size_value * (1024 ** 3)
    elif size_unit == "MB":
        return size_value * (1024 ** 2)
    else:
        raise ValueError("지원되지 않는 크기 단위입니다. (지원 단위: GB, MB)")

if __name__ == "__main__":
    
    parameters = sys.argv[1:]
    
    file_size = convert_to_bytes(parameters[0])
    iter_num = parameters[1]
    webdav_file_path = "uploads/test_file.txt"
    local_file_path = "test_file.txt"
    log_file_path = "io_log.txt"
    
    measure_io_throughput(file_size,
                          webdav_file_path,
                          local_file_path,
                          log_file_path,
                          iter_num)

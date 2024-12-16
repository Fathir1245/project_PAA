# F55123040 Moh. Faathir Ash Shaff
import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value=100, seed=None):
    if seed is not None:
        random.seed(seed)  
    return [random.randint(1, max_value) for _ in range(n)]

def is_unique(array):
    seen = set()  
    for num in array:
        if num in seen:  
            return False
        seen.add(num)  
    return True

def measure_time(func, *args):
    start_time = time.perf_counter()  
    func(*args)  
    end_time = time.perf_counter()  
    return end_time - start_time  

def measure_average_time(func, *args, runs=5):
    times = [measure_time(func, *args) for _ in range(runs)]
    return sum(times) / len(times)  

def validate_input(n, max_value):
    if n <= 0:
        raise ValueError("Ukuran array (n) harus lebih besar dari 0.")
    if max_value <= 0:
        raise ValueError("Nilai maksimum harus lebih besar dari 0.")

def main():
    ns = [100, 150, 200, 250, 300, 350, 400, 500]  
    max_value = 250 - 40  

    worst_case_times = []  
    average_case_times = []  

    for n in ns:
        validate_input(n, max_value)  
        array = generate_array(n, max_value, seed=42)
        worst_case_array = [1] * n
        worst_case_time = measure_average_time(is_unique, worst_case_array)
        average_case_time = measure_average_time(is_unique, array)
        worst_case_times.append(worst_case_time)
        average_case_times.append(average_case_time)
        print(f"n = {n}, Array Unik: {is_unique(array)}, "
              f"Waktu Kasus Terburuk = {worst_case_time:.10f}s, "
              f"Waktu Kasus Rata-Rata = {average_case_time:.10f}s")

    plt.figure(figsize=(10, 6))
    plt.plot(ns, worst_case_times, marker='o', label='Kasus Terburuk', color='red', linestyle='--')
    plt.plot(ns, average_case_times, marker='s', label='Kasus Rata-Rata', color='blue', linestyle='-.')
    plt.title('Perbandingan Performa: Kasus Terburuk vs Kasus Rata-Rata', fontsize=14)
    plt.xlabel('Ukuran Array (n)', fontsize=12)
    plt.ylabel('Waktu Eksekusi (detik)', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

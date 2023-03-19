# python3

def parallel_processing(n, m, data):
    output = []
    next = 0
    time = [0] * n
    for i in range(m):
        thread = next
        start_time = time[thread]
        end_time = start_time + data[i]
        time[thread] = end_time
        next = (next + 1) % n
        output.append((thread, start_time))
    return output

def main():
    n , m = map(int, input(">:: \t").split())
    data = list(map(int, input(">:: \t").split()))
    result = parallel_processing(n,m,data)
    for i,j in result:
        print(i, j)

if __name__ == "__main__":
    main()

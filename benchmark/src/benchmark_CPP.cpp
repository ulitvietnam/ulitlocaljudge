#include <iostream>
#include <chrono>
#include <iomanip>

int main() {
    volatile int count = 0;
    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < 100000000; ++i) {
        count += 1;
    }
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << std::fixed << std::setprecision(10) << elapsed.count();
    return 0;
}
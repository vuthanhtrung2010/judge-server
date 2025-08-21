from dmoj.executors.c_like_executor import CPPExecutor, GCCMixin


class Executor(GCCMixin, CPPExecutor):
    command = 'g++23'
    command_paths = ['g++-15', 'g++']
    std = 'c++23'
    test_program = """
#include <iostream>

#if __cplusplus >= 202302L
int main() {
    std::cout << std::cin.rdbuf();
    return 0;
}
#endif
"""

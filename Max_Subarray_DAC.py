import streamlit as st
import timeit

def max_subarray_divide_conquer(arr):

    def find_max_crossing_subarray(arr, first, mid_point, last):
        Sum_from_Left = float('-inf')
        MaxSum_Left = 0
        MaxSum_Right = 0
        Sum = 0

        for j in range(mid_point, first - 1, -1):
            Sum += arr[j]
            if Sum > Sum_from_Left:
                Sum_from_Left = Sum
                MaxSum_Left = j

        Sum_from_Right = float('-inf')
        Sum = 0

        for k in range(mid_point + 1, last + 1):
            Sum += arr[k]
            if Sum > Sum_from_Right:
                Sum_from_Right = Sum
                MaxSum_Right = k

        return MaxSum_Left, MaxSum_Right, Sum_from_Left + Sum_from_Right

    def find_max_subarray(arr, first, last):
        if first == last:
            return first, last, arr[first]

        mid_point = (first + last) // 2

        left_first, left_last, Sum_from_Left = find_max_subarray(arr, first, mid_point)
        right_first, right_last, Sum_from_Right = find_max_subarray(arr, mid_point + 1, last)
        cross_first, cross_last, cross_sum = find_max_crossing_subarray(arr, first, mid_point, last)

        if Sum_from_Left >= Sum_from_Right and Sum_from_Left >= cross_sum:
            return left_first, left_last, Sum_from_Left
        elif Sum_from_Right >= Sum_from_Left and Sum_from_Right >= cross_sum:
            return right_first, right_last, Sum_from_Right
        else:
            return cross_first, cross_last, cross_sum

    first, last, max_sum = find_max_subarray(arr, 0, len(arr) - 1)
    return max_sum

def max_subarray_brute_force(arr):
    max_sum = float('-inf')
    start = 0
    end = 0

    for j in range(len(arr)):
        current_sum = 0
        for k in range(j, len(arr)):
            current_sum += arr[k]
            if current_sum > max_sum:
                max_sum = current_sum
                start = j
                end = k

    return max_sum

def max_subarray_dynamic_programming(arr):
    max_so_far = float('-inf')
    max_ending_here = 0

    for j in range(len(arr)):
        max_ending_here = max(arr[j], max_ending_here + arr[j])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

def kadanes_algorithm(arr):
    max_so_far = float('-inf')
    max_ending_here = 0
    start = 0
    end = 0
    temp_start = 0

    for j in range(len(arr)):
        max_ending_here += arr[j]

        if max_ending_here < 0:
            max_ending_here = 0
            temp_start = j + 1

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = j

    return max_so_far


def get_running_time(algorithm, arr):
    running_time = timeit.timeit(lambda: algorithm(arr), number=1)
    return running_time



def main():
    st.title("Maximum Subarray Sum Algorithms")

    algorithms = {
        "Divide and Conquer": max_subarray_divide_conquer,
        "Brute Force": max_subarray_brute_force,
        "Dynamic Programming": max_subarray_dynamic_programming,
        "Kadane's Algorithm": kadanes_algorithm
    }

    # Input array
    arr = st.text_input("Enter the array (space-separated):")
    arr = list(map(int, arr.split( )))


    # Algorithm selection
    selected_algorithm = st.selectbox("Select algorithm:", list(algorithms.keys()))

    # Calculate and display maximum subarray sum
    if st.button("Calculate MaxSum"):
        algorithm = algorithms[selected_algorithm]
        max_sum = algorithm(arr)
        st.write("Maximum Subarray Sum:", max_sum)


    def theoretical_time_complexity(algorithm):
        if algorithm == max_subarray_divide_conquer:
            return "O(n log n)"
        elif algorithm == max_subarray_brute_force:
             return "O( n^2)"

        elif algorithm ==max_subarray_dynamic_programming:
            return "O( n )"
        elif algorithm == kadanes_algorithm:
            return "O( n )"


    # Display running time complexity and theoretical time complexity
    if st.button("Show Time Complexity"):
        algorithm = algorithms[selected_algorithm]
        running_time = get_running_time(algorithm, arr)
        theoretical_complexity = theoretical_time_complexity(algorithm)

        st.write("Running Time Complexity:", running_time*1000, "msec")
        st.write("Theoretical Time Complexity:", theoretical_complexity)

if __name__ == "__main__":
    main()
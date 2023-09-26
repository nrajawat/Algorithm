import streamlit as st
import time

def max_subarray_using_Divide_and_Conquer(arr):
    # Divide and conquer approach for maximum subarray problem
    def max_subarray(arr, low, high):
        if low == high:
            return low, high, arr[low]

        mid = (low + high) // 2

        left_low, left_high, left_sum = max_subarray(arr, low, mid)
        right_low, right_high, right_sum = max_subarray(arr, mid + 1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

    def max_crossing_subarray(arr, low, mid, high):
        left_sum = float('-inf')
        sum = 0
        max_left = 0
        for i in range(mid, low - 1, -1):
            sum += arr[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i

        right_sum = float('-inf')
        sum = 0
        max_right = 0
        for i in range(mid + 1, high + 1):
            sum += arr[i]
            if sum > right_sum:
                right_sum = sum
                max_right = i

        return max_left, max_right, left_sum + right_sum

    return max_subarray(arr, 0, len(arr) - 1)


def max_subarray_using_Brute_Force(arr):
    # Brute force approach for maximum subarray problem
    max_sum = float('-inf')
    n = len(arr)
    start_index = 0
    end_index = 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start_index = i
                end_index = j

    return start_index, end_index, max_sum


def max_subarray_using_Dynamic_Programming(arr):
    # Dynamic programming approach for maximum subarray problem
    max_sum = arr[0]
    current_sum = arr[0]
    start_index = 0
    end_index = 0
    temp_index = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            temp_index = i

        current_sum = max(arr[i], current_sum + arr[i])

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = temp_index
            end_index = i

    return start_index, end_index, max_sum


# Streamlit UI code
st.title("Maximum Subarray Problem")
st.write("Calculate the time complexity of different approaches for the maximum subarray problem.")
# Input array
arr = st.text_input("Enter the array (space-separated integers):")
arr = list(map(int, arr.split()))

# Algorithm selection
algorithm = st.selectbox("Select algorithm", ["Divide and Conquer", "Brute Force", "Dynamic Programming"])

# Convert input to array
#arr = [int(x) for x in arr.split()]
find_button = st.button("Find Maximum Subarray")
# Calculate maximum subarray using the selected algorithm and measure time complexityaximum subarray using the selected algorithm and measure time complexity
calculate_button = st.button("Calculate Time Complexity")


if calculate_button and arr:
    #arr = list(map(int, arr.split()))

    if algorithm == "Divide and Conquer":
        start_time = time.time()
        start_index, end_index, max_sum = max_subarray_using_Divide_and_Conquer(arr)
        DC_time = time.time() - start_time

    elif algorithm == "Brute Force":
        start_time = time.time()
        start_index, end_index, max_sum = max_subarray_using_Brute_Force(arr)
        BF_time = time.time() - start_time

    elif algorithm == "Dynamic Programming":
        start_time = time.time()
        start_index, end_index, max_sum = max_subarray_using_Dynamic_Programming(arr)
        DP_time = time.time() - start_time



    end_time = time.time()
    time_taken = ( end_time - start_time )*1000

    st.write("Time Complexity:")
    st.write("Divide and Conquer:", DC_time, "seconds")
    st.write("Brute Force:", BF_time, "seconds")
    st.write("Dynamic Programming:", DP_time, "seconds")

    st.write("Start Index:", start_index)
    st.write("End Index:", end_index)
    st.write("Maximum Sum:", max_sum)
    st.write("Time Taken:",f"{time_taken:.2f}", "milliseconds")

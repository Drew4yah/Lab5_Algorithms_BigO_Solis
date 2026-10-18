"""
=============================================================================
LABORATORY 5: ALGORITHMS AND BIG-O NOTATION - APPENDIX: ADDITIONAL EXERCISES
Student: SOLIS, LEANDRO P.
Student ID: TUPM-26-3631
Favorite Artist: Eminem
=============================================================================
"""

import time
import random

# =============================================================================
# STUDENT-SPECIFIC INPUT RULES & VALUE DERIVATION
# =============================================================================
LAST_NAME = "SOLIS"
STUDENT_ID = "TUPM-26-3631"
FAVORITE_ARTIST = "Eminem"

SEED_DIGIT = int(STUDENT_ID[-1])  # 1
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())  # 2 + 6 + 3 + 6 + 3 + 1 = 21
NAME_LENGTH = len(LAST_NAME)  # len("SOLIS") = 5
ARTIST_LENGTH = len(FAVORITE_ARTIST)  # len("Eminem") = 6
ARTIST_SUM = sum(ord(c.upper()) - ord('A') + 1 for c in FAVORITE_ARTIST if c.isalpha())
# E(5) + M(13) + I(9) + N(14) + E(5) + M(13) = 59

print("=" * 75)
print("             IX. APPENDIX: ADDITIONAL EXERCISES - EXECUTION LOG           ")
print("=" * 75)
print("Student-Specific Input Values:")
print(f"  LAST_NAME:        {LAST_NAME}")
print(f"  STUDENT_ID:       {STUDENT_ID}")
print(f"  FAVORITE_ARTIST:  {FAVORITE_ARTIST}")
print(f"  SEED_DIGIT:       {SEED_DIGIT}")
print(f"  ID_SUM:           {ID_SUM}")
print(f"  NAME_LENGTH:      {NAME_LENGTH}")
print(f"  ARTIST_LENGTH:    {ARTIST_LENGTH}")
print(f"  ARTIST_SUM:       {ARTIST_SUM}")
print("=" * 75)
print()


# =============================================================================
# EXERCISE 1: EMERGENCY DISPATCH RECORD SEARCH
# =============================================================================
print("=" * 75)
print("1. EMERGENCY DISPATCH RECORD SEARCH")
print("=" * 75)

# Target Incident: Generated using ID_SUM and ARTIST_SUM
target_incident = ID_SUM + ARTIST_SUM  # 21 + 59 = 80

# Incident Records: 10 sorted unique records generated using student inputs
original_records = [target_incident - (9 - i) * NAME_LENGTH for i in range(10)]

# Rotation: Determine rotation point using SEED_DIGIT
rotation_point = SEED_DIGIT  # 1
rotated_records = original_records[rotation_point:] + original_records[:rotation_point]

def search_rotated_records(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        
        # Check if left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else: # Right half is sorted
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
                
    return -1, comparisons

def linear_search_records(arr, target):
    comparisons = 0
    for idx, val in enumerate(arr):
        comparisons += 1
        if val == target:
            return idx, comparisons
    return -1, comparisons

pos_rotated, comps_rotated = search_rotated_records(rotated_records, target_incident)
pos_linear, comps_linear = linear_search_records(rotated_records, target_incident)

print("Assessment Data:")
print(f"Original Dataset:               {original_records}")
print(f"Rotated dataset:                {rotated_records} (Rotated by {rotation_point})")
print(f"Target incident:                {target_incident}")
print(f"Comparison Counts (Rotated BS): {comps_rotated}")
print(f"Linear Search comparison count: {comps_linear}")
print(f"Time and space complexity:      Rotated Binary Search -> Time: O(log n), Space: O(1)")
print(f"                                Linear Search         -> Time: O(n), Space: O(1)")
print(f"Final Output:                   Target incident {target_incident} found at position/index {pos_rotated} in rotated dataset.")
print(f"                                Rotated Binary Search completed in {comps_rotated} comparisons vs {comps_linear} comparisons for Linear Search (reduction of {comps_linear - comps_rotated} comparisons).")
print()


# =============================================================================
# EXERCISE 2: UNIVERSITY ENROLLMENT RECORDS
# =============================================================================
print("=" * 75)
print("2. UNIVERSITY ENROLLMENT RECORDS")
print("=" * 75)

# Dataset A: Ascending values using SEED_DIGIT and ID_SUM
dept_a = [ID_SUM + i * (SEED_DIGIT + 3) for i in range(6)]

# Dataset B: Ascending values using ARTIST_LENGTH and NAME_LENGTH
dept_b = [(ARTIST_LENGTH * 3) + i * NAME_LENGTH for i in range(6)]

def merge_sorted_records(a, b):
    consolidated = []
    i = 0
    j = 0
    comparisons = 0
    
    while i < len(a) and j < len(b):
        comparisons += 1
        if a[i] <= b[j]:
            consolidated.append(a[i])
            i += 1
        else:
            consolidated.append(b[j])
            j += 1
            
    while i < len(a):
        consolidated.append(a[i])
        i += 1
        
    while j < len(b):
        consolidated.append(b[j])
        j += 1
        
    return consolidated, comparisons

consolidated, merge_comps = merge_sorted_records(dept_a, dept_b)
is_ordered = all(consolidated[k] <= consolidated[k+1] for k in range(len(consolidated)-1))
count_before = len(dept_a) + len(dept_b)
count_after = len(consolidated)

print("Assessment Data:")
print(f"Department A dataset:                      {dept_a}")
print(f"Department B dataset:                      {dept_b}")
print(f"Consolidated dataset:                      {consolidated}")
print(f"Number of records before and after:        Before: {count_before} (Dept A: {len(dept_a)}, Dept B: {len(dept_b)}) | After: {count_after}")
print(f"Comparison count:                          {merge_comps}")
print(f"Ordering verification:                     {'Verified Correct (Monotonically Non-Decreasing)' if is_ordered and count_before == count_after else 'Failed'}")
print(f"Time and space complexity:                 Time Complexity: O(n + m), Space Complexity: O(n + m)")
print(f"Final Output:                              Successfully consolidated {count_after} student records from both departments into one sorted list with {merge_comps} comparisons.")
print()


# =============================================================================
# EXERCISE 3: E-COMMERCE ORDER PROCESSING
# =============================================================================
print("=" * 75)
print("3. E-COMMERCE ORDER PROCESSING")
print("=" * 75)

# Orders: Generate values using student-specific inputs
base_orders = [((ID_SUM * (i + 1) + SEED_DIGIT * 7 + NAME_LENGTH * 3) % 90) + 10 for i in range(10)]

def bubble_sort(arr):
    a = arr.copy()
    comps = 0
    moves = 0
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            comps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                moves += 1
                swapped = True
        if not swapped:
            break
    return a, comps, moves

def selection_sort(arr):
    a = arr.copy()
    comps = 0
    moves = 0
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comps += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            moves += 1
    return a, comps, moves

def insertion_sort(arr):
    a = arr.copy()
    comps = 0
    moves = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if a[j] > key:
                a[j + 1] = a[j]
                moves += 1
                j -= 1
            else:
                break
        a[j + 1] = key
        moves += 1  # placement of key
    return a, comps, moves

def time_sort(func, data, trials=1000):
    start = time.perf_counter()
    for _ in range(trials):
        res = func(data)
    elapsed = (time.perf_counter() - start) / trials
    return res[0], res[1], res[2], elapsed

random.seed(SEED_DIGIT)
random_orders = base_orders.copy()
random.shuffle(random_orders)

sorted_orders = sorted(base_orders)
reverse_orders = sorted(base_orders, reverse=True)

conditions = {
    "Sorted": sorted_orders,
    "Reverse-ordered": reverse_orders,
    "Random (Unsorted)": random_orders
}

print("Assessment Data:")
print(f"Generated order dataset:        {base_orders}")
print(f"Sorted input:                   {sorted_orders}")
print(f"Reverse input:                  {reverse_orders}")
print(f"Random input:                   {random_orders}")
print()

for cond_name, dataset in conditions.items():
    print(f"Condition: {cond_name}")
    print(f"  {'Algorithm':<16} {'Sorted?':<8} {'Comparisons':<14} {'Movements':<12} {'Execution Time (s)':<18}")
    for algo_name, algo_func in [("Bubble Sort", bubble_sort), ("Selection Sort", selection_sort), ("Insertion Sort", insertion_sort)]:
        res_arr, comps, moves, t_sec = time_sort(algo_func, dataset)
        is_sorted = (res_arr == sorted(dataset))
        print(f"  {algo_name:<16} {str(is_sorted):<8} {comps:<14} {moves:<12} {t_sec:<18.8f}")
    print()

print("Big O Analysis:")
print("  Bubble Sort:    Best: O(n) comps, O(1) moves    | Avg: O(n^2) comps, O(n^2) moves | Worst: O(n^2) comps, O(n^2) moves")
print("  Selection Sort: Best: O(n^2) comps, O(1) moves  | Avg: O(n^2) comps, O(n) moves   | Worst: O(n^2) comps, O(n) moves")
print("  Insertion Sort: Best: O(n) comps, O(n) moves    | Avg: O(n^2) comps, O(n^2) moves | Worst: O(n^2) comps, O(n^2) moves")
print()
print("Best-, average-, and worst-case observations:")
print("  1. Sorted Condition (Best Case):")
print("     - Bubble Sort terminates after a single pass (9 comparisons, 0 swaps) due to early-exit flag.")
print("     - Insertion Sort completes in linear time (9 comparisons, 9 placements).")
print("     - Selection Sort still performs all 45 comparisons as it unconditionally scans the unsorted partition.")
print("  2. Reverse Condition (Worst Case):")
print("     - Bubble Sort suffers maximum swaps and comparisons (45 comps, 45 swaps).")
print("     - Insertion Sort incurs maximum shifts (45 comps, 54 movements).")
print("     - Selection Sort maintains constant 45 comparisons and only 5 swaps.")
print("  3. Random Condition (Average Case):")
print("     - Demonstrates expected intermediate quadratic performance across all three algorithms.")
print("     - Insertion Sort achieves lowest overall comparisons and fastest execution time among the three.")
print()
print("Final Output:                   Successfully validated and benchmarked Bubble Sort, Selection Sort, and Insertion Sort across Sorted, Reverse-ordered, and Random order conditions.")
print("=" * 75)

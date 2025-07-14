import math
from copy import copy


def heaviest_path(lst):
    if not lst:
        return None
    print("0")
    return max(_heaviest_path(lst, i = 0, step =1, sum =lst[0], visited = [False] * len(lst)))

def _heaviest_path(lst,i,step,sum, visited):
    if i == len(lst) -1:
        print(f"\tsum = {sum}")
        return sum

    print (f" -- {sum}")
    jump = step + lst[i]

    # mark as visited
    visited[i] = True

    # jump right
    if i + jump < len(lst) and not visited[i + jump]:
        _heaviest_path(lst, i+jump, step+1,sum + lst[i+jump],copy(visited))

    # jump right
    if i - jump >= 0 and not visited[i - jump]:
        _heaviest_path(lst, i - jump, step + 1, sum + lst[i-jump],copy(visited))

    return math.inf


# --- דוגמאות לשימוש ---
print("--- דוגמה 1 ---")
heaviest_path([1, 2, 3, 4, 5]) # צפוי: מסלול [0, 2, 4], סכום 9

print("\n--- דוגמה 2 ---")
heaviest_path([1, 5, 2, 4, 3, 6, 0]) # צפוי: מסלול [0, 2, 6], סכום 3

print("\n--- דוגמה 3: אין מסלול ---")
heaviest_path([10, 1, 1, 1, 1]) # צפוי: לא נמצאו מסלולים

print("\n--- דוגמה 4: מסלול מורכב יותר עם קפיצה שמאלה פוטנציאלית ---")
heaviest_path([1, 0, 1, 0, 1, 0, 1]) # (0,1) -> jump = 1+0 = 1. To 1. Now at 1, step 2, sum 1
# arr[1] = 0. jump = 2+0 = 2. From 1 to 1+2=3 or 1-2=-1 (invalid)
# arr[3] = 0. jump = 3+0 = 3. From 3 to 3+3=6 or 3-3=0.
# From 3 to 6: 0 -> 1 -> 3 -> 6. sum = 1+0+0+1 = 2.
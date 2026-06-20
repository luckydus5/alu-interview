# Rain

Given a list of non-negative integers representing the heights of walls with
unit width 1 (the cross-section of a relief map), calculate how many square
units of water will be retained after it rains.

## Task

### 0. Rain

**File:** `0-rain.py`

```
def rain(walls)
```

- `walls` is a list of non-negative integers.
- Returns an integer: the total amount of rainwater retained.
- The ends of the list (before index `0` and after the last index) are not
  walls, so they retain no water.
- If the list is empty, returns `0`.

## How it works

Water above any position is bounded by the tallest wall to its left and the
tallest wall to its right. The trapped water at a position equals
`min(left_max, right_max) - height`, summed over all positions.

This solution precomputes, for every index, the maximum wall height to its
left and to its right, then sums the trapped water in a single pass — giving
an O(n) time, O(n) space algorithm.

## Usage

```
$ cat 0_main.py
#!/usr/bin/python3
"""
0_main
"""
rain = __import__('0-rain').rain

if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))

$ ./0_main.py
6
6
```

## Requirements

- Ubuntu 14.04 LTS, `python3` (3.4.3)
- PEP 8 style (1.7.x)
- No imported modules
- All files executable, starting with `#!/usr/bin/python3`
- All modules and functions documented

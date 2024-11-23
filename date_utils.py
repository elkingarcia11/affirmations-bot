from datetime import datetime

def get_time_ranges(now):
    """Define specific sub-ranges within the main range."""
    range1_start = now.replace(hour=12, minute=0, second=0, microsecond=0)
    range1_end = now.replace(hour=17, minute=59, second=59, microsecond=0)

    range2_start = now.replace(hour=18, minute=0, second=0, microsecond=0)
    range2_end = now.replace(hour=23, minute=59, second=59, microsecond=0)

    range3_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    range3_end = now.replace(hour=4, minute=59, second=59, microsecond=0)

    return [
        (range1_start, range1_end, "morning"),
        (range2_start, range2_end, "evening"),
        (range3_start, range3_end, "night"),
    ]

def get_active_range_index(now, sub_ranges):
    """Check which sub-range the current time falls into."""
    for i, (start, end, label) in enumerate(sub_ranges):
        if start <= now <= end:
            return i + 1, label  # Return sub-range index and label
    return None, None  # If no sub-range matches

# Example Usage
"""
now = datetime.now()  # Replace with any datetime object
sub_ranges = get_time_ranges(now)
index, label = get_active_range_index(now, sub_ranges)

if index:
    print(f"Current time falls into range {index}: {label}.")
else:
    print("Current time does not fall into any defined range.")
"""
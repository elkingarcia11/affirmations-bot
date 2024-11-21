def define_sub_ranges(now):
    """Define specific sub-ranges within the main range."""
    range1_start = now.replace(hour=12, minute=0, second=0, microsecond=0)
    range1_end = now.replace(hour=17, minute=59, second=59, microsecond=0)

    range2_start = now.replace(hour=18, minute=0, second=0, microsecond=0)
    range2_end = now.replace(hour=23, minute=59, second=59, microsecond=0)

    range3_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    range3_end = now.replace(hour=4, minute=59, second=59, microsecond=0)

    return [(range1_start, range1_end), (range2_start, range2_end), (range3_start, range3_end)]

def check_sub_ranges(now, sub_ranges):
    """Check which sub-range the current time falls into."""
    for i, (start, end) in enumerate(sub_ranges):
        if start <= now <= end:
            return i + 1  # Return sub-range index (1, 2, or 3)
    return None  # If no sub-range matches
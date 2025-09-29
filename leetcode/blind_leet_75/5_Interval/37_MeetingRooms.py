def can_attend_meetings(intervals):
    """
    Checks if a person can attend all meetings without any overlaps.

    Args:
        intervals: A list of meeting time intervals, where each interval is
                   a list/tuple of two integers [start, end].

    Returns:
        True if all meetings can be attended, False otherwise.
    """
    # Sort the meetings based on their start times.
    # The lambda function provides a key for sorting by the first element (start time) of each interval.
    intervals.sort(key=lambda x: x[0])

    # Iterate through the sorted list from the second meeting.
    # We only need to check for overlaps between consecutive meetings.
    for i in range(1, len(intervals)):
        current_meeting = intervals[i]
        previous_meeting = intervals[i-1]

        # Check for overlap: If the current meeting's start time is less than
        # the previous meeting's end time, there's an overlap.
        if current_meeting[0] < previous_meeting[1]:
            return False

    # If the loop completes without finding any overlaps, all meetings can be attended.
    return True

"""
o(N log N

Given an array of meeting time intervals consisting of start and end times
[[s1,e1], [s2,e2],...] (si < ei), determin if a person could attend all meetings

Input: intervals = [(0,30), (5,10), (15,20)]
output: false
Explanation: (0,30), (5,10) and (0,30), (15,20) will conflict
"""
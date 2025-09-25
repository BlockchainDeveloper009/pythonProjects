# project/util/time_helper.py

import datetime
import time
class TimeHelper:
    """A helper class for time-related functions."""
    def __init__(self):
        """
        Initializes the graph with a list of edges.
        """
        self.start_time = time.time()

    @staticmethod
    def get_current_time_str():
        """Returns the current time as a formatted string."""
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_timestamp():
        """Returns the current Unix timestamp."""
        return datetime.datetime.now().timestamp()



    def print_time_taken(self, problem_name, start_time,):
        # Measure the time for the BFS approach
        print(f"Measuring performance of {problem_name} approach...")

        end_time = time.time()
        duration = end_time - start_time
        print(f"{problem_name} duration: {duration:.6f} seconds")
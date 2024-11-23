#Print order queue

class Queue:
    def __init__(self):
        # Initializes an empty list to act as the queue.
        self.items = []

    def is_empty(self):
        # Checks if the queue is empty.
        return len(self.items) == 0

    def enqueue(self, item):
        # Adds an item to the end of the queue.
        self.items.append(item)

    def dequeue(self):
        # Removes and returns the item from the front of the queue, or None if empty.
        return self.items.pop(0) if not self.is_empty() else None


def simulate_print_queue(jobs):

    # Creates a queue for the print jobs.
    print_queue = Queue()

    # Enqueues each job into the queue.
    for job in jobs:
        print_queue.enqueue(job)

    # Processes each job in the queue.
    while not print_queue.is_empty():
        # Dequeues and prints the current job.
        current_job = print_queue.dequeue()
        print(f"Processing job: {current_job}")


def main():
    # Tests cases with a list of print jobs.
    print_jobs = ["Job 1: Print Invoice", "Job 2: Print Report", "Job 3: Print Presentation", "Job 4: Print Letter", "Job 5: Print Poster" ]

    # Simulates the print queue.
    simulate_print_queue(print_jobs)


# Executes the program.
main()

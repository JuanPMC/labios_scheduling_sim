class thuput_Scheduler():
    def complexity(self, n):
        return n
    def constant_penalties(self):
        return 0

    def schedule(self,tasks,workers):
        scores = []
        task_sizes = [task.task_size for task in tasks]
        mean_task_size = float(sum(task_sizes)) / float(len(task_sizes))

        for id, worker in enumerate(workers):
            for i in range(len(tasks)):
                if mean_task_size != 0:
                    scores.append([id, (i) * (mean_task_size/worker.w_speed)])
                else:
                    mean_task_size = 1
        scores.sort(key=lambda x: x[1], reverse=False)


        # Initialize an empty matrix to store the scheduled tasks
        result_matrix = [[] for _ in range(len(workers))]

        # Initialize a list of tuples to keep track of the number of tasks scheduled on each worker
        task_counts = [[id, 0] for id in range(len(workers))]  # Each tuple represents (worker_id, task_count)

        # Schedule using FIFO
        for id,task in enumerate(tasks):
            result_matrix[scores[id][0]].append(task)

        return result_matrix

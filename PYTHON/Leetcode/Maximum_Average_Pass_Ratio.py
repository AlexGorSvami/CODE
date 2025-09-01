def maxAverageRatio(classes: list, extraStudents: int) -> float:
        n = len(classes)
        heap = []
        for cl in classes:

            curr_pass_ratio = cl[0] / cl[1]
            changed_pass_ratio = (cl[0] + 1) / (cl[1] + 1)

            diff = changed_pass_ratio - curr_pass_ratio
            heappush(heap, (-diff, cl[0], cl[1]))


        for i in range(extraStudents):
            _, pass_value, total_value = heappop(heap)

            pass_value += 1
            total_value += 1

            curr_pass_ratio = pass_value / total_value
            expected_pass_ratio = pass_ratio = (pass_value + 1) / (total_value + 1)

            diff = expected_pass_ratio - curr_pass_ratio
            heappush(heap, (-diff, pass_value, total_value))


        max_average_ratio = sum(p / t for _, p, t in heap) / n
        return max_average_ratio

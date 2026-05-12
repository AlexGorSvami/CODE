class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        init_energy, curr_energy = 0, 0 

        for actual, minimum in tasks:
            if curr_energy < minimum:
                init_energy += (minimum - curr_energy)
                curr_energy = minimum 

            curr_energy -= actual 

        return init_energy 

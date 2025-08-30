# first attempt

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        freq = {}

        for j in cpdomains:

            cur_freq = j.split()
            second = cur_freq[1].split('.')

            if len(second) == 2:
                domains = [second[1], str(second[0] + "." + second[1])]
            elif len(second) == 3:
                domains = [second[2], str(second[1] + "." + second[2]), str(second[0] + "." + second[1] + "." + second[2])]

            for i in domains:
                if i in freq:
                    freq[i] += int(cur_freq[0])
                else:
                    freq[i] = int(cur_freq[0])

            
        new_list = []
        for k, v in freq.items():
            new_list.append(str(v) + " " + k)

        return new_list

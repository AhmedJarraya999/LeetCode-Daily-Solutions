class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt=Counter(students)
        for snd in sandwiches:
            if cnt[snd]==0:
                return cnt[0]+cnt[1]
            else:
                cnt[snd]-=1
        return 0

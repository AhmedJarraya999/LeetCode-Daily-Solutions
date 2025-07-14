class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players=sorted(players)
        trainers=sorted(trainers)
        matches=0
        i=0
        j=0
        for p in players:
            while j<len(trainers) and trainers[j]<p:
                    j+=1
            if j<len(trainers):
                    j+=1
                    matches+=1
        return matches

        
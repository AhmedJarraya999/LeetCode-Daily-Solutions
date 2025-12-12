from collections import defaultdict

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # Sort events: OFFLINE before MESSAGE if same timestamp
        events.sort(key=lambda x: (int(x[1]), x[0] != "OFFLINE"))

        mentions = [0] * numberOfUsers
        offline = defaultdict(int)   # offline[u] = time when user becomes online again

        for event, time, user in events:
            time = int(time)

            # Auto-restore users before processing this event
            for u in range(numberOfUsers):
                if offline[u] <= time:
                    offline[u] = 0   # means online

            if event == "OFFLINE":
                uid = int(user)
                offline[uid] = time + 60   # user stays offline for 60 time units

            else:  # MESSAGE
                if user == "ALL":
                    # Mention all users (even offline)
                    for u in range(numberOfUsers):
                        mentions[u] += 1

                elif user == "HERE":
                    # Mention only online users
                    for u in range(numberOfUsers):
                        if offline[u] <= time:
                            mentions[u] += 1

                else:
                    # Mention specific ids: id0 id2 id2 ...
                    curr = user.split()
                    for tkn in curr:
                        if tkn.startswith("id"):
                            uid = int(tkn[2:])
                            mentions[uid] += 1

        return mentions

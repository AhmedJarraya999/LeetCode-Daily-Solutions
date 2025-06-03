class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_positions = {}
        litter_count = 0
        start = None

        for i in range(m):
            for j in range(n):
                cell = classroom[i][j]
                if cell == 'S':
                    start = (i, j)
                elif cell == 'L':
                    litter_positions[(i, j)] = litter_count
                    litter_count += 1

        all_collected = (1 << litter_count) - 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque()
        queue.append((*start, energy, 0, 0))  # x, y, energy_left, collected_mask, steps

        visited = dict()  # key: (x, y, collected_mask), value: max energy at that state

        while queue:
            x, y, e, mask, steps = queue.popleft()

            if mask == all_collected:
                return steps

            key = (x, y, mask)
            if key in visited and visited[key] >= e:
                continue
            visited[key] = e

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if classroom[nx][ny] == 'X':
                    continue
                if e == 0 and classroom[x][y] != 'R':
                    continue

                new_e = energy if classroom[nx][ny] == 'R' else e - 1

                new_mask = mask
                if (nx, ny) in litter_positions:
                    bit = litter_positions[(nx, ny)]
                    new_mask |= (1 << bit)

                queue.append((nx, ny, new_e, new_mask, steps + 1))

        return -1

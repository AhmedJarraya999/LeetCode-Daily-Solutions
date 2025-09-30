import heapq

class MovieRentingSystem:

    def __init__(self, n: int, entries: list[list[int]]):
        # price[(shop, movie)] = price
        self.price = {(shop, movie): p for shop, movie, p in entries}

        # available[movie] = min-heap of (price, shop, movie)
        self.available = {}
        for shop, movie, p in entries:
            if movie not in self.available:
                self.available[movie] = []
            heapq.heappush(self.available[movie], (p, shop, movie))

        # rented = global min-heap of (price, shop, movie)
        self.rented = []
        self.rented_set = set()   # track active rentals

    def search(self, movie: int) -> list[int]:
        if movie not in self.available:
            return []

        res, temp = [], []
        while self.available[movie] and len(res) < 5:
            price, shop, m = heapq.heappop(self.available[movie])
            if (shop, m) not in self.rented_set:  # valid unrented copy
                res.append(shop)
            temp.append((price, shop, m))

        # push back all popped
        for item in temp:
            heapq.heappush(self.available[movie], item)

        return res

    def rent(self, shop: int, movie: int) -> None:
        self.rented_set.add((shop, movie))
        p = self.price[(shop, movie)]
        heapq.heappush(self.rented, (p, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented_set.remove((shop, movie))
        # lazy deletion: leave in heap, skip later

    def report(self) -> list[list[int]]:
        res, temp = [], []
        while self.rented and len(res) < 5:
            p, shop, movie = heapq.heappop(self.rented)
            if (shop, movie) in self.rented_set:  # still valid
                res.append([shop, movie])
                temp.append((p, shop, movie))

        for item in temp:
            heapq.heappush(self.rented, item)

        return res

import heapq
from collections.abc import Callable
from itertools import count
from puzzle.base_search import BaseSearch
from puzzle.state import GOAL_STATE, State
from puzzle.result import SearchResult


GOAL_POSITIONS = {tile: divmod(index, 3) for index, tile in enumerate(GOAL_STATE)}


class AStar(BaseSearch):
    def __init__(self, heuristic: Callable[[State], int] | None = None):
        self.custom_heuristic = heuristic

    def heuristic(self, state: State) -> int:
        if self.custom_heuristic is not None:
            return self.custom_heuristic(state)

        distance = 0
        for index, tile in enumerate(state.tiles):
            if tile != 0:
                row, column = divmod(index, 3)
                goal_row, goal_column = GOAL_POSITIONS[tile]
                distance += abs(row - goal_row) + abs(column - goal_column)

        return distance

    def search(self, initial: State) -> SearchResult:
        order = count()
        frontier = [(initial.cost + self.heuristic(initial), next(order), initial)]
        best_cost = {initial.tiles: initial.cost}
        result = SearchResult(solution=None, nodes_generated=1, max_frontier_size=1)

        while frontier:
            _, _, state = heapq.heappop(frontier)
            if state.cost != best_cost[state.tiles]:
                continue
            if state.is_goal:
                result.solution = state
                result.depth = state.cost - initial.cost
                break

            result.nodes_expanded += 1
            for child in state.neighbors():
                if child.cost < best_cost.get(child.tiles, float("inf")):
                    best_cost[child.tiles] = child.cost
                    priority = child.cost + self.heuristic(child)
                    heapq.heappush(frontier, (priority, next(order), child))
                    result.nodes_generated += 1

            result.max_frontier_size = max(result.max_frontier_size, len(frontier))

        return result

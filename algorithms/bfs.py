from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class BFS(BaseSearch):

    def search(self, initial: State) -> SearchResult:
        frontier = deque([initial])
        seen = {initial.tiles}
        result = SearchResult(solution=None, nodes_generated=1, max_frontier_size=1)

        while frontier:
            state = frontier.popleft()
            if state.is_goal:
                result.solution = state
                result.depth = state.cost - initial.cost
                break

            result.nodes_expanded += 1
            for child in state.neighbors():
                if child.tiles not in seen:
                    seen.add(child.tiles)
                    frontier.append(child)
                    result.nodes_generated += 1

            result.max_frontier_size = max(result.max_frontier_size, len(frontier))

        return result

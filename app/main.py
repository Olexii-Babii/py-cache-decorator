from typing import Any, Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def wrapper(*args) -> Any:
        if memory.get(args, False) or memory.get(args) == 0:
            print("Getting from cache")
            return memory.get(args)
        else:
            result = func(*args)
            memory[args] = result
            print("Calculating new result")
            return result

    return wrapper

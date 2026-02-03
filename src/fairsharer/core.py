from __future__ import annotations

from typing import List, Sequence


def fair_sharer(values: Sequence[float], num_iterations: int, share: float = 0.1) -> List[float]:
   
    if num_iterations < 0:
        raise ValueError("num_iterations must be >= 0")
    if not (0 <= share <= 0.5):
        raise ValueError("share must be between 0 and 0.5")
    if len(values) == 0:
        return []

    current = [float(v) for v in values]
    n = len(current)

    for _ in range(num_iterations):
        max_value = max(current)
        max_idx = current.index(max_value)

        left_idx = (max_idx - 1) % n
        right_idx = (max_idx + 1) % n

        give_amount = current[max_idx] * share

        new_vals = current.copy()
        new_vals[max_idx] -= 2 * give_amount
        new_vals[left_idx] += give_amount
        new_vals[right_idx] += give_amount

        current = new_vals

    return current

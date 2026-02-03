from fairsharer import fair_sharer


def test_fair_sharer():
    assert fair_sharer([0, 1000, 800, 0], 1) == [100.0, 800.0, 900.0, 0.0]
    assert fair_sharer([0, 1000, 800, 0], 2) == [100.0, 890.0, 720.0, 90.0]

def test_fair_sharer_zero_iterations_returns_original():
    assert fair_sharer([1, 2, 3], 0) == [1.0, 2.0, 3.0]

def test_fair_sharer_ring_neighbors():
    assert fair_sharer([10, 1, 1], 1, share=0.1) == [8.0, 2.0, 2.0]

def test_fair_sharer_empty_list():
    assert fair_sharer([], 5) == []

def test_fair_sharer_invalid_inputs():
    try:
        fair_sharer([1, 2, 3], -1)
        assert False, "Expected ValueError for negative num_iterations"
    except ValueError:
        pass

    try:
        fair_sharer([1, 2, 3], 1, share=0.9)
        assert False, "Expected ValueError for share > 0.5"
    except ValueError:
        pass

"""Cross-member unit tests for Duong Trung Anh (@philip_kkk)'s Week 1 code (W2-4).

Tests Philip's DFS algorithm translation and edge cases across their W1 modules.
"""

from members.philip_kkk.w1 import grades, rules, text_tools, timetable, translate

# ============================================================================
# W1-4: DFS Traversal Algorithm Tests
# ============================================================================


def test_dfs_linear_graph() -> None:
    """Test DFS on a simple linear path: 0 -> 1 -> 2."""
    adj = [[1], [2], []]
    assert translate.dfs(adj, 0) == [0, 1, 2]


def test_dfs_branching_tree() -> None:
    """Test DFS traversal on a branching tree."""
    adj = [[1, 2], [3], [], []]
    assert translate.dfs(adj, 0) == [0, 1, 3, 2]


def test_dfs_cycles_and_back_edges() -> None:
    """Edge case: Graph with cycles does not loop infinitely."""
    adj = [[1, 2], [2], [0]]
    assert translate.dfs(adj, 0) == [0, 1, 2]


def test_dfs_disconnected_component() -> None:
    """Edge case: Traversal from a start node stays within its reachable component."""
    # Component 1: 0 <-> 1; Component 2: 2 -> 3
    adj = [[1], [0], [3], []]
    assert translate.dfs(adj, 2) == [2, 3]


def test_dfs_single_node() -> None:
    """Edge case: Single-node graph with no edges."""
    adj = [[]]
    assert translate.dfs(adj, 0) == [0]


def test_dfs_star_graph() -> None:
    """Test DFS on a star graph where center connects to multiple leaves."""
    adj = [[1, 2, 3], [], [], []]
    assert translate.dfs(adj, 0) == [0, 1, 2, 3]


# ============================================================================
# Additional W1 Edge Case Tests for philip_kkk
# ============================================================================


def test_summary_identical_scores() -> None:
    """Edge case: Summary when all scores are identical."""
    assert grades.summary([5.0, 5.0, 5.0]) == {
        "min": 5.0,
        "max": 5.0,
        "mean": 5.0,
        "median": 5.0,
    }


def test_top_k_larger_than_unique_words() -> None:
    """Edge case: Requesting more top_k elements than available unique words."""
    assert text_tools.top_k("apple banana", 10) == [("apple", 1), ("banana", 1)]


def test_thesis_boundary_values() -> None:
    """Edge case: Exactly at the threshold vs 1 credit below."""
    assert rules.can_register_thesis(120, 2.0) is True
    assert rules.can_register_thesis(119, 2.0) is False
    assert rules.missing(119, 2.0) == ["need 1 more credits"]


def test_timetable_alphabetical_tie() -> None:
    """Edge case: Courses on the same day are strictly sorted alphabetically."""
    schedule = [("MATH101", "Mon"), ("BIO101", "Mon"), ("CHEM101", "Mon")]
    assert timetable.by_day(schedule) == {"Mon": ["BIO101", "CHEM101", "MATH101"]}

"""Edge cases and input immutability for Philip's W1 functions."""

from members.philip_kkk.w1 import grades, rules, text_tools, timetable, translate


def test_summary_does_not_modify_input() -> None:
    scores = [9.0, 6.0, 8.0]
    assert grades.summary(scores)["median"] == 8.0
    assert scores == [9.0, 6.0, 8.0]


def test_repeated_scores() -> None:
    assert grades.summary([4.5] * 3) == dict.fromkeys(
        ("min", "max", "mean", "median"), 4.5
    )


def test_punctuation_only_input() -> None:
    assert text_tools.word_count(".,!?;: \t\n") == {}


def test_top_k_negative_limit() -> None:
    assert text_tools.top_k("apple pear apple", -1) == []


def test_three_way_alphabetical_tie() -> None:
    assert text_tools.top_k("pear apple banana", 2) == [("apple", 1), ("banana", 1)]


def test_each_thesis_threshold_is_required() -> None:
    assert not rules.can_register_thesis(119, 2.0)
    assert not rules.can_register_thesis(120, 1.99)


def test_timetable_preserves_duplicates() -> None:
    assert timetable.by_day([("Z", "Mon"), ("A", "Mon"), ("A", "Mon")]) == {
        "Mon": ["A", "A", "Z"]
    }


def test_dfs_cycles_and_self_loops() -> None:
    graph = [[0, 2, 1], [2], [0, 3], [3]]
    assert translate.dfs(graph, 0) == [0, 2, 3, 1]
    assert graph == [[0, 2, 1], [2], [0, 3], [3]]


def test_dfs_stays_in_start_component() -> None:
    assert translate.dfs([[1], [0], [3], []], 2) == [2, 3]

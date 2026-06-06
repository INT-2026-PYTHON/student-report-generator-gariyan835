"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass
from .stats import (
    average_per_student,
    subjects_offered,
    top_scorer,
    passing_students,
)

def format_report(records):
    averages = average_per_student(records)
    topper, score = top_scorer(records)

    report = [
        f"Total records: {len(records)}",
        f"Subjects: {', '.join(sorted(subjects_offered(records)))}",
        "Average scores:"
    ]

    for name in sorted(averages):
        report.append(f"{name}: {averages[name]}")

    report.append(f"Top scorer: {topper} ({score})")
    report.append(
        f"Passing students: {', '.join(passing_students(records, 60.0))}"
    )

    return "\n".join(report)

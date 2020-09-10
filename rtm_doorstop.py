"""Create a traceability matrix between requirements and tests from Doorstop items."""
import doorstop
import rapidtables
import csv
import fire


def rtm_builder(
    prefix: str, root: str = None, sort_key: str = None, csv_path: str = None
) -> str:
    """Generate a traceability matrix, and output to either stdout or csv.

    Args:
        prefix: The prefix for Doorstop requirements.
        root: The root path to search for Doorstop documents.
        sort_key: If the RTM should be sorted, sort by this key.
            Should be one of 'UID', 'Has Test', 'Tests', or None. Defaults to None.
        csv_path: If the RTM should be written to file, write to this path.
            If omitted, the RTM will be returned. Defaults to None.
    """
    tree = doorstop.build(root=root)
    reqs_doc = tree.find_document(prefix)
    table_data = [
        {
            "UID": str(item),
            "Has Test": bool(item.child_links),
            "Need Test": bool(item.normative),
            "Tests": " ".join([str(child) for child in item.child_links]),
        }
        for item in reqs_doc.items
    ]

    if sort_key:
        table_data = sorted(table_data, key=lambda x: x[sort_key])

    table = rapidtables.make_table(table_data, tablefmt="md")

    if csv_path:
        with open(csv_path, "w", newline="") as csvfile:
            fieldnames = ["UID", "Has Test", "Need Test", "Tests"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in table_data:
                writer.writerow(row)
        return f"Successfully wrote traceability matrix to {csv_path}"
    else:
        return table


def main():
    """Entry point."""
    fire.Fire(rtm_builder)


if __name__ == "__main__":
    main()

"""Create a traceability matrix between requirements and tests from Doorstop items."""
import doorstop
import rapidtables
import csv
import fire


def rtm_builder(prefix, sort=True, csv_path=None):
    """Generate a traceability matrix, and output to either stdout or csv.

    Args:
        prefix: The prefix for Doorstop requirements.
        sort (bool, optional): Specifies if the RTM should be sorted. Defaults to True.
        csv_path ([type], optional): Path to write to file, if desired. Defaults to None.
    """
    tree = doorstop.build()
    reqs_doc = tree.find_document(prefix)
    table_data = [
        {
            "UID": str(item),
            "Has Test": bool(item.child_links),
            "Tests": " ".join([str(child) for child in item.child_links]),
        }
        for item in reqs_doc.items
    ]
    if sort:
        table_data = sorted(table_data, key=lambda x: x["UID"])
    table = rapidtables.make_table(table_data, tablefmt="md")
    if csv_path:
        with open(csv_path, "w", newline="") as csvfile:
            fieldnames = ["UID", "Has Test", "Tests"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in table_data:
                writer.writerow(row)
    else:
        print(table)


def main():
    """Entry point."""
    fire.Fire(rtm_builder)


if __name__ == "__main__":
    main()

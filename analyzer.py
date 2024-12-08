import os
import argparse
from collections import Counter
import csv


def get_default_log_file():
    """
    Returns the default log file path for Linux.
    """
    return "/var/log/syslog"


def read_logs(file_path):
    """
    Reads the log file and returns a list of lines.
    """
    if not os.path.exists(file_path):
        print(f"Log file not found: {file_path}")
        return []
    with open(file_path, 'r') as file:
        return file.readlines()


def parse_logs(log_lines, keyword=None):
    """
    Parses log lines and filters by keyword if provided.
    """
    filtered_logs = []
    for line in log_lines:
        if not keyword or keyword.lower() in line.lower():
            filtered_logs.append(line.strip())
    return filtered_logs


def count_occurrences(log_lines):
    """
    Counts the occurrences of each unique line in the logs.
    """
    return Counter(log_lines)


def display_results(counts):
    """
    Displays the counted results.
    """
    print(f"{'Log Entry':<60} | Count")
    print("-" * 80)
    for log, count in counts.most_common():
        print(f"{log[:60]:<60} | {count}")


def save_to_csv(counts, output_file):
    """
    Saves the results to a CSV file.
    """
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Log Entry", "Count"])
            for log, count in counts.items():
                writer.writerow([log, count])
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error saving results to CSV: {e}")


def main():
    """
    Main function for the command-line tool.
    """
    parser = argparse.ArgumentParser(description="Simplified Log Analyzer")
    parser.add_argument(
        "--logfile", type=str, help="Path to the log file (default: /var/log/syslog).", default=get_default_log_file()
    )
    parser.add_argument(
        "--filter", type=str, help="Keyword to filter logs.", required=False
    )
    parser.add_argument(
        "--output", type=str, help="File to save the results (CSV format).", required=False
    )
    args = parser.parse_args()

    #Read and filter logs
    log_lines = read_logs(args.logfile)
    if not log_lines:
        print("No logs to process.")
        return

    filtered_logs = parse_logs(log_lines, args.filter)

    #Count occurrences
    counts = count_occurrences(filtered_logs)

    #Display results
    display_results(counts)

    #Save results to CSV
    if args.output:
        save_to_csv(counts, args.output)


if __name__ == "__main__":
    main()

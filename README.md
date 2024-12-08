# LogAnalyzer

A command-line tool for analyzing Linux log files. This script reads and processes logs from a specified file, counts occurrences of unique log entries, and provides options to filter results or export them to a CSV file for further analysis in tools like LibreOffice or Excel.

## Features

- Analyze any text-based log file (default: `/var/log/syslog`).
- Filter log entries by keywords.
- Count occurrences of unique log lines.
- Export results to a CSV file for easy filtering and sorting.
- Designed to work natively with Linux tools.

## Requirements

- Python 3.6 or newer
- Runs natively on Linux

## Usage

### **1. Analyze Logs**
By default, the script analyzes `/var/log/syslog` and outputs a summary of log entries with their occurrence counts:
```bash
python analyzer.py
```

### **2. Analyze a Custom Log File**
Specify a custom log file with the `--logfile` option:
```bash
python analyzer.py --logfile /path/to/your/logfile
```

### **3. Filter Logs by Keyword**
Filter logs that contain a specific keyword using the `--filter` option:
```bash
python analyzer.py --filter "error"
```

### **4. Export Results to a CSV File**
Save the analysis results to a CSV file using the `--output` option:
```bash
python analyzer.py --output results.csv
```

### **5. Combine Filtering and CSV Export**
You can combine options to filter logs and save the results to a CSV file:
```bash
python analyzer.py --logfile /var/log/syslog --filter "gnome" --output filtered_logs.csv
```

## Examples

### Example 1: Default Analysis
```bash
python analyzer.py
```
**Output:**
```
Log Entry                                                   | Count
--------------------------------------------------------------------------------
Dec  7 12:34:56 myhost systemd[1]: Starting GNOME Display    | 5
Dec  7 12:34:57 myhost gnome-keyring-daemon[PID]: Initialized | 3
...
```

### Example 2: Filtered and Saved Results
```bash
python analyzer.py --filter "error" --output errors.csv
```
This filters all log entries containing the word "error" and saves them to `errors.csv`.

**CSV Output:**
| Log Entry                                                | Count |
|----------------------------------------------------------|-------|
| Dec  7 12:34:56 myhost systemd[1]: Error initializing GNOME | 3     |
| Dec  7 12:35:22 myhost kernel: Error in module driver      | 2     |
| ...                                                      | ...   |

## Output Files

### **CSV Format**
The saved CSV file contains two columns:
1. `Log Entry`: The unique log line.
2. `Count`: The number of times the log entry appears in the file.

You can open the CSV file in LibreOffice, Excel, or any text editor.

## Limitations

- Designed specifically for text-based log files (e.g., `/var/log/syslog`).
- Only works natively on Linux systems.
- For very large logs, performance may vary depending on system resources.

## Contributing

Feel free to fork this repository and contribute by submitting pull requests. All contributions are welcome!




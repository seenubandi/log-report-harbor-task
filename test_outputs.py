import json
import os
from collections import Counter

OUTPUT_FILE = "report.json"
LOG_FILE = "access.log"

def parse_log():
    counts = Counter()
    total = 0
    with open(LOG_FILE, "r") as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
            ip = parts[0]
            counts[ip] += 1
            total += 1
    return counts, total

def load_output():
    assert os.path.exists(OUTPUT_FILE), "report.json not found"
    with open(OUTPUT_FILE) as f:
        return json.load(f)

def test_total_requests():
    _, expected_total = parse_log()
    data = load_output()
    assert data["total_requests"] == expected_total

def test_ip_counts():
    expected_counts, _ = parse_log()
    data = load_output()
    assert data["requests_per_ip"] == dict(expected_counts)

def test_format():
    data = load_output()
    assert "total_requests" in data
    assert "requests_per_ip" in data
    assert isinstance(data["requests_per_ip"], dict)

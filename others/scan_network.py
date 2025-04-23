#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: scan_network.py
"""Scan network for reachable IPs and measure latency"""

__author__ = "Jugal Kishore <me@devjugal.com>"

# Import Libraries
import ipaddress
import subprocess
import concurrent.futures
import csv
import requests


def fetch_prefixes_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # raise exception if request failed
    data = response.json()
    # Extract IPv4 prefixes from JSON response
    prefixes = data.get("v4", {}).get("prefixes", [])
    return prefixes


def expand_ips(prefixes):
    ips = []
    for prefix in prefixes:
        try:
            network = ipaddress.ip_network(prefix, strict=False)
            ips.extend(str(ip) for ip in network.hosts())
        except ValueError:
            continue  # skip invalid prefixes
    return ips


def ping_ip(ip):
    try:
        # '-c 1' = send 1 ping packet, '-W 1' = wait max 1 second for reply (Linux/macOS)
        output = subprocess.check_output(
            ["ping", "-c", "1", "-W", "1", ip],
            stderr=subprocess.STDOUT,
            universal_newlines=True,
        )
        for line in output.splitlines():
            if "time=" in line:
                time_str = line.split("time=")[1].split()[0]
                latency = float(time_str)
                return ip, latency
        return ip, float("inf")
    except subprocess.CalledProcessError:
        return ip, float("inf")


if __name__ == "__main__":
    url = "https://api.devjugal.com/as/prefixes?as_number=AS9830"
    prefixes = fetch_prefixes_from_url(url)
    print(f"Fetched {len(prefixes)} prefixes from API.")

    ips = expand_ips(prefixes)
    print(f"Expanded to {len(ips)} individual IPs.")

    results = []
    max_workers = min(1000, len(ips))

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_ip = {executor.submit(ping_ip, ip): ip for ip in ips}
        for future in concurrent.futures.as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                ip, latency = future.result()
            except Exception:
                latency = float("inf")
            results.append((ip, latency))

    results.sort(key=lambda x: x[1])

    with open("output.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["IP Address", "Latency (ms)"])
        for ip, latency in results:
            status = f"{latency:.2f}" if latency != float("inf") else "unreachable"
            csv_writer.writerow([ip, status])

    print("Results saved to output.csv")

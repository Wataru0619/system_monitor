#!/bin/bash
# SPDX-FileCopyrightText: 2025 Wataru Suenaga
# SPDX-License-Identifier: GPL-3.0-only

ng () {
    echo "Test failed"
    res=1
}

res=0

# Test1: 出力メッセージが正しくパブリッシュされているか
output=$(ros2 topic echo /system_info --once 2>&1)
status=$?

echo "Test1 command status: $status"

if [[ "$output" =~ "CPU Usage" ]] && [[ "$output" =~ "Memory Usage" ]] && [[ "$output" =~ "Network Traffic" ]] && [ $status -eq 0 ]; then
    echo "Test1 Passed"
else
    ng
fi

# Test2
sleep 2
output=$(ros2 topic echo /system_info --once 2>&1)

echo "Test2 command status: $status"

if [[ "$output" =~ "CPU Usage" ]] && [[ "$output" =~ "Memory Usage" ]] && [[ "$output" =~ "Network Traffic" ]]; then
    echo "Test2 Passed"
else
    ng
fi


if [ $res -eq 0 ]; then
    echo "All tests passed"
else
    echo "Some tests failed"
fi

# This software package is licensed under the GPL-3.0 License, and redistribution and usage are permitted under its terms.
# © 2025:Wataru Suenaga

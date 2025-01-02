#!/bin/bash
# SPDX-FileCopyrightText: 2024 Wataru Suenaga
# SPDX-License-Identifier: GPL-3.0-only

ng () {
    echo "Test failed"
    res=1
}

res=0

# Test1: 出力メッセージが正しくパブリッシュされているか
# ROS2のトピックの出力を確認
output=$(ros2 topic echo /system_info --once 2>&1)
status=$?

# 出力内容を確認
if [[ "$output" =~ "CPU Frequency" ]] && [[ "$output" =~ "CPU Cores" ]] && [[ "$output" =~ "Memory Usage" ]] && [ $status -eq 0 ]; then
    echo "Test1 Passed"
else
    ng
fi

# Test2: トピックがパブリッシュされていることを確認
# 一定時間待機してから再確認
sleep 2
output=$(ros2 topic echo /system_info --once 2>&1)
if [[ "$output" =~ "CPU Frequency" ]] && [[ "$output" =~ "CPU Cores" ]] && [[ "$output" =~ "Memory Usage" ]]; then
    echo "Test2 Passed"
else
    ng
fi

# 結果の表示
if [ $res -eq 0 ]; then
    echo "All tests passed"
else
    echo "Some tests failed"
fi


# Recap of complexity reduction

[Functional aggregation](https://github.com/code-craft-a1/simple-monitor-in-py-suryanshv23/blob/3539061e51edaaedc546fb2aa0ae9e7bdf9da800/monitor.py) instead of a procedural for-loop.

[Return value enrichment](https://github.com/code-craft-a1/simple-monitor-in-cpp-Tanyagarg702/blob/0fff7f256ad82738e1019586ed7e2409e8b07cec/monitor.cpp) - the consumer's perspective.
A user will want to see which vital is off, when things are "not ok"

[Range classification](https://github.com/code-craft-a1/simple-monitor-in-cpp-Shivsharma779/blob/deea5f6ab0d85a7d49d67dfd9d2c8c0e385228aa/monitor.cpp) - helps the care-giver.
Action taken when temperature is low is very different from when it is high. Notice the split between `determineLowerRange` and `determineUpperRange`.

[Expressing exceptions](https://github.com/code-craft-a1/simple-monitor-in-py-priyanja/blob/ccc5a53bad2fcd132c383dbb8caf79ae80359314/monitor.py) like SPO2, which has no upper limit.

[Testing the parts, then testing the whole](https://github.com/code-craft-a1/simple-monitor-in-py-priyanja/blob/ccc5a53bad2fcd132c383dbb8caf79ae80359314/monitor.test.py)

## Open-close principle

The code is open for extension, but closed for modification. How far do we keep it open?

[Vitals declared as yml](https://github.com/clean-code-craft-p-1/simple-monitor-in-cpp-art-pogorelov/blob/c0d771ad5924b8427a50daf496745c0cbebcc232/monitor/resource/config.yml)

[Property based tests for range](https://github.com/clean-code-craft-p-1/simple-monitor-in-cpp-art-pogorelov/blob/c0d771ad5924b8427a50daf496745c0cbebcc232/monitor/test/src/RangeTest.cpp)

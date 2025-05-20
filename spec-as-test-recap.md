# Recap of statistics

The [following code](https://github.com/code-craft-a1/spring-in-cpp-Tanyagarg702/blob/1eb34d3c6be6ddad2bf82a9b8321851a57441d6f/stats.cpp) returns NaN when the input is empty.

```cpp
  if (values.empty()) {
    double nan = std::numeric_limits<double>::quiet_NaN();
    return Statistics::Stats(nan, nan, nan);
  }
```

It needs `#include <limits>` in Ubuntu. It may be indirectly included in other platforms. How do we make portable code? Do we need to build on all platforms?

Is there an easier way? Use `cpplint` (included in the next assignment)

---

What else can go wrong, and what should be the behavior? [Add them as tests](https://github.com/code-craft-a1/spring-in-py-priyanja/blob/1181092a7d97deeacdcf583ebbe706064cb67312/statistics.test.py)

---

Use of built-in functions [in C++](https://github.com/code-craft-a1/spring-in-cpp-bhumikaadobe/blob/90e5a350ad0836054f7c9f4e5bfaeef2ab71f299/stats.cpp#L13) and [in JavaScript](https://github.com/code-craft-a1/spring-in-js-bhatiaPankaj/blob/ea4ad16737b2be4af8101c1d01985282e4f40376/statistics.mjs#L5) for statistics.

---

Mistake-proofing [with spans and non-discardable return values](https://github.com/clean-code-craft-p-1/spring-in-cpp-art-pogorelov/blob/fc5a656ed2a90d4b160f491865e40222a817a7eb/stats.h#L15)

## Take-away

Use tests to express the specification.

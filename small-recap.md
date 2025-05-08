# Modularity and Naming recap

[Mistake-proofing](https://github.com/code-craft-a1/well-named-in-cpp-bhumikaadobe/blob/2c41cced4edcf665ef9e3d5b33ace4bab2cd09b2/ColorDefs.cpp) with `const`

Tests in a separate file, [with exception behavior](https://github.com/code-craft-a1/well-named-in-js-rekha-m/blob/9e79a6f1ea975dc93230238540d09b8721db594d/app/test/ColorPairTest.js)

[Isolation of code with stable lifecycle](https://github.com/code-craft-a1/well-named-in-cpp-Shivsharma779/blob/a352ffd32116cad6db2ad18a36018336843a6850/ColorPair.hpp)

Linking together [with a simple CMakeList](https://github.com/code-craft-a1/well-named-in-cpp-KaranSingh1301/blob/ca7062e28341f1edbd57a484f826385e9e4feb94/CMakeLists.txt)

Separating the color enum [Color Map](https://github.com/code-craft-a1/well-named-in-cpp-KaranSingh1301/blob/ca7062e28341f1edbd57a484f826385e9e4feb94/ColorMap.h) from the [pairing](https://github.com/code-craft-a1/well-named-in-cpp-KaranSingh1301/blob/ca7062e28341f1edbd57a484f826385e9e4feb94/ColorPair.cpp) and the [conversion](https://github.com/code-craft-a1/well-named-in-cpp-KaranSingh1301/blob/ca7062e28341f1edbd57a484f826385e9e4feb94/ColorUtils.cpp)

## Take-away

- Separate code with different life-cycles
- Separate new code from legacy
- Make your class hard to misuse: "Shift left" the detection of errors

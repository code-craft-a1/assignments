
Different sensor-data in different classes?

```cpp
class RainySensorStub : public IWeatherSensor {
    double TemperatureInC() const override { return 26; }
    int Precipitation() const override { return 70; }
    int Humidity() const override { return 72; }
    int WindSpeedKMPH() const override { return 52; }
};
```

```cpp
class SunnySensorStub : public IWeatherSensor {
    double TemperatureInC() const override { return 20; }
    int Precipitation() const override { return 10; }
    int Humidity() const override { return 30; }
    int WindSpeedKMPH() const override { return 10; }
};
```

... Or different instances of one class?

```cpp
class SensorStub : public IWeatherSensor {
        private:
            double temperature;
            int precipitation;
            int humidity;
            int windSpeed;

        public:
            // Constructor to allow configurable sensor values
            SensorStub(double temp, int precip, int hum, int wind)
                : temperature(temp), precipitation(precip), humidity(hum), windSpeed(wind) {}

            double TemperatureInC() const override {
                return temperature;
            }

            int Precipitation() const override {
                return precipitation;
            }

            int Humidity() const override {
                return humidity;
            }

            int WindSpeedKMPH() const override {
                return windSpeed;
            }
    };

SensorStub rainySensorStub(26, 70, 72, 52);
SensorStub sunnySensorStub(20, 10, 30, 10);
```

---

[Property based tests](https://github.com/clean-code-craft-p-1/test-failer-in-cpp-art-pogorelov/blob/master/lib/test/src/SensorStub.h) in C++

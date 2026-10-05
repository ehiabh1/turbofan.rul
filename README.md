# Turbofan Engine RUL Prediction

Predicting how many flights a jet engine has left before it fails, from
its sensor readings (NASA C-MAPSS dataset, FD001).

## Problem

Engines wear out. Service them too early and you throw away good parts;
too late and they fail in service, which is expensive and unsafe.
Remaining Useful Life (RUL) prediction aims at the middle: estimate how
many flights an engine has left, based on what its sensors say today.

## Data

NASA's C-MAPSS turbofan dataset, subset FD001.

- 100 engines run until they failed (used for training)
- 100 more switched off partway through (used for testing)
- 21 sensors recorded once per flight, plus 3 operating settings
- Engines lasted between 128 and 362 flights, median 199

The raw files aren't included in this repo. See `data/README.md` for the
download link.

## Approach

**Working out the answer for each row.** Training engines ran to
failure, so RUL is just how many flights remain until the end of that
engine's record. Test engines stop early, so NASA supplies the true RUL
at each one's last recorded flight, and the rest is counted back from
there.

**Dropping useless sensors.** Seven columns hold exactly the same value
in all 20,631 rows. A sensor that never changes can't tell a healthy
engine from a failing one, so they go. Sensor 6 only takes two values
and shows no trend, so it goes too — that one's a judgement call.
Operating settings 1 and 2 only wobble around a single setting in this
subset, so they carry nothing useful either. That leaves 14 sensors.

**Capping RUL at 125.** Early in an engine's life the sensors look flat,
so there's no way to tell a young engine with 250 flights left from one
with 30 — the difference comes from manufacturing variation the sensors
don't capture. Capping the target at 125 tells the model "healthy, a
long way from failure" instead of asking it to guess. Since every engine
here lasted at least 128 flights, the cap never cuts into the part where
degradation actually shows.

**Scoring at the final flight only.** The question is one prediction per
test engine, at the moment its data stops, so that's where the models
are scored.

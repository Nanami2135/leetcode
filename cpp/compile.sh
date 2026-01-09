workdir="${1:-.}"
cmake -S "$workdir" -B "$workdir/build" -DCMAKE_BUILD_TYPE=Debug
cmake --build "$workdir/build" --config Debug -- -j

# cmake -S . -B ./build -DCMAKE_BUILD_TYPE=Debug
# cmake --build ./build --config Debug -- -j

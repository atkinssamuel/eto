# formatting .cpp and .h files using astyle
astyle_formatter="astyle --max-code-length=80 --remove-comment-prefix --remove-braces --suffix=none"
$astyle_formatter main.cpp
for hfile in *.h; do
  $astyle_formatter "$hfile"
done;

# formatting Python files using Pyblack
black_formatter="black ."
cd ../
$black_formatter
cd palisade_container || exit

# building cpp solution
rm -r build
mkdir build
cd build || exit
cmake ..
make
cd ..

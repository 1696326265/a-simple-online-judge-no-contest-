cd pro
g++ refresh.cpp -o refresh
./refresh &
cd ..
cd sub/todo
g++ gao.cpp -o gao
./gao &
cd ../..
python3 main.py

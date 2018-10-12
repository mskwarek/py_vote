backend_dirs=`find ./*/backend -not -path '*/\.*' -type d`
for dir in ${backend_dirs}
do
	python -m unittest discover $dir "*_test.py"
done

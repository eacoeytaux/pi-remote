set -e

exec 200>$(dirname $0)/stepper.py.lock
flock -n 200 || exit 1
pid=$$
echo $pid 1>&200

echo "python $(dirname $0)/stepper.py $1"
python $(dirname $0)/stepper.py $1 $(dirname $0)/stepper.py.lastdir
echo "done"


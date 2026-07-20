#!/bin/bash
set -e

mkdir -p /logs/verifier

pytest -q --disable-warnings --maxfail=1
RESULT=$?

if [ $RESULT -eq 0 ]; then
  echo "1" > /logs/verifier/reward.txt
else
  echo "0" > /logs/verifier/reward.txt
fi

cat <<EOF > /logs/verifier/ctrf.json
{
  "tests_run": 3,
  "status": $RESULT
}
EOF

exit 0

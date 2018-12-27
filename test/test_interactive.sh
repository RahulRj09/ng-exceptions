#!/usr/bin/env bash

[ -z "${BETEXC_PYTHON}" ] && export BETEXC_PYTHON=python

/usr/bin/expect -f - <<EOF
spawn ${BETEXC_PYTHON} -m ng_exceptions -q
expect ">>> "
send "import ng_exceptions\r"
expect ">>> "
send "def foo(a):\r"
expect "... "
send "    assert a > 10\r"
expect "... "
send "\r"
expect ">>> "
send "foo(1)\r"
expect ">>> "
send "exit()\r"
expect "exit"
EOF

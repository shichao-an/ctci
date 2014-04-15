#!/bin/bash

usage="./makequestion.sh question_number [type]"
[ "$#" -lt 1 -o "$#" -gt 2  ] && { echo "$usage"; exit 1; }

qno="$1"
qtype="$2"
scriptdir=$(dirname "$0")
chapterdir="$scriptdir/chapter${qno%%.*}"
filename="${chapterdir}/question${qno}"


create_question ()
{
    [ -z "$qtype" ] && qtype="py"
    if [ "$qtype" = "py" ]
    then
        cat > "${filename}.$qtype" << EOF
from __future__ import print_function


def _test():
    pass

def _print():
    pass


if __name__ == '__main__':
    _test()
    _print()
EOF
    else
        touch "${filename}.$qtype"
    fi
}

if [ -d "$chapterdir" ]
then
    ls "$filename"* &> /dev/null && \
        { echo "This question already exists."; exit 1; }
    create_question
else
    mkdir "$chapterdir"
    create_question
fi

echo "${filename}.${qtype} created."

#!/bin/bash

set -euo pipefail
set -x

for i in bin/*; do
  cp ${i} /usr/local/bin/$(basename ${i})
done

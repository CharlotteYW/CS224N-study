#!/usr/bin/env bash
# Local environment for CS224N study and later assignment experiments.
# Assignment starter packages are added when that assignment begins.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is not on PATH." >&2
  exit 1
fi

echo "Using $(python3 --version)"
python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python - << 'PY'
import numpy
import torch

print(f"numpy {numpy.__version__}")
print(f"torch {torch.__version__}")
mps = getattr(torch.backends, "mps", None)
print(f"mps available: {bool(mps and torch.backends.mps.is_available())}")
PY

echo
echo "Environment is ready. Activate it with:"
echo "  source .venv/bin/activate"

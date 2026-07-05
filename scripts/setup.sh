#!/bin/bash
set -euo pipefail
echo "Setting up AWS Architecture Agent..."
pip install -e ".[dev]"
echo "Setup complete!"

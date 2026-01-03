#!/bin/bash

if [ -f "VERSION" ]; then
  echo "Artifact validation passed"
else
  echo "VERSION file missing"
  exit 1
fi

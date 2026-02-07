#!/bin/bash

source ./venv/Scripts/activate
python Update_readme.py

CURRENT_DATE=$(date +%Y-%m-%d)
LATEST_FILE=$(ls -t | grep -v "Update_readme.py" | grep -v "update_repo.sh" | head -n 1)

git add .
git commit -m "$CURRENT_DATE and $LATEST_FILE"
git push

deactivate
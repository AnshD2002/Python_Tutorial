& ./venv/Scripts/Activate.ps1
python Update_readme.py

$CURRENT_DATE = Get-Date -Format "yyyy-MM-dd"
$LATEST_FILE = Get-ChildItem | 
               Where-Object { $_.Name -ne "Update_readme.py" -and $_.Name -ne "update_repo.ps1" -and $_.Name -ne "venv" } | 
               Sort-Object LastWriteTime -Descending | 
               Select-Object -First 1 -ExpandProperty Name

git add .
git commit -m "$CURRENT_DATE and $LATEST_FILE"
git push

deactivate
# How to activate a venv env in python

## Activation Commands

### macOS/Linux (zsh/bash)

```bash
source .venv/bin/activate
```

### Windows (Command Prompt)

```cmd
.venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

## Deactivation

```bash
deactivate
```

## Full Example for this project

```bash
# Navigate to project directory
cd /Users/jacksu/Desktop/CODE/PYTHON/AI_ML

# Activate virtual environment
source .venv/bin/activate

# Your prompt should now show (.venv) at the beginning
# Install packages if needed
pip install package_name

# Run Python scripts
python your_script.py

# Deactivate when done
deactivate
```
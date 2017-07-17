# prereqs
# - virtual environment 'env' must be active
# - must be in 'app' directory
# run (from command line)
#   python create_db.py
#   or (?)
#   python ./scripts/create_db.py

import os, sys
sys.path.append(os.getcwd())  # must be run from 'app' directory

from main import db

if __name__ == '__main__':
  db.create_all()
'''
main entry point to app
- imports app from app.py (where it was configured)
- runs views, which tells app (loaded in memory here when imported) about routing
- can be run directly with Flask dev server
'''

from app import app, db
import models
import views

if __name__ == '__main__':
  app.run()
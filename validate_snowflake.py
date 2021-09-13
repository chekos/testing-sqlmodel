import os
from sqlalchemy import create_engine


SF_USER = os.environ["SF_USER"]
SF_PASS = os.environ["SF_PASS"]
SF_ACCT = os.environ["SF_ACCT"]

engine = create_engine(f"snowflake://{SF_USER}:{SF_PASS}@{SF_ACCT}/")
try:
    connection = engine.connect()
    results = connection.execute("select current_version()").fetchone()
    print(results[0])
finally:
    connection.close()
    engine.dispose()

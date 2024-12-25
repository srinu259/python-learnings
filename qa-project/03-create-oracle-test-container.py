import sys, pytest
if sys.platform.startswith('win') or sys.platform == 'darwin':
    pytest.skip("linux only test")

import sqlalchemy
from testcontainers.oracle import OracleDbContainer

with OracleDbContainer() as oracle:
    engine = sqlalchemy.create_engine(oracle.get_connection_url())
    with engine.begin() as connection:
        result = connection.execute(sqlalchemy.text("SELECT 1 FROM dual"))
        result.fetchall()


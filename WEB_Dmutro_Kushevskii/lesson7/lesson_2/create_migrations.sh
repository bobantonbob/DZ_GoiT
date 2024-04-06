#!/usr/bin/env python3

alembic init migrations
alembic revision --autogenerate -m 'Init'
alembic upgrade +1

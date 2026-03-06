import pytest
import os
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from shared.models import GatewayKey

@pytest.mark.asyncio
async def test_db():
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        return
    engine = create_async_engine(db_url)
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    
    async with async_session() as session:
        result = await session.execute(select(GatewayKey).limit(1))
        key = result.scalar_one_or_none()
        if key:
             print("Key Found")

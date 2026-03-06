import pytest
from shared.database import async_session_maker
from shared.models import Credential, Provider
from router.adapters import get_adapter
from sqlalchemy import select
from sqlalchemy.orm import selectinload

@pytest.mark.asyncio
async def test_openrouter():
    async with async_session_maker() as session:
        stmt = select(Credential).options(selectinload(Credential.provider)).where(Credential.label == 'unifyroute-key-DooSrar')
        cred = (await session.execute(stmt)).scalar_one_or_none()
        if not cred:
            return
        adapter = get_adapter("unifyroute")
        try:
            res = await adapter.chat(cred, [{"role": "user", "content": "hello"}], "meta-llama/llama-3.1-8b-instruct:free", stream=False)
            print(res)
        except Exception as e:
            print(f"Error: {e}")

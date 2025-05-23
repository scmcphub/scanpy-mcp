import pytest
from fastmcp import Client
import anndata
from pathlib import Path


@pytest.mark.asyncio 
async def test_read_and_write(mcp_config):
    # Pass the server directly to the Client constructor
    test_dir = Path(__file__).parent / "data/hg19"
    outfile = Path(__file__).parent / "data/test.h5ad"
    async with Client(mcp_config) as client:
        result = await client.call_tool("io_read", {"request":{"filename": test_dir}})
        assert "AnnData" in result[0].text

        result = await client.call_tool("io_write", {"request":{"filename": outfile}})
        assert outfile.exists()
        outfile.unlink()

import random
from fastmcp import FastMCP
import json

mcp = FastMCP("SimpleTools")


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """
    Do numbers ko add karta hai.

    Args:
        a: Pehla number
        b: Doosra number

    Returns:
        a aur b ka sum
    """
    return a + b


@mcp.tool()
def generate_random_number(min_value: int = 1, max_value: int = 100) -> int:
    """
    Diye gaye range ke beech ek random number generate karta hai.

    Args:
        min_value: Minimum value (default 1)
        max_value: Maximum value (default 100)

    Returns:
        min_value aur max_value ke beech ek random integer
    """
    return random.randint(min_value, max_value)


@mcp.resource("info://server")
def server_info() -> str:
    """
    Get the information about this server
    """
    
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0.0",
        "description": "A basic mcp server with math tools",
        "tools": ["add_numbers", "generate_random_number"],
        "author": "your name"
    }
    
    return json.dumps(info, indent=2)


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port="8000")
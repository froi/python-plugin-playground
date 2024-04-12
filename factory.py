from typing import Any, Callable
from parsers.parser import Parser

parser_creation_funcs: dict[str, Callable[..., Parser]] = {}

def register(parser_type: str, creation_func: Callable[..., Parser]):
    """Register a new parser type"""
    parser_creation_funcs[parser_type] = creation_func


def unregister(parser_type: str):
    """Register a new parser type"""
    parser_creation_funcs.pop(parser_type, None)


def create(arguments: dict[str, Any]) -> Parser:
    args_copy = arguments.copy()
    parser_type = args_copy.pop("type")

    try:
        creation_func = parser_creation_funcs[parser_type]
        return creation_func(**args_copy["data"])
    except KeyError:
        raise ValueError(f"Unknown parser type {parser_type!r}")

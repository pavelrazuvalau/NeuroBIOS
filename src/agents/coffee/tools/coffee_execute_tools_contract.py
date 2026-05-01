from typing import Any
from pydantic import BaseModel, Field
from neurobios.lm.models import ToolSchema, ToolFunctionSchema


class GrindCoffeeArgs(BaseModel):
    strength: str = Field(description="Coffee strength or amount of beans to grind")


class VolumeArgs(BaseModel):
    volume: float = Field(description="Volume to pour in units")


def build_tool_schema(
    name: str, description: str, args_model: type[BaseModel]
) -> ToolSchema:
    return ToolSchema(
        type="function",
        function=ToolFunctionSchema(
            name=name,
            description=description,
            parameters=args_model.model_json_schema(),
        ),
    )


COFFEE_TOOLS_LIST = [
    build_tool_schema(
        "grind_coffee", "Grinds coffee beans before pouring water", GrindCoffeeArgs
    ),
    build_tool_schema(
        "pour_water",
        "Pours hot water into the cup. Requires coffee to be ground first",
        VolumeArgs,
    ),
    build_tool_schema(
        "pour_milk",
        "Pours milk into the cup. Use only if the recipe requires milk (Cappuccino, Flat White)",
        VolumeArgs,
    ),
    build_tool_schema(
        "pour_chocolate",
        "Pours chocolate into the cup. Use only if the recipe requires chocolate (Hot Chocolate, Mocha)",
        VolumeArgs,
    ),
]

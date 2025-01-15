"""This file houses the protocol for the pipeline functions as well as the functions themselves"""

from functools import wraps
from typing import Any, Dict, Optional, Protocol, Union, runtime_checkable

import polars


@runtime_checkable
class PipelineFunc(Protocol):
    """This defines a protocol that all functions taking a pipeline class
    that inherits from BasicPipeline must adhere to."""

    def __call__(
        self,
        dataframe: Union[polars.DataFrame, polars.LazyFrame],
        parameters: Optional[Dict[str, Any]],
    ) -> Union[polars.DataFrame, polars.LazyFrame, None]:
        """Defines the typing of the call method the function must adhere to"""

        ...


def pipeline_func_protocol_check(f: PipelineFunc):
    """Decorator to check  the protocol before calling the function. Mainly for debugging and adherence principles."""

    @wraps(f)
    def wrapper(*args, **kwargs):
        """wrapper function"""
        if isinstance(f, PipelineFunc):
            return f(*args, **kwargs)
        else:
            raise TypeError(f"Expected PipelineFunc, got {type(f)}")

    return wrapper

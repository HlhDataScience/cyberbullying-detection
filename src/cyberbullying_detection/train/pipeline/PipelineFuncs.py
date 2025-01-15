"""This file houses the protocol for the pipeline functions as well as the functions themselves"""

from typing import Any, Dict, Optional, Protocol, Union

import polars


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

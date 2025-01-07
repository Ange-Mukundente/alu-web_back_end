
from typing import Tuple, Any, Union, Sequence,List


def zoom_array(lst: Sequence[int], factor: Union[int, float] = 2) -> Tuple[Union[int, float]]:

    if isinstance(factor, float):
        factor = int(factor)
    zoomed_in: List[Union[int, float]]= [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)

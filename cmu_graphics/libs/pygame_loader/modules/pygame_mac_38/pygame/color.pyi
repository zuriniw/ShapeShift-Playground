from typing import Text, Tuple, Union, overload, List, Optional

_ColorValue = Union[
    "Color", str, Tuple[int, int, int], List[int], int, Tuple[int, int, int, int]
]

class Color:
    r: int
    g: int
    b: int
    a: int
    cmy: Tuple[float, float, float]
    hsva: Tuple[float, float, float, float]
    hsla: Tuple[float, float, float, float]
    i1i2i3: Tuple[float, float, float]
    __hash__: None  # type: ignore
    @overload
    def __init__(self, r: int, g: int, b: int, a: Optional[int] = ...) -> None: ...
    @overload
    def __init__(self, rgbvalue: _ColorValue) -> None: ...
    @overload
    def __getitem__(self, i: int) -> int: ...
    @overload
    def __getitem__(self, s: slice) -> Tuple[int]: ...
    def __setitem__(self, key: int, value: int) -> None: ...
    def __add__(self, other: Color) -> Color: ...
    def __sub__(self, other: Color) -> Color: ...
    def __mul__(self, other: Color) -> Color: ...
    def __floordiv__(self, other: Color) -> Color: ...
    def __mod__(self, other: Color) -> Color: ...
    def normalize(self) -> Tuple[float, float, float, float]: ...
    def correct_gamma(self, gamma: float) -> Color: ...
    def set_length(self, length: int) -> None: ...
    def lerp(self, color: _ColorValue, amount: float) -> Color: ...
    def premul_alpha(self) -> Color: ...

import typing
from functools import reduce
from itertools import product
from operator import mul
from typing import Any, Literal, Tuple, TypeVar, TypeVarTuple, Union

import inflect

# Generated with:
# for i in range(65):
#      print(f"{inflect.engine().number_to_words(i).replace('-','').upper()} = Literal[{i}]")
ZERO = Literal[0]
ONE = Literal[1]
TWO = Literal[2]
THREE = Literal[3]
FOUR = Literal[4]
FIVE = Literal[5]
SIX = Literal[6]
SEVEN = Literal[7]
EIGHT = Literal[8]
NINE = Literal[9]
TEN = Literal[10]
ELEVEN = Literal[11]
TWELVE = Literal[12]
THIRTEEN = Literal[13]
FOURTEEN = Literal[14]
FIFTEEN = Literal[15]
SIXTEEN = Literal[16]
SEVENTEEN = Literal[17]
EIGHTEEN = Literal[18]
NINETEEN = Literal[19]
TWENTY = Literal[20]
TWENTYONE = Literal[21]
TWENTYTWO = Literal[22]
TWENTYTHREE = Literal[23]
TWENTYFOUR = Literal[24]
TWENTYFIVE = Literal[25]
TWENTYSIX = Literal[26]
TWENTYSEVEN = Literal[27]
TWENTYEIGHT = Literal[28]
TWENTYNINE = Literal[29]
THIRTY = Literal[30]
THIRTYONE = Literal[31]
THIRTYTWO = Literal[32]
THIRTYTHREE = Literal[33]
THIRTYFOUR = Literal[34]
THIRTYFIVE = Literal[35]
THIRTYSIX = Literal[36]
THIRTYSEVEN = Literal[37]
THIRTYEIGHT = Literal[38]
THIRTYNINE = Literal[39]
FORTY = Literal[40]
FORTYONE = Literal[41]
FORTYTWO = Literal[42]
FORTYTHREE = Literal[43]
FORTYFOUR = Literal[44]
FORTYFIVE = Literal[45]
FORTYSIX = Literal[46]
FORTYSEVEN = Literal[47]
FORTYEIGHT = Literal[48]
FORTYNINE = Literal[49]
FIFTY = Literal[50]
FIFTYONE = Literal[51]
FIFTYTWO = Literal[52]
FIFTYTHREE = Literal[53]
FIFTYFOUR = Literal[54]
FIFTYFIVE = Literal[55]
FIFTYSIX = Literal[56]
FIFTYSEVEN = Literal[57]
FIFTYEIGHT = Literal[58]
FIFTYNINE = Literal[59]
SIXTY = Literal[60]
SIXTYONE = Literal[61]
SIXTYTWO = Literal[62]
SIXTYTHREE = Literal[63]
SIXTYFOUR = Literal[64]

# Generated with:
# nums = [inflect.engine().number_to_words(i).replace('-','').upper() for i in range(65)]
# f"tuple([{', '.join(nums)}])"
ALL_NUMS = tuple(
    [
        ZERO,
        ONE,
        TWO,
        THREE,
        FOUR,
        FIVE,
        SIX,
        SEVEN,
        EIGHT,
        NINE,
        TEN,
        ELEVEN,
        TWELVE,
        THIRTEEN,
        FOURTEEN,
        FIFTEEN,
        SIXTEEN,
        SEVENTEEN,
        EIGHTEEN,
        NINETEEN,
        TWENTY,
        TWENTYONE,
        TWENTYTWO,
        TWENTYTHREE,
        TWENTYFOUR,
        TWENTYFIVE,
        TWENTYSIX,
        TWENTYSEVEN,
        TWENTYEIGHT,
        TWENTYNINE,
        THIRTY,
        THIRTYONE,
        THIRTYTWO,
        THIRTYTHREE,
        THIRTYFOUR,
        THIRTYFIVE,
        THIRTYSIX,
        THIRTYSEVEN,
        THIRTYEIGHT,
        THIRTYNINE,
        FORTY,
        FORTYONE,
        FORTYTWO,
        FORTYTHREE,
        FORTYFOUR,
        FORTYFIVE,
        FORTYSIX,
        FORTYSEVEN,
        FORTYEIGHT,
        FORTYNINE,
        FIFTY,
        FIFTYONE,
        FIFTYTWO,
        FIFTYTHREE,
        FIFTYFOUR,
        FIFTYFIVE,
        FIFTYSIX,
        FIFTYSEVEN,
        FIFTYEIGHT,
        FIFTYNINE,
        SIXTY,
        SIXTYONE,
        SIXTYTWO,
        SIXTYTHREE,
        SIXTYFOUR,
    ]
)

# Generated with:
# nums = [inflect.engine().number_to_words(i).replace('-','').upper() for i in range(65)]
# f"Union[{', '.join(nums)}]"
ALL_NUMS_Union = Union[
    ZERO,
    ONE,
    TWO,
    THREE,
    FOUR,
    FIVE,
    SIX,
    SEVEN,
    EIGHT,
    NINE,
    TEN,
    ELEVEN,
    TWELVE,
    THIRTEEN,
    FOURTEEN,
    FIFTEEN,
    SIXTEEN,
    SEVENTEEN,
    EIGHTEEN,
    NINETEEN,
    TWENTY,
    TWENTYONE,
    TWENTYTWO,
    TWENTYTHREE,
    TWENTYFOUR,
    TWENTYFIVE,
    TWENTYSIX,
    TWENTYSEVEN,
    TWENTYEIGHT,
    TWENTYNINE,
    THIRTY,
    THIRTYONE,
    THIRTYTWO,
    THIRTYTHREE,
    THIRTYFOUR,
    THIRTYFIVE,
    THIRTYSIX,
    THIRTYSEVEN,
    THIRTYEIGHT,
    THIRTYNINE,
    FORTY,
    FORTYONE,
    FORTYTWO,
    FORTYTHREE,
    FORTYFOUR,
    FORTYFIVE,
    FORTYSIX,
    FORTYSEVEN,
    FORTYEIGHT,
    FORTYNINE,
    FIFTY,
    FIFTYONE,
    FIFTYTWO,
    FIFTYTHREE,
    FIFTYFOUR,
    FIFTYFIVE,
    FIFTYSIX,
    FIFTYSEVEN,
    FIFTYEIGHT,
    FIFTYNINE,
    SIXTY,
    SIXTYONE,
    SIXTYTWO,
    SIXTYTHREE,
    SIXTYFOUR,
]

T1 = TypeVar("T1", bound=ALL_NUMS_Union)
T2 = TypeVar("T2", bound=ALL_NUMS_Union)
T3 = TypeVar("T3", bound=ALL_NUMS_Union)
T4 = TypeVar("T4", bound=ALL_NUMS_Union)
T5 = TypeVar("T5", bound=ALL_NUMS_Union)

Shape = Tuple
Shape1D = Shape[T1]
Shape2D = Shape[T1, T2]
Shape3D = Shape[T1, T2, T3]
Shape4D = Shape[T1, T2, T3, T4]
Shape5D = Shape[T1, T2, T3, T4, T5]

Shape1DType = TypeVar("Shape1DType", bound=Shape1D)
Shape2DType = TypeVar("Shape2DType", bound=Shape2D)
Shape3DType = TypeVar("Shape3DType", bound=Shape3D)
Shape4DType = TypeVar("Shape4DType", bound=Shape4D)
Shape5DType = TypeVar("Shape5DType", bound=Shape5D)

ShapeVarGen = TypeVarTuple("ShapeVarGen")

ShapeND = Shape[ALL_NUMS_Union, ...]

ShapeNDType = TypeVar("ShapeNDType", bound=ShapeND)

GenericDType = TypeVar("GenericDType", bound=Any)

# Generated with:
# for i in range(1, 65):
#     print(build_shape_mul_to(get_nd_shapes_for_ravel(ALL_NUMS, i, 2), i, 2))
SHAPE_2D_MUL_TO_ONE = TypeVar(
    "SHAPE_2D_MUL_TO_ONE",
    bound=Shape2D[Literal[ONE], Literal[ONE]],
)
SHAPE_2D_MUL_TO_TWO = TypeVar(
    "SHAPE_2D_MUL_TO_TWO",
    bound=Union[Shape2D[Literal[ONE], Literal[TWO]], Shape2D[Literal[TWO], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_THREE = TypeVar(
    "SHAPE_2D_MUL_TO_THREE",
    bound=Union[Shape2D[Literal[ONE], Literal[THREE]], Shape2D[Literal[THREE], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_FOUR = TypeVar(
    "SHAPE_2D_MUL_TO_FOUR",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FOUR]],
        Shape2D[Literal[TWO], Literal[TWO]],
        Shape2D[Literal[FOUR], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FIVE = TypeVar(
    "SHAPE_2D_MUL_TO_FIVE",
    bound=Union[Shape2D[Literal[ONE], Literal[FIVE]], Shape2D[Literal[FIVE], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_SIX = TypeVar(
    "SHAPE_2D_MUL_TO_SIX",
    bound=Union[
        Shape2D[Literal[ONE], Literal[SIX]],
        Shape2D[Literal[TWO], Literal[THREE]],
        Shape2D[Literal[THREE], Literal[TWO]],
        Shape2D[Literal[SIX], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_SEVEN = TypeVar(
    "SHAPE_2D_MUL_TO_SEVEN",
    bound=Union[Shape2D[Literal[ONE], Literal[SEVEN]], Shape2D[Literal[SEVEN], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_EIGHT = TypeVar(
    "SHAPE_2D_MUL_TO_EIGHT",
    bound=Union[
        Shape2D[Literal[ONE], Literal[EIGHT]],
        Shape2D[Literal[TWO], Literal[FOUR]],
        Shape2D[Literal[FOUR], Literal[TWO]],
        Shape2D[Literal[EIGHT], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_NINE = TypeVar(
    "SHAPE_2D_MUL_TO_NINE",
    bound=Union[
        Shape2D[Literal[ONE], Literal[NINE]],
        Shape2D[Literal[THREE], Literal[THREE]],
        Shape2D[Literal[NINE], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_TEN = TypeVar(
    "SHAPE_2D_MUL_TO_TEN",
    bound=Union[
        Shape2D[Literal[ONE], Literal[TEN]],
        Shape2D[Literal[TWO], Literal[FIVE]],
        Shape2D[Literal[FIVE], Literal[TWO]],
        Shape2D[Literal[TEN], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_ELEVEN = TypeVar(
    "SHAPE_2D_MUL_TO_ELEVEN",
    bound=Union[Shape2D[Literal[ONE], Literal[ELEVEN]], Shape2D[Literal[ELEVEN], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_TWELVE = TypeVar(
    "SHAPE_2D_MUL_TO_TWELVE",
    bound=Union[
        Shape2D[Literal[ONE], Literal[TWELVE]],
        Shape2D[Literal[TWO], Literal[SIX]],
        Shape2D[Literal[THREE], Literal[FOUR]],
        Shape2D[Literal[FOUR], Literal[THREE]],
        Shape2D[Literal[SIX], Literal[TWO]],
        Shape2D[Literal[TWELVE], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_THIRTEEN = TypeVar(
    "SHAPE_2D_MUL_TO_THIRTEEN",
    bound=Union[Shape2D[Literal[ONE], Literal[THIRTEEN]], Shape2D[Literal[THIRTEEN], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_FOURTEEN = TypeVar(
    "SHAPE_2D_MUL_TO_FOURTEEN",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FOURTEEN]],
        Shape2D[Literal[TWO], Literal[SEVEN]],
        Shape2D[Literal[SEVEN], Literal[TWO]],
        Shape2D[Literal[FOURTEEN], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FIFTEEN = TypeVar(
    "SHAPE_2D_MUL_TO_FIFTEEN",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FIFTEEN]],
        Shape2D[Literal[THREE], Literal[FIVE]],
        Shape2D[Literal[FIVE], Literal[THREE]],
        Shape2D[Literal[FIFTEEN], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_SIXTEEN = TypeVar(
    "SHAPE_2D_MUL_TO_SIXTEEN",
    bound=Union[
        Shape2D[Literal[ONE], Literal[SIXTEEN]],
        Shape2D[Literal[TWO], Literal[EIGHT]],
        Shape2D[Literal[FOUR], Literal[FOUR]],
        Shape2D[Literal[EIGHT], Literal[TWO]],
        Shape2D[Literal[SIXTEEN], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_SEVENTEEN = TypeVar(
    "SHAPE_2D_MUL_TO_SEVENTEEN",
    bound=Union[Shape2D[Literal[ONE], Literal[SEVENTEEN]], Shape2D[Literal[SEVENTEEN], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_EIGHTEEN = TypeVar(
    "SHAPE_2D_MUL_TO_EIGHTEEN",
    bound=Union[
        Shape2D[Literal[ONE], Literal[EIGHTEEN]],
        Shape2D[Literal[TWO], Literal[NINE]],
        Shape2D[Literal[THREE], Literal[SIX]],
        Shape2D[Literal[SIX], Literal[THREE]],
        Shape2D[Literal[NINE], Literal[TWO]],
        Shape2D[Literal[EIGHTEEN], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_NINETEEN = TypeVar(
    "SHAPE_2D_MUL_TO_NINETEEN",
    bound=Union[Shape2D[Literal[ONE], Literal[NINETEEN]], Shape2D[Literal[NINETEEN], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_TWENTY = TypeVar(
    "SHAPE_2D_MUL_TO_TWENTY",
    bound=Union[
        Shape2D[Literal[ONE], Literal[TWENTY]],
        Shape2D[Literal[TWO], Literal[TEN]],
        Shape2D[Literal[FOUR], Literal[FIVE]],
        Shape2D[Literal[FIVE], Literal[FOUR]],
        Shape2D[Literal[TEN], Literal[TWO]],
        Shape2D[Literal[TWENTY], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_TWENTYONE = TypeVar(
    "SHAPE_2D_MUL_TO_TWENTYONE",
    bound=Union[
        Shape2D[Literal[ONE], Literal[TWENTYONE]],
        Shape2D[Literal[THREE], Literal[SEVEN]],
        Shape2D[Literal[SEVEN], Literal[THREE]],
        Shape2D[Literal[TWENTYONE], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_TWENTYTWO = TypeVar(
    "SHAPE_2D_MUL_TO_TWENTYTWO",
    bound=Union[
        Shape2D[Literal[ONE], Literal[TWENTYTWO]],
        Shape2D[Literal[TWO], Literal[ELEVEN]],
        Shape2D[Literal[ELEVEN], Literal[TWO]],
        Shape2D[Literal[TWENTYTWO], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_TWENTYTHREE = TypeVar(
    "SHAPE_2D_MUL_TO_TWENTYTHREE",
    bound=Union[Shape2D[Literal[ONE], Literal[TWENTYTHREE]], Shape2D[Literal[TWENTYTHREE], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_TWENTYFOUR = TypeVar(
    "SHAPE_2D_MUL_TO_TWENTYFOUR",
    bound=Union[
        Shape2D[Literal[ONE], Literal[TWENTYFOUR]],
        Shape2D[Literal[TWO], Literal[TWELVE]],
        Shape2D[Literal[THREE], Literal[EIGHT]],
        Shape2D[Literal[FOUR], Literal[SIX]],
        Shape2D[Literal[SIX], Literal[FOUR]],
        Shape2D[Literal[EIGHT], Literal[THREE]],
        Shape2D[Literal[TWELVE], Literal[TWO]],
        Shape2D[Literal[TWENTYFOUR], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_TWENTYFIVE = TypeVar(
    "SHAPE_2D_MUL_TO_TWENTYFIVE",
    bound=Union[
        Shape2D[Literal[ONE], Literal[TWENTYFIVE]],
        Shape2D[Literal[FIVE], Literal[FIVE]],
        Shape2D[Literal[TWENTYFIVE], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_TWENTYSIX = TypeVar(
    "SHAPE_2D_MUL_TO_TWENTYSIX",
    bound=Union[
        Shape2D[Literal[ONE], Literal[TWENTYSIX]],
        Shape2D[Literal[TWO], Literal[THIRTEEN]],
        Shape2D[Literal[THIRTEEN], Literal[TWO]],
        Shape2D[Literal[TWENTYSIX], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_TWENTYSEVEN = TypeVar(
    "SHAPE_2D_MUL_TO_TWENTYSEVEN",
    bound=Union[
        Shape2D[Literal[ONE], Literal[TWENTYSEVEN]],
        Shape2D[Literal[THREE], Literal[NINE]],
        Shape2D[Literal[NINE], Literal[THREE]],
        Shape2D[Literal[TWENTYSEVEN], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_TWENTYEIGHT = TypeVar(
    "SHAPE_2D_MUL_TO_TWENTYEIGHT",
    bound=Union[
        Shape2D[Literal[ONE], Literal[TWENTYEIGHT]],
        Shape2D[Literal[TWO], Literal[FOURTEEN]],
        Shape2D[Literal[FOUR], Literal[SEVEN]],
        Shape2D[Literal[SEVEN], Literal[FOUR]],
        Shape2D[Literal[FOURTEEN], Literal[TWO]],
        Shape2D[Literal[TWENTYEIGHT], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_TWENTYNINE = TypeVar(
    "SHAPE_2D_MUL_TO_TWENTYNINE",
    bound=Union[Shape2D[Literal[ONE], Literal[TWENTYNINE]], Shape2D[Literal[TWENTYNINE], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_THIRTY = TypeVar(
    "SHAPE_2D_MUL_TO_THIRTY",
    bound=Union[
        Shape2D[Literal[ONE], Literal[THIRTY]],
        Shape2D[Literal[TWO], Literal[FIFTEEN]],
        Shape2D[Literal[THREE], Literal[TEN]],
        Shape2D[Literal[FIVE], Literal[SIX]],
        Shape2D[Literal[SIX], Literal[FIVE]],
        Shape2D[Literal[TEN], Literal[THREE]],
        Shape2D[Literal[FIFTEEN], Literal[TWO]],
        Shape2D[Literal[THIRTY], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_THIRTYONE = TypeVar(
    "SHAPE_2D_MUL_TO_THIRTYONE",
    bound=Union[Shape2D[Literal[ONE], Literal[THIRTYONE]], Shape2D[Literal[THIRTYONE], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_THIRTYTWO = TypeVar(
    "SHAPE_2D_MUL_TO_THIRTYTWO",
    bound=Union[
        Shape2D[Literal[ONE], Literal[THIRTYTWO]],
        Shape2D[Literal[TWO], Literal[SIXTEEN]],
        Shape2D[Literal[FOUR], Literal[EIGHT]],
        Shape2D[Literal[EIGHT], Literal[FOUR]],
        Shape2D[Literal[SIXTEEN], Literal[TWO]],
        Shape2D[Literal[THIRTYTWO], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_THIRTYTHREE = TypeVar(
    "SHAPE_2D_MUL_TO_THIRTYTHREE",
    bound=Union[
        Shape2D[Literal[ONE], Literal[THIRTYTHREE]],
        Shape2D[Literal[THREE], Literal[ELEVEN]],
        Shape2D[Literal[ELEVEN], Literal[THREE]],
        Shape2D[Literal[THIRTYTHREE], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_THIRTYFOUR = TypeVar(
    "SHAPE_2D_MUL_TO_THIRTYFOUR",
    bound=Union[
        Shape2D[Literal[ONE], Literal[THIRTYFOUR]],
        Shape2D[Literal[TWO], Literal[SEVENTEEN]],
        Shape2D[Literal[SEVENTEEN], Literal[TWO]],
        Shape2D[Literal[THIRTYFOUR], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_THIRTYFIVE = TypeVar(
    "SHAPE_2D_MUL_TO_THIRTYFIVE",
    bound=Union[
        Shape2D[Literal[ONE], Literal[THIRTYFIVE]],
        Shape2D[Literal[FIVE], Literal[SEVEN]],
        Shape2D[Literal[SEVEN], Literal[FIVE]],
        Shape2D[Literal[THIRTYFIVE], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_THIRTYSIX = TypeVar(
    "SHAPE_2D_MUL_TO_THIRTYSIX",
    bound=Union[
        Shape2D[Literal[ONE], Literal[THIRTYSIX]],
        Shape2D[Literal[TWO], Literal[EIGHTEEN]],
        Shape2D[Literal[THREE], Literal[TWELVE]],
        Shape2D[Literal[FOUR], Literal[NINE]],
        Shape2D[Literal[SIX], Literal[SIX]],
        Shape2D[Literal[NINE], Literal[FOUR]],
        Shape2D[Literal[TWELVE], Literal[THREE]],
        Shape2D[Literal[EIGHTEEN], Literal[TWO]],
        Shape2D[Literal[THIRTYSIX], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_THIRTYSEVEN = TypeVar(
    "SHAPE_2D_MUL_TO_THIRTYSEVEN",
    bound=Union[Shape2D[Literal[ONE], Literal[THIRTYSEVEN]], Shape2D[Literal[THIRTYSEVEN], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_THIRTYEIGHT = TypeVar(
    "SHAPE_2D_MUL_TO_THIRTYEIGHT",
    bound=Union[
        Shape2D[Literal[ONE], Literal[THIRTYEIGHT]],
        Shape2D[Literal[TWO], Literal[NINETEEN]],
        Shape2D[Literal[NINETEEN], Literal[TWO]],
        Shape2D[Literal[THIRTYEIGHT], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_THIRTYNINE = TypeVar(
    "SHAPE_2D_MUL_TO_THIRTYNINE",
    bound=Union[
        Shape2D[Literal[ONE], Literal[THIRTYNINE]],
        Shape2D[Literal[THREE], Literal[THIRTEEN]],
        Shape2D[Literal[THIRTEEN], Literal[THREE]],
        Shape2D[Literal[THIRTYNINE], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FORTY = TypeVar(
    "SHAPE_2D_MUL_TO_FORTY",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FORTY]],
        Shape2D[Literal[TWO], Literal[TWENTY]],
        Shape2D[Literal[FOUR], Literal[TEN]],
        Shape2D[Literal[FIVE], Literal[EIGHT]],
        Shape2D[Literal[EIGHT], Literal[FIVE]],
        Shape2D[Literal[TEN], Literal[FOUR]],
        Shape2D[Literal[TWENTY], Literal[TWO]],
        Shape2D[Literal[FORTY], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FORTYONE = TypeVar(
    "SHAPE_2D_MUL_TO_FORTYONE",
    bound=Union[Shape2D[Literal[ONE], Literal[FORTYONE]], Shape2D[Literal[FORTYONE], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_FORTYTWO = TypeVar(
    "SHAPE_2D_MUL_TO_FORTYTWO",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FORTYTWO]],
        Shape2D[Literal[TWO], Literal[TWENTYONE]],
        Shape2D[Literal[THREE], Literal[FOURTEEN]],
        Shape2D[Literal[SIX], Literal[SEVEN]],
        Shape2D[Literal[SEVEN], Literal[SIX]],
        Shape2D[Literal[FOURTEEN], Literal[THREE]],
        Shape2D[Literal[TWENTYONE], Literal[TWO]],
        Shape2D[Literal[FORTYTWO], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FORTYTHREE = TypeVar(
    "SHAPE_2D_MUL_TO_FORTYTHREE",
    bound=Union[Shape2D[Literal[ONE], Literal[FORTYTHREE]], Shape2D[Literal[FORTYTHREE], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_FORTYFOUR = TypeVar(
    "SHAPE_2D_MUL_TO_FORTYFOUR",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FORTYFOUR]],
        Shape2D[Literal[TWO], Literal[TWENTYTWO]],
        Shape2D[Literal[FOUR], Literal[ELEVEN]],
        Shape2D[Literal[ELEVEN], Literal[FOUR]],
        Shape2D[Literal[TWENTYTWO], Literal[TWO]],
        Shape2D[Literal[FORTYFOUR], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FORTYFIVE = TypeVar(
    "SHAPE_2D_MUL_TO_FORTYFIVE",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FORTYFIVE]],
        Shape2D[Literal[THREE], Literal[FIFTEEN]],
        Shape2D[Literal[FIVE], Literal[NINE]],
        Shape2D[Literal[NINE], Literal[FIVE]],
        Shape2D[Literal[FIFTEEN], Literal[THREE]],
        Shape2D[Literal[FORTYFIVE], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FORTYSIX = TypeVar(
    "SHAPE_2D_MUL_TO_FORTYSIX",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FORTYSIX]],
        Shape2D[Literal[TWO], Literal[TWENTYTHREE]],
        Shape2D[Literal[TWENTYTHREE], Literal[TWO]],
        Shape2D[Literal[FORTYSIX], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FORTYSEVEN = TypeVar(
    "SHAPE_2D_MUL_TO_FORTYSEVEN",
    bound=Union[Shape2D[Literal[ONE], Literal[FORTYSEVEN]], Shape2D[Literal[FORTYSEVEN], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_FORTYEIGHT = TypeVar(
    "SHAPE_2D_MUL_TO_FORTYEIGHT",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FORTYEIGHT]],
        Shape2D[Literal[TWO], Literal[TWENTYFOUR]],
        Shape2D[Literal[THREE], Literal[SIXTEEN]],
        Shape2D[Literal[FOUR], Literal[TWELVE]],
        Shape2D[Literal[SIX], Literal[EIGHT]],
        Shape2D[Literal[EIGHT], Literal[SIX]],
        Shape2D[Literal[TWELVE], Literal[FOUR]],
        Shape2D[Literal[SIXTEEN], Literal[THREE]],
        Shape2D[Literal[TWENTYFOUR], Literal[TWO]],
        Shape2D[Literal[FORTYEIGHT], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FORTYNINE = TypeVar(
    "SHAPE_2D_MUL_TO_FORTYNINE",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FORTYNINE]],
        Shape2D[Literal[SEVEN], Literal[SEVEN]],
        Shape2D[Literal[FORTYNINE], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FIFTY = TypeVar(
    "SHAPE_2D_MUL_TO_FIFTY",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FIFTY]],
        Shape2D[Literal[TWO], Literal[TWENTYFIVE]],
        Shape2D[Literal[FIVE], Literal[TEN]],
        Shape2D[Literal[TEN], Literal[FIVE]],
        Shape2D[Literal[TWENTYFIVE], Literal[TWO]],
        Shape2D[Literal[FIFTY], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FIFTYONE = TypeVar(
    "SHAPE_2D_MUL_TO_FIFTYONE",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FIFTYONE]],
        Shape2D[Literal[THREE], Literal[SEVENTEEN]],
        Shape2D[Literal[SEVENTEEN], Literal[THREE]],
        Shape2D[Literal[FIFTYONE], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FIFTYTWO = TypeVar(
    "SHAPE_2D_MUL_TO_FIFTYTWO",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FIFTYTWO]],
        Shape2D[Literal[TWO], Literal[TWENTYSIX]],
        Shape2D[Literal[FOUR], Literal[THIRTEEN]],
        Shape2D[Literal[THIRTEEN], Literal[FOUR]],
        Shape2D[Literal[TWENTYSIX], Literal[TWO]],
        Shape2D[Literal[FIFTYTWO], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FIFTYTHREE = TypeVar(
    "SHAPE_2D_MUL_TO_FIFTYTHREE",
    bound=Union[Shape2D[Literal[ONE], Literal[FIFTYTHREE]], Shape2D[Literal[FIFTYTHREE], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_FIFTYFOUR = TypeVar(
    "SHAPE_2D_MUL_TO_FIFTYFOUR",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FIFTYFOUR]],
        Shape2D[Literal[TWO], Literal[TWENTYSEVEN]],
        Shape2D[Literal[THREE], Literal[EIGHTEEN]],
        Shape2D[Literal[SIX], Literal[NINE]],
        Shape2D[Literal[NINE], Literal[SIX]],
        Shape2D[Literal[EIGHTEEN], Literal[THREE]],
        Shape2D[Literal[TWENTYSEVEN], Literal[TWO]],
        Shape2D[Literal[FIFTYFOUR], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FIFTYFIVE = TypeVar(
    "SHAPE_2D_MUL_TO_FIFTYFIVE",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FIFTYFIVE]],
        Shape2D[Literal[FIVE], Literal[ELEVEN]],
        Shape2D[Literal[ELEVEN], Literal[FIVE]],
        Shape2D[Literal[FIFTYFIVE], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FIFTYSIX = TypeVar(
    "SHAPE_2D_MUL_TO_FIFTYSIX",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FIFTYSIX]],
        Shape2D[Literal[TWO], Literal[TWENTYEIGHT]],
        Shape2D[Literal[FOUR], Literal[FOURTEEN]],
        Shape2D[Literal[SEVEN], Literal[EIGHT]],
        Shape2D[Literal[EIGHT], Literal[SEVEN]],
        Shape2D[Literal[FOURTEEN], Literal[FOUR]],
        Shape2D[Literal[TWENTYEIGHT], Literal[TWO]],
        Shape2D[Literal[FIFTYSIX], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FIFTYSEVEN = TypeVar(
    "SHAPE_2D_MUL_TO_FIFTYSEVEN",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FIFTYSEVEN]],
        Shape2D[Literal[THREE], Literal[NINETEEN]],
        Shape2D[Literal[NINETEEN], Literal[THREE]],
        Shape2D[Literal[FIFTYSEVEN], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FIFTYEIGHT = TypeVar(
    "SHAPE_2D_MUL_TO_FIFTYEIGHT",
    bound=Union[
        Shape2D[Literal[ONE], Literal[FIFTYEIGHT]],
        Shape2D[Literal[TWO], Literal[TWENTYNINE]],
        Shape2D[Literal[TWENTYNINE], Literal[TWO]],
        Shape2D[Literal[FIFTYEIGHT], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_FIFTYNINE = TypeVar(
    "SHAPE_2D_MUL_TO_FIFTYNINE",
    bound=Union[Shape2D[Literal[ONE], Literal[FIFTYNINE]], Shape2D[Literal[FIFTYNINE], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_SIXTY = TypeVar(
    "SHAPE_2D_MUL_TO_SIXTY",
    bound=Union[
        Shape2D[Literal[ONE], Literal[SIXTY]],
        Shape2D[Literal[TWO], Literal[THIRTY]],
        Shape2D[Literal[THREE], Literal[TWENTY]],
        Shape2D[Literal[FOUR], Literal[FIFTEEN]],
        Shape2D[Literal[FIVE], Literal[TWELVE]],
        Shape2D[Literal[SIX], Literal[TEN]],
        Shape2D[Literal[TEN], Literal[SIX]],
        Shape2D[Literal[TWELVE], Literal[FIVE]],
        Shape2D[Literal[FIFTEEN], Literal[FOUR]],
        Shape2D[Literal[TWENTY], Literal[THREE]],
        Shape2D[Literal[THIRTY], Literal[TWO]],
        Shape2D[Literal[SIXTY], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_SIXTYONE = TypeVar(
    "SHAPE_2D_MUL_TO_SIXTYONE",
    bound=Union[Shape2D[Literal[ONE], Literal[SIXTYONE]], Shape2D[Literal[SIXTYONE], Literal[ONE]]],
)
SHAPE_2D_MUL_TO_SIXTYTWO = TypeVar(
    "SHAPE_2D_MUL_TO_SIXTYTWO",
    bound=Union[
        Shape2D[Literal[ONE], Literal[SIXTYTWO]],
        Shape2D[Literal[TWO], Literal[THIRTYONE]],
        Shape2D[Literal[THIRTYONE], Literal[TWO]],
        Shape2D[Literal[SIXTYTWO], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_SIXTYTHREE = TypeVar(
    "SHAPE_2D_MUL_TO_SIXTYTHREE",
    bound=Union[
        Shape2D[Literal[ONE], Literal[SIXTYTHREE]],
        Shape2D[Literal[THREE], Literal[TWENTYONE]],
        Shape2D[Literal[SEVEN], Literal[NINE]],
        Shape2D[Literal[NINE], Literal[SEVEN]],
        Shape2D[Literal[TWENTYONE], Literal[THREE]],
        Shape2D[Literal[SIXTYTHREE], Literal[ONE]],
    ],
)
SHAPE_2D_MUL_TO_SIXTYFOUR = TypeVar(
    "SHAPE_2D_MUL_TO_SIXTYFOUR",
    bound=Union[
        Shape2D[Literal[ONE], Literal[SIXTYFOUR]],
        Shape2D[Literal[TWO], Literal[THIRTYTWO]],
        Shape2D[Literal[FOUR], Literal[SIXTEEN]],
        Shape2D[Literal[EIGHT], Literal[EIGHT]],
        Shape2D[Literal[SIXTEEN], Literal[FOUR]],
        Shape2D[Literal[THIRTYTWO], Literal[TWO]],
        Shape2D[Literal[SIXTYFOUR], Literal[ONE]],
    ],
)

##
## Code gen tools
##


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


def get_nd_shapes_for_ravel(factors: list, final_dim_size: int, start_dim: int):
    all_factors = filter(lambda i: i.__args__[0] <= final_dim_size, factors)
    return list(
        filter(
            lambda seq: reduce(mul, map(lambda i: i.__args__[0], seq), 1) == final_dim_size,
            product(all_factors, repeat=start_dim),
        )
    )


def build_shape_mul_to(factor_tuples: list[tuple], final_dim_size: int, start_dim: int):
    if start_dim == 1:
        shape_nd_type = Shape1D
    if start_dim == 2:
        shape_nd_type = Shape2D
    if start_dim == 3:
        shape_nd_type = Shape3D
    if start_dim == 4:
        shape_nd_type = Shape4D
    if start_dim == 5:
        shape_nd_type = Shape5D
    final_dim_size_str = inflect.engine().number_to_words(final_dim_size).upper().replace("-", "")  # type: ignore
    shape_nd_type_str = namestr(shape_nd_type, globals())[0]  # type: ignore
    factor_tuple_strings = [
        ", ".join([f"Literal[{namestr(f, globals())[0]}]" for f in ft]) for ft in factor_tuples
    ]
    shape_factor_tuple_str = ", ".join([f"{shape_nd_type_str}[{ft}]" for ft in factor_tuple_strings])
    return_str = f"""SHAPE_{start_dim}D_MUL_TO_{final_dim_size_str} = TypeVar("SHAPE_{start_dim}D_MUL_TO_{final_dim_size_str}",bound=Union[{shape_factor_tuple_str}],)"""
    return return_str

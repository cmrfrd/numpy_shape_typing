from typing import overload

from numpy.typing import NDArray

from numpy_shape_typing.types import (
    EIGHT,
    EIGHTEEN,
    ELEVEN,
    FIFTEEN,
    FIFTY,
    FIFTYEIGHT,
    FIFTYFIVE,
    FIFTYFOUR,
    FIFTYNINE,
    FIFTYONE,
    FIFTYSEVEN,
    FIFTYSIX,
    FIFTYTHREE,
    FIFTYTWO,
    FIVE,
    FORTY,
    FORTYEIGHT,
    FORTYFIVE,
    FORTYFOUR,
    FORTYNINE,
    FORTYONE,
    FORTYSEVEN,
    FORTYSIX,
    FORTYTHREE,
    FORTYTWO,
    FOUR,
    FOURTEEN,
    NINE,
    NINETEEN,
    ONE,
    SEVEN,
    SEVENTEEN,
    SHAPE_2D_MUL_TO_EIGHT,
    SHAPE_2D_MUL_TO_EIGHTEEN,
    SHAPE_2D_MUL_TO_ELEVEN,
    SHAPE_2D_MUL_TO_FIFTEEN,
    SHAPE_2D_MUL_TO_FIFTY,
    SHAPE_2D_MUL_TO_FIFTYEIGHT,
    SHAPE_2D_MUL_TO_FIFTYFIVE,
    SHAPE_2D_MUL_TO_FIFTYFOUR,
    SHAPE_2D_MUL_TO_FIFTYNINE,
    SHAPE_2D_MUL_TO_FIFTYONE,
    SHAPE_2D_MUL_TO_FIFTYSEVEN,
    SHAPE_2D_MUL_TO_FIFTYSIX,
    SHAPE_2D_MUL_TO_FIFTYTHREE,
    SHAPE_2D_MUL_TO_FIFTYTWO,
    SHAPE_2D_MUL_TO_FIVE,
    SHAPE_2D_MUL_TO_FORTY,
    SHAPE_2D_MUL_TO_FORTYEIGHT,
    SHAPE_2D_MUL_TO_FORTYFIVE,
    SHAPE_2D_MUL_TO_FORTYFOUR,
    SHAPE_2D_MUL_TO_FORTYNINE,
    SHAPE_2D_MUL_TO_FORTYONE,
    SHAPE_2D_MUL_TO_FORTYSEVEN,
    SHAPE_2D_MUL_TO_FORTYSIX,
    SHAPE_2D_MUL_TO_FORTYTHREE,
    SHAPE_2D_MUL_TO_FORTYTWO,
    SHAPE_2D_MUL_TO_FOUR,
    SHAPE_2D_MUL_TO_FOURTEEN,
    SHAPE_2D_MUL_TO_NINE,
    SHAPE_2D_MUL_TO_NINETEEN,
    SHAPE_2D_MUL_TO_ONE,
    SHAPE_2D_MUL_TO_SEVEN,
    SHAPE_2D_MUL_TO_SEVENTEEN,
    SHAPE_2D_MUL_TO_SIX,
    SHAPE_2D_MUL_TO_SIXTEEN,
    SHAPE_2D_MUL_TO_SIXTY,
    SHAPE_2D_MUL_TO_SIXTYFOUR,
    SHAPE_2D_MUL_TO_SIXTYONE,
    SHAPE_2D_MUL_TO_SIXTYTHREE,
    SHAPE_2D_MUL_TO_SIXTYTWO,
    SHAPE_2D_MUL_TO_TEN,
    SHAPE_2D_MUL_TO_THIRTEEN,
    SHAPE_2D_MUL_TO_THIRTY,
    SHAPE_2D_MUL_TO_THIRTYEIGHT,
    SHAPE_2D_MUL_TO_THIRTYFIVE,
    SHAPE_2D_MUL_TO_THIRTYFOUR,
    SHAPE_2D_MUL_TO_THIRTYNINE,
    SHAPE_2D_MUL_TO_THIRTYONE,
    SHAPE_2D_MUL_TO_THIRTYSEVEN,
    SHAPE_2D_MUL_TO_THIRTYSIX,
    SHAPE_2D_MUL_TO_THIRTYTHREE,
    SHAPE_2D_MUL_TO_THIRTYTWO,
    SHAPE_2D_MUL_TO_THREE,
    SHAPE_2D_MUL_TO_TWELVE,
    SHAPE_2D_MUL_TO_TWENTY,
    SHAPE_2D_MUL_TO_TWENTYEIGHT,
    SHAPE_2D_MUL_TO_TWENTYFIVE,
    SHAPE_2D_MUL_TO_TWENTYFOUR,
    SHAPE_2D_MUL_TO_TWENTYNINE,
    SHAPE_2D_MUL_TO_TWENTYONE,
    SHAPE_2D_MUL_TO_TWENTYSEVEN,
    SHAPE_2D_MUL_TO_TWENTYSIX,
    SHAPE_2D_MUL_TO_TWENTYTHREE,
    SHAPE_2D_MUL_TO_TWENTYTWO,
    SHAPE_2D_MUL_TO_TWO,
    SIX,
    SIXTEEN,
    SIXTY,
    SIXTYFOUR,
    SIXTYONE,
    SIXTYTHREE,
    SIXTYTWO,
    T1,
    TEN,
    THIRTEEN,
    THIRTY,
    THIRTYEIGHT,
    THIRTYFIVE,
    THIRTYFOUR,
    THIRTYNINE,
    THIRTYONE,
    THIRTYSEVEN,
    THIRTYSIX,
    THIRTYTHREE,
    THIRTYTWO,
    THREE,
    TWELVE,
    TWENTY,
    TWENTYEIGHT,
    TWENTYFIVE,
    TWENTYFOUR,
    TWENTYNINE,
    TWENTYONE,
    TWENTYSEVEN,
    TWENTYSIX,
    TWENTYTHREE,
    TWENTYTWO,
    TWO,
    GenericDType,
    Shape1D,
    Shape2D,
)

# Generated with:
# for i in range(1, 65):
#     res = build_shape_mul_to(get_nd_shapes_for_ravel(ALL_NUMS, i, 2), i, 2).split(" ")[0]
#     i_str = inflect.engine().number_to_words(i).upper().replace("-", "")
#     print(
#         f'''
#     @overload
#     def ravel(arr: NDArray[{res}, GenericDType]) -> NDArray[Shape1D[{i_str}], GenericDType]:
#         ...
#         '''
#     )


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_ONE, GenericDType]) -> NDArray[Shape1D[ONE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_TWO, GenericDType]) -> NDArray[Shape1D[TWO], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_THREE, GenericDType]) -> NDArray[Shape1D[THREE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FOUR, GenericDType]) -> NDArray[Shape1D[FOUR], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FIVE, GenericDType]) -> NDArray[Shape1D[FIVE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_SIX, GenericDType]) -> NDArray[Shape1D[SIX], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_SEVEN, GenericDType]) -> NDArray[Shape1D[SEVEN], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_EIGHT, GenericDType]) -> NDArray[Shape1D[EIGHT], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_NINE, GenericDType]) -> NDArray[Shape1D[NINE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_TEN, GenericDType]) -> NDArray[Shape1D[TEN], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_ELEVEN, GenericDType]) -> NDArray[Shape1D[ELEVEN], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_TWELVE, GenericDType]) -> NDArray[Shape1D[TWELVE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_THIRTEEN, GenericDType]) -> NDArray[Shape1D[THIRTEEN], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FOURTEEN, GenericDType]) -> NDArray[Shape1D[FOURTEEN], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FIFTEEN, GenericDType]) -> NDArray[Shape1D[FIFTEEN], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_SIXTEEN, GenericDType]) -> NDArray[Shape1D[SIXTEEN], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_SEVENTEEN, GenericDType]) -> NDArray[Shape1D[SEVENTEEN], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_EIGHTEEN, GenericDType]) -> NDArray[Shape1D[EIGHTEEN], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_NINETEEN, GenericDType]) -> NDArray[Shape1D[NINETEEN], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_TWENTY, GenericDType]) -> NDArray[Shape1D[TWENTY], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_TWENTYONE, GenericDType]) -> NDArray[Shape1D[TWENTYONE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_TWENTYTWO, GenericDType]) -> NDArray[Shape1D[TWENTYTWO], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_TWENTYTHREE, GenericDType]
) -> NDArray[Shape1D[TWENTYTHREE], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_TWENTYFOUR, GenericDType]
) -> NDArray[Shape1D[TWENTYFOUR], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_TWENTYFIVE, GenericDType]
) -> NDArray[Shape1D[TWENTYFIVE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_TWENTYSIX, GenericDType]) -> NDArray[Shape1D[TWENTYSIX], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_TWENTYSEVEN, GenericDType]
) -> NDArray[Shape1D[TWENTYSEVEN], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_TWENTYEIGHT, GenericDType]
) -> NDArray[Shape1D[TWENTYEIGHT], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_TWENTYNINE, GenericDType]
) -> NDArray[Shape1D[TWENTYNINE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_THIRTY, GenericDType]) -> NDArray[Shape1D[THIRTY], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_THIRTYONE, GenericDType]) -> NDArray[Shape1D[THIRTYONE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_THIRTYTWO, GenericDType]) -> NDArray[Shape1D[THIRTYTWO], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_THIRTYTHREE, GenericDType]
) -> NDArray[Shape1D[THIRTYTHREE], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_THIRTYFOUR, GenericDType]
) -> NDArray[Shape1D[THIRTYFOUR], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_THIRTYFIVE, GenericDType]
) -> NDArray[Shape1D[THIRTYFIVE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_THIRTYSIX, GenericDType]) -> NDArray[Shape1D[THIRTYSIX], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_THIRTYSEVEN, GenericDType]
) -> NDArray[Shape1D[THIRTYSEVEN], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_THIRTYEIGHT, GenericDType]
) -> NDArray[Shape1D[THIRTYEIGHT], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_THIRTYNINE, GenericDType]
) -> NDArray[Shape1D[THIRTYNINE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FORTY, GenericDType]) -> NDArray[Shape1D[FORTY], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FORTYONE, GenericDType]) -> NDArray[Shape1D[FORTYONE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FORTYTWO, GenericDType]) -> NDArray[Shape1D[FORTYTWO], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_FORTYTHREE, GenericDType]
) -> NDArray[Shape1D[FORTYTHREE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FORTYFOUR, GenericDType]) -> NDArray[Shape1D[FORTYFOUR], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FORTYFIVE, GenericDType]) -> NDArray[Shape1D[FORTYFIVE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FORTYSIX, GenericDType]) -> NDArray[Shape1D[FORTYSIX], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_FORTYSEVEN, GenericDType]
) -> NDArray[Shape1D[FORTYSEVEN], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_FORTYEIGHT, GenericDType]
) -> NDArray[Shape1D[FORTYEIGHT], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FORTYNINE, GenericDType]) -> NDArray[Shape1D[FORTYNINE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FIFTY, GenericDType]) -> NDArray[Shape1D[FIFTY], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FIFTYONE, GenericDType]) -> NDArray[Shape1D[FIFTYONE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FIFTYTWO, GenericDType]) -> NDArray[Shape1D[FIFTYTWO], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_FIFTYTHREE, GenericDType]
) -> NDArray[Shape1D[FIFTYTHREE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FIFTYFOUR, GenericDType]) -> NDArray[Shape1D[FIFTYFOUR], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FIFTYFIVE, GenericDType]) -> NDArray[Shape1D[FIFTYFIVE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FIFTYSIX, GenericDType]) -> NDArray[Shape1D[FIFTYSIX], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_FIFTYSEVEN, GenericDType]
) -> NDArray[Shape1D[FIFTYSEVEN], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_FIFTYEIGHT, GenericDType]
) -> NDArray[Shape1D[FIFTYEIGHT], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_FIFTYNINE, GenericDType]) -> NDArray[Shape1D[FIFTYNINE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_SIXTY, GenericDType]) -> NDArray[Shape1D[SIXTY], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_SIXTYONE, GenericDType]) -> NDArray[Shape1D[SIXTYONE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_SIXTYTWO, GenericDType]) -> NDArray[Shape1D[SIXTYTWO], GenericDType]:
    ...


@overload
def ravel(
    arr: NDArray[SHAPE_2D_MUL_TO_SIXTYTHREE, GenericDType]
) -> NDArray[Shape1D[SIXTYTHREE], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[SHAPE_2D_MUL_TO_SIXTYFOUR, GenericDType]) -> NDArray[Shape1D[SIXTYFOUR], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[Shape2D[T1, ONE], GenericDType]) -> NDArray[Shape1D[T1], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[Shape2D[ONE, T1], GenericDType]) -> NDArray[Shape1D[T1], GenericDType]:
    ...


@overload
def ravel(arr: NDArray[Shape1D[T1], GenericDType]) -> NDArray[Shape1D[T1], GenericDType]:
    ...


def ravel(arr):
    return arr.ravel()

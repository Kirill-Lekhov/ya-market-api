from typing import TypeVar, Callable, cast
from functools import wraps
from warnings import warn


FunctionT = TypeVar("FunctionT", bound=Callable)


def deprecated(
	message: str = "Function {func_name} is deprecated",
	*,
	stacklevel: int = 2,
) -> Callable[[FunctionT], FunctionT]:
	"""
	Marks function as deprecated and shows deprecation warning.

	Args:
		message: Warning message.
		stacklevel: Warning stacklevel (pls see `warning.warn` docs).

	Examples:
		>>> @deprecated()
		>>> def my_func(): ...
		>>> my_func()		# Shows default warning message
		>>> @deprecated("Custom warning message")
		>>> def my_func(): ...
		>>> my_func()		# Shows 'Custom warning message'
	"""
	def wrapper(function: FunctionT) -> FunctionT:
		@wraps(function)
		def inner(*args, **kwargs):
			warn(message.format(func_name=function.__qualname__), DeprecationWarning, stacklevel)
			return function(*args, **kwargs)

		return cast(FunctionT, inner)

	return wrapper

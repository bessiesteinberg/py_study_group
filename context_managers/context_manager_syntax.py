with something_that_returns_a_context_manager() as my_resource:
	do_something(my_resource)

# 'my_resource' will only exist within the indent block

# but this raises the question... what is a context manager??
class Report:

    """
    Report/trace/print each function as you call. As simply as adding a decorator to them.
    """

    def report(func):

        """
        Decorator for reporting when a function starts executing and ends.
        """

        def modified_behaviour(*args, **kwargs):

            print("Started execution of", func.__name__)

            bullshit = func(*args, **kwargs)

            print("Ended execution of", func.__name__)

        return modified_behaviour
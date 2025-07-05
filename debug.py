from warnings import deprecated as _deprecated

class Report:

    """
    Report/trace/print each function as you call. As simply as adding a decorator to them.
    """
    
    def report_function(report_end: bool = True, enable: bool = True, report_parameters: bool = True):

        """
        Decorator for reporting when a function starts executing and ends.

        The parameters and their meaning are:
            - report_end: bool = whatever it should also report when the function stops execution (apart from when it starts), by default true.
            - enable: bool = indicates if the report is done or not in general, by default true.
            - report_parameters: bool = whatever the parameters of the function debugged are also reported.
        """

        def decorator(func):

            if enable:

                def modified_behaviour(*args, **kwargs):

                    print(f"Started execution of {func.__name__}")
                    if report_parameters:
                        print(f"    - Parameters: {args}")
                        print(f"    - Keyword parameters: {kwargs}")

                    bullshit = func(*args, **kwargs)

                    if report_end:
                        print("Ended execution of", func.__name__)

                    return bullshit

                return modified_behaviour
            
            else:

                return func #do no changes
        
        return decorator
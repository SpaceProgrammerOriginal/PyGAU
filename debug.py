from warnings import deprecated as _deprecated

class Report:

    """
    Report/trace/print each function as you call. As simply as adding a decorator to them.
    """

    @_deprecated("Use 'report_function' decorator instead. This decorator will get deleted in version 1.2")
    def report(func):

        """
        Decorator for reporting when a function starts executing and ends.
        """

        def modified_behaviour(*args, **kwargs):

            print("Started execution of", func.__name__)

            bullshit = func(*args, **kwargs)

            print("Ended execution of", func.__name__)

            return bullshit #fixed little bug

        return modified_behaviour
    
    def report_function(report_end: bool = True, enable: bool = True):

        """
        Decorator for reporting when a function starts executing and ends.

        As parameters, it takes "report_end" that indicates whatever it should also report when the function stops execution.
        It also takes "debug" that indicates if the report is done or not.
        """

        def decorator(func):

            if enable:

                def modified_behaviour(*args, **kwargs):

                    print("Started execution of", func.__name__)

                    bullshit = func(*args, **kwargs)

                    if report_end:
                        print("Ended execution of", func.__name__)

                    return bullshit

                return modified_behaviour
            
            else:

                return func #do no changes
        
        return decorator
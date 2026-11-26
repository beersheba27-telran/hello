def minMaxAvg (numbers: list[int])->dict[str, int]:
    """
    returns dictionary with minimal, maximal and rounded to int avg values
    that is dictionary with three pairs if list isn't empty and with no pairs otherwise
    additional requirement: to use function "reduce" (from functools import reduce)
    """
def get_occurrences_counts(strings: list[str])->list[str]:
    """
    returns list of ordered strings
    each output string should have the following structure
    <string from the input list>=><occurrencies count>
    The output list should be sorted by two criteria:
      descending order of counts and ascending order of strings themselves
      example: input list is ["lmn", "vs", "y", "y", "ab", "a", "lmn", "lmn"]
      the output list is ["lmn=>3", "y=>2", "a=>1", "ab=>1", "vs=>1"]
    """
def get_counts_strings(strings: list[str]) -> dict[int, list[str]] :
    """
    returns dictionary with an occurrence count as a key and sorted list of
      strings with the count
    example:  input list is ["lmn", "vs", "y", "y", "ab", "a", "lmn", "lmn"],
    output dict is {3:["lmn"], 2:["y"], 1:["a","ab","vs"]} 
    """ 
def update_with_first_removing[K, V](cache: dict[K, V], entry: tuple[K, V], limit: int)->None:
    """
    if "cache" dictionary already has a key-value pair with first item of a given "entry" as the key
    the key-value pair will be updated with second item of the entry 
    if "cache" dictionary doesn't have a such key-value pair the given "entry" should be added.
    But if the adding new pair will exeed a "limit" the first pair (isertion order) should be deleted
    Example: "cache" - {"a":10, "b":20, "c":30} update_with_first_removing(cache, ("a", 40),3) will update pair with key "a"
    and cache will be {"a":40, "b":20, "c":30}; update_with_first_removing(cache, ("d", 40),3) will add new pair,but
    remove the first one, so cache will be { "b":20, "c":30, "d":40}
    """        
  

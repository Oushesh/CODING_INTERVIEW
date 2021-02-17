##  Feedback
  * A
      * 15 drops, correct solution.
  * D-
    * No signatures, and missing move support except for a brief mention in something referenced from elsewhere, no destructor either.
    ‘When’ is incomplete, only really covering copy construction/assignment.
    ‘Why’ only covers parameterised constructors, and using default and delete for the default constructor.
  * C
        Fails INT_MIN (-minor).
        Doesn’t guard against invalid bases and gets stuck in a loop (-minor).
        Uses a large fixed size buffer without explanation (-major).
        Uses std::swap against advice (-minor).
  * B
        *Doesn’t write to OutBuffer for an empty matrix (-minor).
        Crashes on null matrix (-minor).
        Fails 1x12 and 3x5 (-minor).
        Implemented using recursion rather than a loop.

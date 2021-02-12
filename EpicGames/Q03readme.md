## Unit Tests
   Reference: https://www.rapidtables.com/convert/number/decimal-to-hex.html?x=1567 </br>
   The answers were checked based on the ground truth provided in the link above.
## Note:
    In standard itoa(), negative numbers are handled only with
    base 10. Otherwise numbers are considered unsigned and twos complements
    are used. Here we perform fast_itoa and add -ve infront.
   * Tested with results:</br>
       Input:1567 </br>
       Output:
             Base:10 1567
             Base:2 11000011111
             Base:8 3037
             Base:16 61f

            Input:  -1567

             Base:10 1567
             Base:2 -11000011111
             Base:8 -3037
             Base:16 -61f

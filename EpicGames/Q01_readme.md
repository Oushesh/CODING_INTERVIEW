## Walkthrough the Approach
   * We are on 120 floor with 2 Xbox.
     * Owing to lack of information we make the following assumptions:
       * We do not have terminal velocity and fall is a freefall.
       * The Xbox that survives the fall can be used once more and so on.
       * If the Xbox gets broken when dropped, then it would also get broken if thrown from 1 or more floors above the critical floor.
       * Likewise if Xbox survives from a given floor, it would also survive when thrown from all the ones below it.

    * If we had only 1 Xbox, then I would go on dropping it from the first floor. if no break, then second and so forth... In this case, the worst case would be 120 droppings and highest floor 120.
    * Now, with 2 Xboxes:
      * We cannot directly find the critical given we have only 2 Xboxes, rather than a deterministic approach we need to take a procedural approach to guarantee that the 2 Xboxes will always work.

      * We write the approach mathematically as follows:
        Let's assume the first attempt is on 'Zth' floor.
        If Xbox breaks, we try remaining (Z-1) floors one by one. Worst Case (x trials)
      * If Xbox does not break, we move (x-1) floors up (not exceeding x floor). Now we have (x-1) trials.
        * x+(x-1)
        * If no break: x+(x-1)+(x-2)+...
        * This goes on. x+x(x-1)+x(x-2)+(x-3)+..1
        * But total floor is 120.
        * We have:
          * x+(x-1)+(x-2)+(x-3)+...+1=120
          * x(x+1)/2 = 120
              * x ~ 15

        Ans: [15,15+14,15+14+13,...] =  [15,29,42,54,65,75,84,92,99,105,110,114,117,119,120]

## The different algorithimc style solution
  * Dynamic Programming --> Q01DynamicProgramming.cpp
      * 
  * Optimised version of the Dynamic Proramming.

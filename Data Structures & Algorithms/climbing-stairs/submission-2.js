class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n, memo = {}) {
        if(n in memo) return memo[n];
        if(n <= 2) return n;

        memo[n] = this.climbStairs(n - 1, memo) + this.climbStairs(n - 2, memo)
        
        return memo[n];
    }
}

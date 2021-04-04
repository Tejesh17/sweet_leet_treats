/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    Loop1:
    for (i=0; i<nums.length; i++){
        Loop2:        
        for (j =0; j< nums.length; j++){

            if ( (i!=j) &&(nums[i]+ nums[j] == target)){
                
                return ([i, j])
            }
        }
    }
};
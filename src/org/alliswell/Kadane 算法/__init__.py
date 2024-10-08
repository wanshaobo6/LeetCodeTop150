# Kadane算法‌是一种用于解决最大子数组和问题的动态规划算法。它的核心思想是通过迭代数组的每个元素，维护两个变量来跟踪局部最优解和全局最优解，从而找到包含最大和的连续子数组。这个算法的时间复杂度为O(n)，其中n为数组的长度，意味着它只需要遍历一次数组即可找到最大子数组的和，而空间复杂度为O(1)，即只需要常数级别的额外空间。
# Kadane算法的工作原理可以概括为以下几个步骤：
# ‌初始化‌：设置两个变量，max_so_far和max_ending_here，分别用于记录全局最大和以及以当前元素结尾的子数组的最大和。初始时，这两个变量都设置为数组的第一个元素。
# ‌遍历数组‌：从数组的第二个元素开始遍历整个数组。
# ‌更新最大和‌：对于数组中的每个元素，更新max_ending_here和max_so_far。max_ending_here被设置为当前元素与max_ending_here + 当前元素的较大值，这表示要么开始一个新的子数组（如果当前元素比之前的子数组和大），要么继续当前的子数组（如果加上当前元素后的和更大）。然后，将max_so_far更新为max_so_far和max_ending_here中的较大值，以确保全局最大和始终是最新的。
# ‌返回结果‌：遍历完成后，max_so_far将包含整个数组中最大子数组的和，返回这个值即可。
# Kadane算法的优势在于它能够在一次遍历中就找到最大子数组和，避免了使用传统的暴力搜索方法，大大提高了效率。这个算法不仅适用于最大子数组和问题，还可以衍生出一些变种问题，如寻找数列中最大乘积序列等，常出现在编程面试中‌12。
# ‌Kadane算法‌是一种用于解决最大子数组和问题的动态规划算法。它的核心思想是通过迭代数组的每个元素，维护两个变量来跟踪局部最优解和全局最优解，从而找到包含最大和的连续子数组。这个算法的时间复杂度为O(n)，其中n为数组的长度，意味着它只需要遍历一次数组即可找到最大子数组的和，而空间复杂度为O(1)，即只需要常数级别的额外空间。
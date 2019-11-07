#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def merge_sort(self, nums):
        answer = []  #創一個空的list
        if len(nums) <= 1:  #如果list等於或小於1，就直接回傳該list
            return nums
        mid = int(len(nums)/2)  #找出中間值在哪，拆解list
        left = self.merge_sort(nums[:mid])  
        right = self.merge_sort(nums[mid:])

        while (len(right) > 0) or (len(left) > 0):
            if len(right) > 0 and len(left) > 0:  
                if right[0] > left[0]:
                    answer.append(left[0])
                    left.pop(0)
                else :
                    answer.append(right[0])
                    right.pop(0)
            elif len(right) > 0:
                for i in right:
                    answer.append(i)
                    right.pop(0)
            else:
                for i in left:
                    answer.append(i)
                    left.pop(0)

        return answer


# In[ ]:





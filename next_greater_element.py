class Sol:
    def next_greater_element(self, nums1, nums2):
        list=[]
        for n1 in nums1:
            if nums2.index(n1)+1<len(nums2) and nums2[nums2.index(n1)+1]>n1:
                list.append(nums2[nums2.index(n1)+1])
            else:
                list.append(-1)
        return list

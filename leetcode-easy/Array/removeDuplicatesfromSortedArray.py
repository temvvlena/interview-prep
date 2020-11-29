# 2 cursor ашиглан энэ бодлогыг бодож болно.
def removeDuplicates(self, nums: List[int]) -> int:

    tmp = 1

    # Энэ for loop-ээс нийт хэдэн утга солигдсон болон солигдсон утгууд нь хамгийн хойно байрлуулах болно
    # Worst Case Time: O(n)

    for i in range(1, len(nums)):

        # Эхний cursor нь хамгийн сүүлд солигдсон газрын index зааж өгөх болно
        # Хоёрдох cursor нь "i" бөгөөд дараагийн солигдох ёстой value хайх болно
        # Хэрвээ "i" нь түүний яг доор байрлах  "i-1" тэнцүү биш тохиолдолд, сүүлд солигдсон газрын tmp value нь "i"  value тай тэнцэж, өөрийн утгыг нэгээр нэмэх болно.
        if nums[i] != nums[i-1]:
            nums[tmp] = nums[i]
            tmp += 1
    
    # nums.pop() утга нь хамгийн хойно байрлах утгыг гаргадаг листнээс устгадаг тул, шууд for loop-ын тухайн нийт уртаасаа tmp value хасаж өгвөл, хойно үлдсэн давхар утгуудыг гаргаж болно.
    # Worst Case Time: O(n)
    for i in range(len(nums)-tmp):
        nums.pop()    
    
    return len(nums)
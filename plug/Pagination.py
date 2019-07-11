
class Pagination():
    """分页器"""
    def __init__(self,current_page,maxPageNum,per_page_show=3,page_list_nums=7):
        # 当前页数
        self.current_page = current_page
        # 列表显示数
        self.maxPageNum = maxPageNum
        # 每页记录显示数
        self.per_page_show = per_page_show
        # 最多个数
        self.page_list_nums = page_list_nums

    def start(self):
        pass
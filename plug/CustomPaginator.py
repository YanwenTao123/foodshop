from django.core.paginator import Paginator

class CustomPaginator(Paginator):
    """分页器"""
    def __init__(self,current_page,page_list_nums,*args,**kwargs):
        self.current_page = current_page # 当前页码
        self.page_list_nums = page_list_nums # 当前页面显示的页码列表数
        super(CustomPaginator, self).__init__(*args,**kwargs)

    def page_list_show(self):
        # 总页数小于需显示的数目时：
        if self.current_page < self.num_pages:
            return range(1,self.num_pages)
        # 第一页到显示需显示数目一半时：
        part = int(self.num_pages/2)
        if self.current_page < part:
            return range(1,self.page_list_nums)
        # 最后的页码显示：
        if (self.current_page+part) > self.num_pages:
            return range(self.num_pages-self.page_list_nums+1,self.num_pages+1)
        # 剩余中间页码显示：
        return range(self.current_page-part,self.current_page+part)
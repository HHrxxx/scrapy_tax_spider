# taxSpider
爬取各大税务信息网站的相关文件

目前爬取网站


    国家税务总局----最新文件(http://www.chinatax.gov.cn/chinatax/whmanuscriptList/n810755?_channelName=%E6%9C%80%E6%96%B0%E6%96%87%E4%BB%B6&_isAgg=0&_pageSize=20&_template=index)
    
    
    北京市税务局----基层动态(http://beijing.chinatax.gov.cn/bjswjwz/xwdt/jcdt/)

基于Scrapy框架、数据库MySQL

爬取的内容：


    # 文章标题  title
    # 链接      url
    # 来源      source
    # 发布时间  postTime
    # 内容      content
    # 标记状态  status

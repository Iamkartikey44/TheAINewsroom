import requests

class News:
    def __init__(self,api_key):
        self.api_key = api_key

    def fetch_news(self,query,num_news):
        url = f"https://newsapi.org/v2/everything?q={query}&from=2023-11-03&sortBy=publishedAt&pageSize={num_news}&language=en&apiKey={self.api_key}"   
        response = requests.get(url)
        

        if response.status_code==200:
            news_data = response.json()
         
            return news_data.get("articles",[])
        else:
            return []

    def fetch_news_descriptions(self,query,num_news):
        news = self.fetch_news(query,num_news)
        desc_list = [news_item['description'] for news_item in news]
        
        return desc_list     
    
    def fetch_news_string(self,query,num_news):
        desc_list = self.fetch_news_descriptions(query,num_news)
        desc_string= "\n".join([f"{i+1}. {paragraph}" for i,paragraph in enumerate(desc_list)])
      

        return desc_string
    
   
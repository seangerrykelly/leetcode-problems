# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
# This one seems like kind of a troll. I didn't really do anything
class Codec:

    TINY_URL_BASE = 'http://tinyurl.com/'
    shortUrlToLongUrl = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        urlParts = longUrl.split('/')
        urlPath = urlParts[-1]
        result = self.TINY_URL_BASE + urlPath
        self.shortUrlToLongUrl[result] = longUrl
        return self.TINY_URL_BASE + urlPath
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.shortUrlToLongUrl[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
from urllib import urlencode
import cookielib,urllib2

class Renren(object):
    def __init__(self):
        self.cj = cookielib.LWPCookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)
        self.url = "http://www.renren.com/PLogin.do"
        
    def setinfo(self,domain='',origURL='',username='',password=''):
        self.domain = domain
        self.origURL = origURL
        self.username = username
        self.password = password
        
    def produce_params(self):
        params = {
            'domain':self.domain,
            'origURL':self.origURL,
            'email':self.username,
            'password':self.password,
        }
        return urlencode(params)
        
    def login(self):
        params = self.produce_params()
        r = self.opener.open(self.url,params)
        if r.geturl()=='http://www.renren.com/****':
            print 'Login OK!'
        else:
            print 'Failed!'
            
renren = Renren()
domain = 'renren.com'
origURL = 'http://www.renren.com/Home.do'
username = '****'
password = '****'
renren.setinfo(domain,origURL,username,password)
renren.login()
        

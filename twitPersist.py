class twitPersist:
  
  import time
  
  def __init__(self):
    #rate limiting
    self.time_of_last_hit = int( time.time() )
    
    #messaging
    self.message = ''
    self.last_deleted_message = ''
    self.last_reply_id = ''
  
  def getRateLimit(self, api):
    '''Returns the time in seconds that the program must wait before hitting the API again in order to not exceed the rate limit. If the limit has already been reached, the return value will be the time in seconds until the hourly reset'''
    
    MaxHitFrequency = api.MaximumHitFrequency()
    current_time = int ( time.time() )
    
    #what if rate limit has already been reached?
    if 0 == MaxHitFrequency:
      limit = api.GetRateLimitStatus()
      return limit["reset_time_in_seconds"] - current_time
    
    #otherwise...
    time_since_last_hit = current_time - self.time_of_last_hit
    
    return MaxHitFrequency - time_since_last_hit
    
  def logHit(self):
    self.time_of_last_hit = int( time.time() )
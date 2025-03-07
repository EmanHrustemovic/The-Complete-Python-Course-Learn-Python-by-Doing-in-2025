#CREATING OUR OWN ERROR :

class MyCustomError(TypeError):
    def __init__(self,message,code):
       super().__init__(f'Error code {code} : {message}')
       self.code = code




raise  MyCustomError('OUCH !! An error occurred !', 500)

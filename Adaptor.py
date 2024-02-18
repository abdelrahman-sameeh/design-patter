class Target:
    '''
      this is a target class 
    '''
    
    def request(self) -> str:
      return 'Request From Target Class'


class Adaptee:

    def __init__(self, message) -> None:
        self.message = message
    
    def specific_request(self):
      return self.message


class Adaptor(Target, Adaptee):
    def request(self) -> str:
      return f'Translator Message => {self.specific_request()[::-1]}'


def client_code(target: 'Target'):
    
    print(target.request())


if __name__ == '__main__':

    target = Target()
    
    client_code(target)
    
    print('#'*50)
    
    adaptor = Adaptor(Adaptee('ssalc etpada morf egassem siht').message)
    
    client_code(adaptor)
    

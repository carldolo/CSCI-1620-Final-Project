from controller import *

def main():
    '''
    Executes the application.
    '''
    try:
        app = QApplication([])
        window = Controller()
        window.show()
        app.exec_()
    except Exception as mainError:
        print(mainError)

if __name__ == '__main__':
    main()


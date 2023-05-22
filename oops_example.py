import os

class Tomcat:
    def get_details(self,server_xml):
        self.t_conf = server_xml
        self.t_home = os.path.dirname(os.path.dirname(server_xml))
        return None

    def display_details(self):
        print(f'config file is {self.t_conf}\nhome dir is {self.t_home}')


def main():
    tomcat7 = Tomcat()
    tomcat8 = Tomcat()
    tomcat7.get_details("/home/shaigaut/tomcat7/conf/server.xml")
    tomcat8.get_details("/home/shaigaut/tomcat8/conf/server.xml")
    tomcat7.display_details()
    tomcat8.display_details()
    return None

if __name__ == "__main__":
    main()

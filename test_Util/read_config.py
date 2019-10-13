import configparser


class ReadConfig:
    @staticmethod
    def get_config(file_path, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]


if __name__ == '__main__':
    from test_Util import project_path

    print(ReadConfig.get_config(project_path.test_config_path, 'MODE', 'mode'))

import yaml


class ReadConfig():
    def __init__(self, yaml_file = '../config/config.yaml'):
        self.yaml_file = yaml_file
        self.configs = self._read_yaml()

    def _read_yaml(self):
        with open(self.yaml_file, encoding='utf-8') as f:
            config_dict = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
            return config_dict

    def config(self, path):
        list_path = path.split('.')
        try:
            if len(list_path) < 1:
                print('参数错误！')
            elif len(list_path) == 1:
                return self.configs[list_path[0]]
            else:
                return self.configs[list_path[0]][list_path[1]]
        except:
            print('请检查参数路径是否正确：%s'%path)


    def write_yaml(self):
        with open(self.yaml_file, mode='a', encoding='utf-8') as f:
            data = {'name4':'张崇垚'}
            # allow_unicode=True 可写入中文
            yaml.dump(data, stream=f, allow_unicode=True)

if __name__ == '__main__':
    read_config = ReadConfig('../config/config.yaml')
    print(read_config.config('database.hostname.user'))
    read_config.config('2.3')
    read_config.config('database.port')
    # read_config.write_yaml()
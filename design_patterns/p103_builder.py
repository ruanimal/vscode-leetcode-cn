"""建造者
适用于对象的构建步骤是固定的, 但是每个步骤接收的参数可选项较多
"""

class Computer:

    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None      # 单位为GB
        self.hdd = None         # 单位为GB
        self.gpu = None

    def __str__(self):
        info = ('Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)


class ComputerBuilder:

    def __init__(self):
        self.computer = Computer('AG23385193')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer:
    """Engineer对象就是主管类(Director)
    该类并不是很必要, 有过度设计的嫌疑, 相应的逻辑可以由客户端完成
    """

    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory),
                           self.builder.configure_hdd(hdd),
                           self.builder.configure_gpu(gpu))]

    @property
    def computer(self):
        return self.builder.computer


def main(hdd=500, memory=8, gpu='GeForce GTX 650 Ti'):
    builder = ComputerBuilder()
    builder.configure_memory(memory)
    builder.configure_hdd(hdd)
    builder.configure_gpu(gpu)
    computer = builder.computer
    print(computer)

if __name__ == '__main__':
    main()

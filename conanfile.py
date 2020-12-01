from conans import ConanFile


class ParticlePackage(ConanFile):
    name = 'AdafruitBusIO'
    version = '1.6.0'
    url = 'https://github.com/hicktech/conan-AdafruitBusIO'
    repo_url = 'https://github.com/adafruit/Adafruit_BusIO.git'
    generators = 'cmake'
    settings = []
    requires = []

    def package(self):
        self.copy('*.c*', dst='src', excludes='*examples*')
        self.copy('*.h*', dst='include', excludes='*examples*')

    def source(self):
        self.run(f'git clone {self.repo_url} .')
        self.run(f'git checkout {self.version}')

    def package_info(self):
        self.cpp_info.srcdirs = ['src']

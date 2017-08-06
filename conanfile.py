from conans import ConanFile, CMake, tools
import glob, os

class LuacppConan(ConanFile):
    name = "lua-cpp"
    version = "5.3.4"
    license = "MIT"
    url = "https://github.com/jinq0123/conan-lua-cpp"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    
    __name = "lua-%s" % version

    def source(self):
        zip_name = "%s.tar.gz" % self.__name    
        url = "https://www.lua.org/ftp/%s" % self.zip_name
        download(url, zip_name)
        tools.check_sha1(zip_name, "79790cfd40e09ba796b01a571d4d63b52b1cd950")
        unzip(zip_name)
        os.unlink(zip_name)
        __rename_c_to_cpp()
        
    def build(self):
        cmake = CMake(self)
        self.run('cmake . %s' % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["lua-cpp"]

    
    def __rename_c_to_cpp(self):
        # Rename *.c files to *.cpp
        c = glob.glob(r'src/*.c')
        for f in c:
            print(f)
            # os.rename(f, f + "pp")

from conans import ConanFile, CMake, tools
import glob, os, shutil

class LuacppConan(ConanFile):
    name = "lua-cpp"
    version = "5.3.4"
    license = "MIT"
    url = "https://github.com/jinq0123/conan-lua-cpp"
    description = "Lua %s build as C++" % version
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    exports_sources = "CMakeLists.txt"

    __name = "lua-%s" % version

    def source(self):
        zip_name = "%s.tar.gz" % self.__name
        url = "https://www.lua.org/ftp/%s" % zip_name
        tools.download(url, zip_name)
        tools.check_sha1(zip_name, "79790cfd40e09ba796b01a571d4d63b52b1cd950")
        tools.unzip(zip_name)
        os.unlink(zip_name)
        
        shutil.move("CMakeLists.txt", "%s/CMakeLists.txt" % self.__name)
        self.__rename_c_to_cpp()

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.__name)
        cmake.build()        

    def package(self):
        inc_h = "lua.h", "luaconf.h", "lualib.h", "lauxlib.h", "lua.hpp"
        src_dir = "%s/src" % self.__name
        for h in inc_h:
            self.copy(h, dst="include", src=src_dir)
            
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["lua-cpp"]


    def __rename_c_to_cpp(self):
        # Rename *.c files to *.cpp
        cfiles = glob.glob(r'%s/src/*.c' % self.__name)
        for f in cfiles:
            os.rename(f, f + "pp")
